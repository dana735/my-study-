import json
import math
import time
from pathlib import Path

EPSILON = 1e-9
REPEAT = 10


# 1. MAC: 같은 위치의 숫자를 곱해서 모두 더하기
def mac(matrix, kernel):
    total = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j] * kernel[i][j]
    return total


# 2. 크기와 값의 차이를 보정한 유사도
def similarity(matrix, kernel):
    numerator = mac(matrix, kernel)
    a = mac(matrix, matrix)
    b = mac(kernel, kernel)

    if a == 0 or b == 0:
        return 0.0

    return numerator / math.sqrt(a * b)


# 3. 라벨을 통일하기
def normalize_label(label):
    if not isinstance(label, str):
        return None

    label = label.strip().lower()

    if label in ("+", "cross"):
        return "Cross"
    if label == "x":
        return "X"
    if label == "undecided":
        return "UNDECIDED"

    return None


# 4. 올바른 정사각형 숫자 배열인지 확인
def valid_matrix(matrix, size=None):
    if not isinstance(matrix, list) or not matrix:
        return False

    n = len(matrix)

    if size is not None and n != size:
        return False

    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            return False

        for value in row:
            if isinstance(value, bool):
                return False
            if not isinstance(value, (int, float)):
                return False
            if not math.isfinite(value):
                return False

    return True



# 5. Cross와 X 패턴 판정
def classify(matrix, filters):
    if not valid_matrix(matrix):
        raise ValueError("입력 배열이 올바르지 않습니다.")

    if not isinstance(filters, dict):
        raise ValueError("필터 데이터가 올바르지 않습니다.")

    normalized_filters = {}

    for key, value in filters.items():
        label = normalize_label(key)
        if label in ("Cross", "X"):
            normalized_filters[label] = value

    size = len(matrix)

    for key in ("Cross", "X"):
        if key not in normalized_filters:
            raise ValueError(f"{key} 필터가 없습니다.")
        if not valid_matrix(normalized_filters[key], size):
            raise ValueError(f"{key} 필터가 올바르지 않습니다.")

    cross_score = mac(matrix, normalized_filters["Cross"])
    x_score =mac(matrix, normalized_filters["X"])

    if abs(cross_score - x_score) < EPSILON:
        result = "UNDECIDED"
    elif cross_score > x_score:
        result = "Cross"
    else:
        result = "X"

    return result, cross_score, x_score
    
# 6. 3x3 기본 필터
def make_3x3_filters():
    return {
        "cross": [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ],
        "x": [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    }


# 7. 사용자 직접 입력
def manual_test():
    print("\n[1] 3x3 직접 입력")
    print("한 줄에 숫자 3개씩 입력하세요.")
    print("Enter만 누르면 건너뜁니다.")

    matrix = []

    for i in range(3):
        while True:
            line = input(f"{i + 1}번째 줄: ").strip()

            if not line:
                print("직접 입력을 건너뜁니다.")
                return

            try:
                row = [float(x) for x in line.split()]

                if len(row) != 3:
                    print("숫자를 정확히 3개 입력하세요.")
                    continue

                if not all(math.isfinite(x) for x in row):
                    print("유효한 숫자를 입력하세요.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print("숫자만 입력하세요.")
    start = time.perf_counter()
    result, cross_score, x_score = classify(
        matrix, make_3x3_filters()
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    print(f"Cross 점수: {cross_score:.6f}")
    print(f"X 점수: {x_score:.6f}")
    print(f"판정 결과: {result}")
    print(f"연산 시간: {elapsed_ms:.6f} ms")

# 8. JSON 데이터 검사 및 성능 측정
def json_test(data):
    print("\n[2] JSON 패턴 검사")

    if not isinstance(data, dict):
        print("오류: JSON 최상위 구조가 올바르지 않습니다.")
        return 0, 1, ["JSON 데이터 오류"]   

    filters = data.get("filters")
    patterns = data.get("patterns")

    if not isinstance(filters, dict) or not isinstance(patterns, dict):
        print("오류: filters 또는 patterns가 올바르지 않습니다.")
        return 0, 1, ["JSON 데이터 오류"]     

    passed = 0
    failed = 0
    failed_cases = []
    
    for name, item in patterns.items():
        print(f"\n패턴: {name}")

        try:
            if not isinstance(item, dict):
                raise ValueError("패턴 항목이 객체가 아닙니다.")

            matrix = item.get("input")
            expected = normalize_label(item.get("expected"))

            if expected is None:
                raise ValueError("예상 정답 라벨이 올바르지 않습니다.")

            if not valid_matrix(matrix):
                raise ValueError("입력 배열이 올바르지 않습니다.")

            size = len(matrix)
            filter_name = f"size_{size}"

            if filter_name not in filters:
                raise ValueError(f"{filter_name} 필터가 없습니다.")

            selected_filters = filters[filter_name]

            # 10회 반복하여 평균 계산 시간 측정
            times = []

            for _ in range(REPEAT):
                start = time.perf_counter()

                result, cross_score, x_score = classify(
                    matrix, selected_filters
                )

                elapsed = time.perf_counter() - start
                times.append(elapsed)

            average = sum(times) / REPEAT
            operations = size * size * 2

            correct = result == expected

            if correct:
                passed += 1
                status = "PASS"
            else:
                failed += 1 
                failed_cases.append(name)
                status = "FAIL"

            print(f"크기: {size}x{size}")
            print(f"예상 정답: {expected}")
            print(f"실제 판정: {result}")
            print(f"Cross 점수: {cross_score:.6f}")
            print(f"X 점수: {x_score:.6f}")
            print(f"검사 결과: {status}")
            print(f"10회 평균 시간: {average:.8f}초")
            print(f"MAC 곱셈 횟수(1회 판정): {operations}")

            if not correct:
                print("실패 이유: 예상 정답과 실제 판정이 다릅니다.")

        except (ValueError, TypeError, KeyError, ZeroDivisionError) as error:
            failed += 1
            failed_cases.append(name)
            print("검사 결과: FAIL")
            print(f"실패 이유: {error}")
    return passed, failed, failed_cases


# 9. 최종 보고서
def report(passed, failed, failed_cases):
    total = passed + failed

    print("\n" + "=" * 50)
    print("[3] 최종 결과 보고서")
    print("=" * 50)

    print(f"전체 검사: {total}개")
    print(f"PASS: {passed}개")
    print(f"FAIL: {failed}개")
    print(f"실패 케이스 목록: {failed_cases}")
    if total:
        print(f"정확도: {passed / total * 100:.2f}%")

    print("\n[4] 성능 분석")
    print("각 패턴을 10회 반복 측정했습니다.")
    print("MAC 계산량은 N x N 배열에서 O(N^2)입니다.")
    print("패턴이 커질수록 곱셈과 덧셈 횟수가 늘어납니다.")
    print("시간 측정 결과는 컴퓨터 환경에 따라 달라집니다.")
    print("이 프로그램은 실제 NPU가 아닌 Python 시뮬레이터입니다.")


# 10. 프로그램 실행
def main():
    print("=" * 50)
    print("Mini NPU Simulator - MAC 패턴 분석 V2")
    print("=" * 50)

    path = Path(__file__).resolve().parent / "data.json"

    if not path.exists():
        print("오류: data.json 파일을 찾을 수 없습니다.")
        return

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"JSON 읽기 오류: {error}")
        return

    manual_test()
   
    passed, failed, failed_cases = json_test(data)
    report(passed, failed, failed_cases)

if __name__ == "__main__":
    main()
