from question_model import ModelQuestion
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(ModelQuestion(question["question"], (question["correct_answer"])))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations, you have finished the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
