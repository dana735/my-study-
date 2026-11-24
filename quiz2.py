
# quiz2.py

import json
from pathlib import Path

# 데이터 저장 파일 위치
STATE_FILE = Path(__file__).parent / "state.json"


class QuizGame:

    def __init__(self):
        self.quizzes = []
        self.score = 0
        self.high_score = 0
        self.load_data()

    # 기본 문제 생성
    def default_quizzes(self):
        return [
            {"question": "대한민국의 수도는?", "answer": "서울"},
            {"question": "파이썬 파일의 확장자는?", "answer": ".py"},
            {"question": "1 + 1은?", "answer": "2"}
        ]

    # 데이터 저장
    def save_data(self):
        data = {
            "quizzes": self.quizzes,
            "high_score": self.high_score
        }

        try:
            temp_file = STATE_FILE.with_suffix(".tmp")

            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            temp_file.replace(STATE_FILE)
            print("데이터가 저장되었습니다.")

        except OSError as e:
            print("저장 오류:", e)

    # 데이터 불러오기
    def load_data(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            quizzes = data["quizzes"]
            high_score = data["high_score"]

            # 데이터 구조 검사
            if not isinstance(quizzes, list):
                raise ValueError("문제 목록 형식 오류")

            if type(high_score) is not int or high_score < 0:
                raise ValueError("최고 점수 형식 오류")

            for q in quizzes:
                if not isinstance(q, dict):
                    raise ValueError("문제 형식 오류")

                for key in ("question", "answer"):
                    if not isinstance(q.get(key), str):
                        raise ValueError("문제 데이터 오류")
                    if not q[key].strip():
                        raise ValueError("빈 문제 또는 정답")

            self.quizzes = quizzes
            self.high_score = high_score
            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            self.quizzes = self.default_quizzes()
            self.save_data()

        except (ValueError, KeyError, TypeError, OSError) as e:
            print("데이터 불러오기 오류:", e)

            # 손상된 파일 백업
            try:
                backup = STATE_FILE.with_suffix(".json.bak")
                if STATE_FILE.exists():
                    if backup.exists():
                        raise OSError("기존 백업 파일이 있습니다.")
                    STATE_FILE.rename(backup)
                    print("기존 파일을 백업했습니다.")
            except OSError as error:
                print("백업 실패:", error)
                raise SystemExit("데이터 보호를 위해 종료합니다.")

            self.quizzes = self.default_quizzes()
            self.high_score = 0
            self.save_data()

    # 빈 입력 검사
    def get_input(self, message):
        while True:
            value = input(message).strip()

            if value:
                return value

            print("빈 입력은 허용되지 않습니다.")

    # 문제 추가
    def add_quiz(self, question, answer):
        question = question.strip()
        answer = answer.strip()

        if not question or not answer:
            print("문제와 정답을 모두 입력하세요.")
            return

        self.quizzes.append({
            "question": question,
            "answer": answer
        })

        print("새로운 문제가 등록되었습니다.")
        self.save_data()

    # 사용자 문제 등록
    def register_quiz(self):
        question = self.get_input("새로운 문제: ")
        answer = self.get_input("정답: ")
        self.add_quiz(question, answer)

    # 문제 목록 확인
    def show_quizzes(self):
        print("\n--- 등록된 문제 목록 ---")

        for i, q in enumerate(self.quizzes, start=1):
            print(f"{i}. {q['question']}")

        print(f"전체 문제 수: {len(self.quizzes)}개")

    # 퀴즈 게임 실행
    def run(self):
        self.score = 0

        if not self.quizzes:
            print("등록된 문제가 없습니다.")
            return

        print("\n--- 퀴즈 게임을 시작합니다! ---")

        for q in self.quizzes:
            user_ans = self.get_input(
                f"문제: {q['question']} 정답은? "
            )

            if user_ans.casefold() == q["answer"].strip().casefold():
                print("정답입니다! ✨")
                self.score += 1
            else:
                print(f"오답입니다. 정답: {q['answer']}")

        print(f"\n총 {len(self.quizzes)}문제 중 "
              f"{self.score}문제를 맞혔습니다!")

        # 최고 점수 갱신
        if self.score > self.high_score:
            self.high_score = self.score
            print("최고 점수를 갱신했습니다!")

        self.save_data()

    # 메인 메뉴
    def menu(self):
        try:
            while True:
                print("\n===== 파이썬 퀴즈 게임 =====")
                print("1. 퀴즈 풀기")
                print("2. 새로운 문제 등록")
                print("3. 문제 목록 보기")
                print("4. 최고 점수 확인")
                print("5. 종료")

                choice = self.get_input("메뉴 선택: ")

                if choice == "1":
                    self.run()

                elif choice == "2":
                    self.register_quiz()

                elif choice == "3":
                    self.show_quizzes()

                elif choice == "4":
                    print(f"최고 점수: {self.high_score}점")

                elif choice == "5":
                    self.save_data()
                    print("프로그램을 종료합니다.")
                    break

                else:
                    print("1~5 사이의 번호를 입력하세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n프로그램 실행이 중단되었습니다.")
            self.save_data()
            print("종료합니다.")


# 프로그램 시작
if __name__ == "__main__":
    game = QuizGame()
    game.menu()
