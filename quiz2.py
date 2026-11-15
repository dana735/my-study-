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

