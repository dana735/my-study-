# 📚 Python Study & Assignment Log

파이썬 기초 문법과 과제 학습 내용을 기록하는 공간입니다.


---

## 📌 1. 과제 개요 (Overview)
* **학습 주제:** 파이썬 기초 및 실습 과제
* **진행 기간:** 2026년 [11월] [10일] ~ 
* **목표:** 
  * 파이썬 기본 문법(변수, 조건문, 반복문 등) 익히기
  * VS Code와 Git/GitHub 연동 및 버전 관리 익히기

---

## 🛠️ 2. 사용 환경 (Environment)
* **Language:** Python 3.x
* **Editor:** Visual Studio Code (VS Code)
* **Version Control:** Git & GitHub

---

## 📂 3. 주요 학습 내용 (Content)
- * 파이썬 기본 환경 설정 및 실습

1. 변수와 출력 (print)
개념: 상자에 값을 담고(a = 10), 화면에 보여주는(print(a)) 가장 기본 문법입니다.

AI 활용 힌트:  복사해서 AI에게 "이 파이썬 코드 실행 결과가 뭐야?" 

2. 조건문 (if / else)
개념: "만약 ~라면 A를 하고, 아니면 B를 해라" 하는 판단 기준입니다.

AI 활용 힌트: "파이썬에서 점수가 60점 이상이면 합격 출력하는 if문 작성해 줘" 

3. 반복문 (for / while) 및 리스트
개념: 여러 개의 데이터([1, 2, 3])를 순서대로 하나씩 꺼내서 똑같은 작업을 반복하는 것입니다.

AI 활용 힌트: "파이썬 리스트에 있는 퀴즈 문제 3개를 for문으로 하나씩 출력하는 간단한 코드 써줘" 

---

## 💻 3. 주요 학습 내용 (Content)

* **파이썬 기본 환경 설정 및 출력문 / 조건문 실습**
  * 사용자로부터 값을 입력받고 조건에 따라 결과를 다르게 출력하는 기본 문법(`print`, `input`, `if/else`) 학습

  1.변수화 출력(print)

💡 파이썬 코드가 만들어지는 과정 (가장 기본 구조)
코드는 딱 3단계로 이루어집니다.

변수: 상자에 어떤 값을 담는다.

조건문(if/else): 그 상자에 든 값을 가지고 "참인가 거짓인가" 판단한다.

출력(print): 판단 결과에 맞춰 화면에 글자를 보여준다.

💻 80점 기준으로 만든 실제 파이썬 코드 예시


```python
# 점수에 따른 합격 여부 판별 예제
score = int(input("점수를 입력하세요: "))

*60점 기준 
score = 60

if score >= 60:
    print("합격입니다!")
else:
    print("불합격입니다.")
- * 조건문과 반복문 활용 (예제 코드 작성)

# 1단계: 변수 (성적 값을 상자에 담기)
score = 85

# 2단계: 조건문 및 3단계: 출력 (판단해서 화면에 보여주기)
if score >= 80:
    print("합격입니다!")
else:
    print("불합격입니다.")


다른 예

score = 85  # 변수(score)에 85점을 저장

if score >= 80:
    print("합격")  # 80점 이상일 때 실행
else:
    print("불합격")  # 80점 미만일 때 실행

    score = 85 : 점수라는 변수에 숫자 85를 담았습니다.

if score >= 80: : "만약 score가 80 이상이면?" 하고 물어보는 조건문(명령어)입니다.

print("합격") : 조건이 맞으니까 화면에 "합격"을 출력해 줍니다.


![alt text](image.png)

3. 반복문 (for)은 언제 쓰나요?
반복문은 "여러 개 들어있는 목록(리스트)에서 하나씩 꺼내서 똑같은 일을 반복시킬 때" 사용합니다.


---# 과일 목록(리스트) 상자를 만듭니다.
fruits = ["사과", "바나나", "딸기"]

# for문을 써서 목록에서 하나씩 꺼내서 print로 출력합니다.


for f in fruits:
    print(f)



🔍 컴퓨터가 동작하는 순서
fruits 상자 안에서 첫 번째 "사과"를 꺼내 f에 넣고 print ➔ 화면에 사과 출력

두 번째 "바나나"를 꺼내 f에 넣고 print ➔ 화면에 바나나 출력

세 번째 "딸기"를 꺼내 f에 넣고 print ➔ 화면에 딸기 출력

더 이상 꺼낼 게 없으니 반복 끝!


다음 파이썬 코드를 실행했을 때 화면에 출력되는 결과로 올바른 것은?

numbers = [10, 20, 30]
for num in numbers:
    print(num)

    10
    20
    30

*for vs while 차이점 한눈에 보기
for (개수가 정해져 있을 때): "목록에 있는 것 처음부터 끝까지(3번만) 반복해!"

while (조건이 참일 동안 계속): "~하는 동안 끝없이(조건이 끝날 때까지) 계속 반복해!"

while문 코드 예시
"숫자가 1부터 시작해서 3이 될 때까지 계속 반복해라" 할 때 while을 씁니다.

count = 1

while count <= 3:
    print(count)
    count = count + 1  # 숫자를 1씩 더해줍니다.

    🔍 컴퓨터가 동작하는 순서
count가 1입니다. (3 이하가 맞으니 화면에 1 출력 ➔ 숫자가 2가 됨)

count가 2입니다. (3 이하가 맞으니 화면에 2 출력 ➔ 숫자가 3이 됨)

count가 3입니다. (3 이하가 맞으니 화면에 3 출력 ➔ 숫자가 4가 됨)

count가 4가 되면 "3 이하"라는 조건에 맞지 않으므로 반복 중단!

**for가 보이면 👉 "아, 정해진 리스트나 개수만큼 하나씩 순서대로 반복하는구나!"

while이 보이면 👉 "아, 조건이 맞는 동안 숫자를 올려가며 계속 반복하는구나



퀴즈 실행 

<img width="148" height="149" alt="image" src="https://github.com/user-attachments/assets/75657bcf-ad1c-4fb6-8949-802576ca81ad" />

<img width="746" height="295" alt="image" src="https://github.com/user-attachments/assets/102b4d6a-21a6-4d8e-a228-491df78cf786" />


## 💡 4. 오늘의 느낀 점 & 배운 점
* 코딩을 직접 실습하면서 에러를 해결하는 과정이 흥미로웠습니다. 

if else 가  같은 선에 있어야 에러 안난다 

* 마크다운 문법을 활용해 공부한 내용을 보기 좋게 정리하는 법을 배웠습니다.


대한민국의 수도는?", "서울"


<img width="704" height="416" alt="image" src="https://github.com/user-attachments/assets/bf92366c-350b-4eda-9eb4-45af9ed7aa70" />

 (quiz2.py)

```python
# quiz2.py

class QuizGame:
    def __init__(self):
        # 퀴즈 목록과 점수를 초기화합니다.
        self.quizzes = []
        self.score = 0

    def add_quiz(self, question, answer):
        # 문제를 추가하는 기능입니다.
        self.quizzes.append({"question": question, "answer": answer})

    def run(self):
        # 게임을 실행하는 기능입니다.
        print("\n--- 퀴즈 게임을 시작합니다! ---")
        for q in self.quizzes:
            user_ans = input(f"문제: {q['question']} 정답은? ")
            if user_ans == q['answer']:
                print("정답입니다! ✨")
                self.score += 1
            else:
                print(f"아쉽네요. 정답은 [{q['answer']}]입니다. 😅")
        
        print(f"\n[게임 종료] 총 {len(self.quizzes)}문제 중 {self.score}문제를 맞혔습니다!")

# 여기서부터는 실제 게임을 실행하는 부분입니다.


if __name__ == "__main__":
    game = QuizGame()
    
    # 문제 추가 (원하는 대로 수정 가능!)
    game.add_quiz("대한민국의 수도는?", "서울")
    game.add_quiz("파이썬 파일의 확장자는?", ".py")
    game.add_quiz("1 + 1은?", "2")
    
    # 게임 시작
    game.run()

## 퀴즈 주제 선정 이유
파이썬 프로그래밍의 기초 개념(데이터 타입, 함수, 클래스 등)을 재미있게 복습하기 위해 선정하였습니다.

## 기능 목록
- 퀴즈 풀기: 등록된 문제를 풀고 점수를 계산합니다.
- 퀴즈 등록: 사용자가 새로운 문제를 추가할 수 있습니다.
- 목록 보기: 현재 저장된 모든 퀴즈와 정답을 확인합니다.
- 최고 점수 확인: 파일에 저장된 역대 최고 점수를 보여줍니다.
- 자동 저장: 모든 데이터는 `state.json`에 실시간으로 저장됩니다.

## 파일 구조
- `quiz2.py`: 메인 프로그램 코드
- `state.json`: 퀴즈 데이터 및 최고 점수 저장 파일 (UTF-8)




  
