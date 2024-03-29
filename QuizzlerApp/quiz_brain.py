import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answser):
        if user_answer.lower() == correct_answser.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong...")
        print(f"The correct answer is: {correct_answser}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}.")
        print("\n")
