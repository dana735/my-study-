
import json
import math
import time
from pathlib import Path
EPSILON = 1e-9

# 1. MAC 연산: 곱한 값을 모두 더하기
def mac(matrix, kernel):
    total = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j] * kernel[i][j]
    return total


# 2. 패턴의 크기 차이를 보정한 점수
def similarity(matrix, kernel):
    score = mac(matrix, kernel)

    matrix_power = mac(matrix, matrix)
    kernel_power = mac(kernel, kernel)

    if matrix_power == 0 or kernel_power == 0:
        return 0.0

    return score / math.sqrt(matrix_power * kernel_power)


# 3. 십자가(+)와 X 중 어떤 패턴인지 판정
def classify(matrix, filters):
    cross_score = similarity(matrix, filters["cross"])
    x_score = similarity(matrix, filters["x"])

    if abs(cross_score - x_score) < EPSILON:
        result = "UNDECIDED"
    elif cross_score > x_score:
        result = "+"
    else:
        result = "x"

    return result, cross_score, x_score   


# 4. 3x3 패턴의 필터 만들기
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


# 5. 사용자에게 3x3 숫자 입력받기
def user_input_test():
    print("\n[1] 사용자 입력 테스트")
    print("3x3 패턴을 입력하세요.")
    print("각 줄에 숫자 3개를 띄어쓰기로 입력합니다.")
    print("Enter만 누르면 이 테스트를 건너뜁니다.")

    matrix = []

    for i in range(3):
        while True:
            line = input(f"{i + 1}번째 줄: ").strip()

            if line == "":
                print("사용자 입력 테스트를 건너뜁니다.")
                return

            try:
                row = [float(x) for x in line.split()]

                if len(row) != 3:
                    print("숫자 3개를 입력해 주세요.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print("숫자만 입력해 주세요.")

    
    start = time.perf_counter()

    result, cross_score, x_score = classify(
        matrix, make_3x3_filters()
    )

    elapsed_ms = (time.perf_counter() - start) * 1000

    print("\nMAC 패턴 분석 결과")
    print(f"십자가 점수: {cross_score:.4f}")
    print(f"X 점수: {x_score:.4f}")
    print(f"판정 결과: {result}")
    print(f"연산 시간: {elapsed_ms:.6f} ms")
   


# 6. JSON 데이터 분석 및 성능 측정
def json_test(data):
    print("\n[2] JSON 데이터 분석")
    print("-" * 55)

    filters = data["filters"]
    patterns = data["patterns"]

    passed = 0
    failed = 0
    performance = {}

    for name, item in patterns.items():
        matrix = item["input"]
        expected = item["expected"]

        size = len(matrix)
        filter_name = f"size_{size}"
        selected_filters = filters[filter_name]

        start = time.perf_counter()

        result, cross_score, x_score = classify(
            matrix, selected_filters
        )

        elapsed = time.perf_counter() - start

        correct = result == expected

        if correct:
            passed += 1
            status = "PASS"
        else:
            failed += 1
            status = "FAIL"

        performance[name] = elapsed

        print(f"\n패턴: {name}")
        print(f"크기: {size}x{size}")
        print(f"예상 정답: {expected}")
        print(f"판정 결과: {result}")
        print(f"십자가 점수: {cross_score:.4f}")
        print(f"X 점수: {x_score:.4f}")
        print(f"검사 결과: {status}")
        print(f"계산 시간: {elapsed:.8f}초")

    return passed, failed, performance


# 7. 결과 보고서
def report(passed, failed, performance):
    total = passed + failed

    print("\n" + "=" * 55)
    print("[3] 최종 결과 보고서")
    print("=" * 55)

    print(f"전체 테스트: {total}개")
    print(f"PASS: {passed}개")
    print(f"FAIL: {failed}개")

    if total > 0:
        accuracy = passed / total * 100
        print(f"정확도: {accuracy:.2f}%")

    print("\n[4] 성능 분석")
    print("MAC 연산의 계산량은 O(N²)입니다.")
    print("패턴 크기가 커지면 계산할 숫자도 많아집니다.")

    for name, elapsed in performance.items():
        print(f"{name}: {elapsed:.8f}초")

    print("\n참고: 실행 시간은 컴퓨터 상태에 따라 달라집니다.")


# 8. 프로그램 시작
def main():
    print("=" * 55)
    print("MAC 연산을 이용한 패턴 분석 프로그램")
    print("=" * 55)

    file_path = Path(__file__).resolve().parent / "data.json"

    if not file_path.exists():
        print("오류: data.json 파일을 찾을 수 없습니다.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"JSON 파일 읽기 오류: {error}")
        return

    user_input_test()

    passed, failed, performance = json_test(data)

    report(passed, failed, performance)


if __name__ == "__main__":
    main()
