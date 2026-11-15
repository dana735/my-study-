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
## * 프로젝트 구조 설계
먼저 코드를 작성하기 전, 파일 구조를 아래와 같이 잡는 것을 추천합니다.


my-study/
├── .gitignore       # 파이썬 캐시 파일 등을 제외
├── README.md        # 프로젝트 설명서
├── state.json       # 데이터 저장 파일 (자동 생성)
└── quiz.py          # 메인 실행 코드


.gitignore 파일 만들기 
내용에 __pycache__/ 라고 한 줄만 적고 저장 (파이썬 실행 시 생기는 불필요한 파일을 Git이 무시하게 해줌.)


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

## 💻 4. 주요 학습 내용 (Content)

* **파이썬 기본 환경 설정 및 출력문 / 조건문 실습**
  * 사용자로부터 값을 입력받고 조건에 따라 결과를 다르게 출력하는 기본 문법(`print`, `input`, `if/else`) 학습

### 과제 1: 기초 퀴즈 프로그램 (`quiz.py`)
- **내용**: 변수, 조건문, 반복문을 활용한 간단한 퀴즈 프로그램


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

 ![퀴즈 실행 화면](images/퀴즈실행.png)

 ![터미널 화면](images/terminal.png)
 


퀴즈 실행 

![alt text](image-2.png)



## 💡 4. 오늘의 느낀 점 & 배운 점
* 코딩을 직접 실습하면서 에러를 해결하는 과정이 흥미로웠습니다. 

if else 가  같은 선에 있어야 에러 안난다

*마크다운 문법을 활용해 공부한 내용을 보기 좋게 정리하는 법을 배웠습니다

[Quiz 클래스]
개별 퀴즈의 정보를 담고 출력하는 역할을 합니다.

python
📋 복사
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices  # 리스트 형태 [문항1, 문항2, 문항3, 문항4]
        self.answer = answer    # 정답 번호 (1~4)

    def display(self, index):
        """문제를 화면에 출력합니다."""
        print(f"\nQ{index}. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}) {choice}")

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }


[QuizGame 클래스]
게임의 전체 흐름(데이터 로드, 메뉴 출력, 퀴즈 진행)을 관리합니다.

python
📋 복사
import json
import os

class QuizGame:
    def __init__(self):
        self.file_path = "state.json"
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def load_data(self):
        """파일에서 데이터를 불러오거나 초기화합니다."""
        if not os.path.exists(self.file_path):
            self.set_default_quizzes()
            return

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
        except (json.JSONDecodeError, Exception):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 시작합니다.")
            self.set_default_quizzes()

    def save_data(self):
        """현재 상태를 JSON 파일로 저장합니다."""
        data = {
            "best_score": self.best_score,
            "quizzes": [q.to_dict() for q in self.quizzes]
        }
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def set_default_quizzes(self):
        """기본 퀴즈 5개를 설정합니다."""
        # 예시 데이터 (본인의 주제에 맞게 수정하세요!)
        default_data = [
            {"question": "파이썬의 창시자는?", "choices": ["귀도 반 로섬", "제임스 고슬링", "빌 게이츠", "데니스 리치"], "answer": 1},
            # ... 추가 4개 더 작성
        ]
        self.quizzes = [Quiz(**q) for q in default_data]
        self.save_data()

    # 추가 메서드들: play_quiz(), add_quiz(), show_menu() 등 구현




### 과제 2. 클래스를 활용한 퀴즈 게임 (`quiz2.py`) ✅ (New!)
- **내용**: 클래스(Class)와 객체(Object)를 활용하여 구조화된 퀴즈 게임 구현
- **학습 포인트**: 
  - `Quiz` 클래스: 문제와 정답 데이터 관리
  - `QuizGame` 클래스: 게임 실행 로직(점수 계산, 진행) 관리
  - 객체 지향 프로그래밍(OOP)의 기초 이해


import json
import os

# 1. 퀴즈 정보를 담는 클래스
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {"question": self.question, "answer": self.answer}

# 2. 게임 로직 및 데이터 관리를 담당하는 클래스
class QuizGame:
    def __init__(self, filename='state.json'):
        self.filename = filename
        self.quizzes = []
        self.high_score = 0
        self.load_data()

        # 기본 퀴즈가 없을 경우 5개 추가
        if not self.quizzes:
            self.add_default_quizzes()

    def add_default_quizzes(self):
        default_data = [
            Quiz("파이썬의 창시자는? (영문)", "Guido van Rossum"),
            Quiz("리스트에 요소를 추가하는 메서드는?", "append"),
            Quiz("파이썬 파일의 확장자는?", ".py"),
            Quiz("정수형을 뜻하는 파이썬 예약어는?", "int"),
            Quiz("출력을 담당하는 함수는?", "print")
        ]
        self.quizzes.extend(default_data)
        self.save_data()

    # 데이터 불러오기 (JSON)
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.quizzes = [Quiz(q['question'], q['answer']) for q in data.get('quizzes', [])]
                    self.high_score = data.get('high_score', 0)
            except Exception as e:
                print(f"데이터 로드 중 오류 발생: {e}")

    # 데이터 저장하기 (JSON)
    def save_data(self):
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "high_score": self.high_score
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # 퀴즈 풀기
    def play(self):
        print("\n--- 퀴즈를 시작합니다! ---")
        current_score = 0
        for q in self.quizzes:
            user_ans = input(f"{q.question}: ")
            if user_ans.strip().lower() == q.answer.lower():
                print("정답입니다!")
                current_score += 1
            else:
                print(f"틀렸습니다. 정답은 {q.answer}입니다.")
        
        print(f"\n최종 점수: {current_score}/{len(self.quizzes)}")
        
        if current_score > self.high_score:
            print("✨ 최고 기록 경신! ✨")
            self.high_score = current_score
            self.save_data()

    # 퀴즈 추가
    def add_quiz(self):
        question = input("새로운 퀴즈 질문을 입력하세요: ")
        answer = input("정답을 입력하세요: ")
        self.quizzes.append(Quiz(question, answer))
        self.save_data()
        print("퀴즈가 성공적으로 추가되었습니다.")

    # 퀴즈 목록 보기
    def show_list(self):
        print("\n--- 퀴즈 목록 ---")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question} (정답: {q.answer})")

    # 점수 확인
    def show_score(self):
        print(f"\n현재 최고 점수: {self.high_score}점")

# 3. 메인 메뉴 실행
def main():
    game = QuizGame()

    while True:
        print("\n[ 파이썬 퀴즈 프로그램 ]")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 등록")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")
        
        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            game.play()
        elif choice == '2':
            game.add_quiz()
        elif choice == '3':
            game.show_list()
        elif choice == '4':
            game.show_score()
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()


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

## 🛠 주요 기능 업데이트
- **JSON 데이터 저장**: 퀴즈 점수와 진행 상황이 `state.json` 파일에 자동으로 저장됩니다.
- **메뉴 시스템**: 퀴즈 풀기, 문제 등록, 종료 기능을 선택할 수 있습니다.

## 💾 데이터 저장 방식 (JSON)
이 프로그램은 파이썬의 `json` 모듈을 사용하여 데이터를 관리합니다. 
프로그램을 종료해도 `state.json` 파일에 기록이 남기 때문에 다음 실행 시 점수를 이어갈 수 있습니다.