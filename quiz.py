import json
import os

# 1. 개별 퀴즈를 담당하는 Quiz 클래스
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question      # 문제
        self.choices = choices        # 보기 (4개)
        self.answer = answer          # 정답 번호 (1~4)

# 2. 전체 게임 진행과 메뉴를 담당하는 QuizGame 클래스
class QuizGame:
    def __init__(self):
        self.score = 0
        self.quizzes = [
            Quiz("파이썬의 창시자는 누구인가요?", ["1. 토마스 앤더슨", "2. 귀도 반 로섬", "3. 빌 게이츠", "4. 스티브 잡스"], 2),
            Quiz("다음 중 파이썬 기본 데이터 타입이 아닌 것은?", ["1. int", "2. str", "3. array", "4. bool"], 3),
            Quiz("조건을 처리할 때 사용하는 키워드가 아닌 것은?", ["1. if", "2. elif", "3. switch", "4. else"], 3),
            Quiz("반복문 종류로 올바른 것은?", ["1. for / while", "2. try / except", "3. open / close", "4. input / print"], 1),
            Quiz("데이터를 파일에 저장할 때 주로 사용하는 텍스트 형식은?", ["1. html", "2. json", "3. css", "4. py"], 2)
        ]

    def run(self):
        while True:
            print("\n=== 🧠 파이썬 기초 퀴즈 게임 ===")
            print("1. 퀴즈 풀기")
            print("2. 점수 확인")
            print("3. 종료")
            
            choice = input("원하는 메뉴 번호를 입력하세요: ").strip()
            
            if choice == '1':
                self.play_quiz()
            elif choice == '2':
                print(f"\n현재 내 점수: {self.score}점")
            elif choice == '3':
                print("\n프로그램을 종료합니다. 수고하셨습니다!")
                break
            else:
                print("\n[오류] 잘못된 입력입니다. 1~3 사이의 숫자를 입력해주세요.")

    def play_quiz(self):
        print("\n--- 퀴즈를 시작합니다! ---")
        self.score = 0
        for i, q in enumerate(self.quizzes, 1):
            print(f"\n문제 {i}. {q.question}")
            for c in q.choices:
                print(c)
            
            ans = input("정답 번호 입력 (1~4): ").strip()
            if ans.isdigit() and int(ans) == q.answer:
                print("정답입니다! 👏")
                self.score += 20
            else:
                print(f"틀렸습니다! 정답은 {q.answer}번입니다.")
        print(f"\n퀴즈 종료! 총 점수: {self.score}/100점")

if __name__ == "__main__":
    game = QuizGame()
    game.run()