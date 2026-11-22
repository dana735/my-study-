
import json
from pathlib import Path

# 1. 기본 MAC 계산: 같은 위치끼리 곱해서 모두 더하기
def mac(matrix, kernel):
    total = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j] * kernel[i][j]
    return total


# 2. 출제자가 제공한 JSON 파일 읽기
file_path = Path(__file__).parent / "data.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)


# 3. 모든 패턴 검사
success = 0
failure = 0
tie = 0

for name, item in data["patterns"].items():
    size = name.rsplit("_", 1)[0]
    filters = data["filters"][size]

    cross_score = mac(item["input"], filters["cross"])
    x_score = mac(item["input"], filters["x"])

    expected = item["expected"]

    if cross_score > x_score:
        predicted = "+"
    elif x_score > cross_score:
        predicted = "x"
    else:
        predicted = "동점"

    if predicted == "동점":
        tie += 1
        result = "동점 - 판정 불가"
    elif predicted == expected:
        success += 1
        result = "성공"
    else:
        failure += 1
        result = "실패"

    print(f"\n검사: {name}")
    print(f"Cross 점수: {cross_score:.2f}")
    print(f"X 점수: {x_score:.2f}")
    print(f"정답: {expected}")
    print(f"예측: {predicted}")
    print(f"결과: {result}")

print("\n===== 최종 결과 =====")
print(f"성공: {success}개")
print(f"실패: {failure}개")
print(f"동점(판정 불가): {tie}개")
print(f"전체: {success + failure + tie}개")
