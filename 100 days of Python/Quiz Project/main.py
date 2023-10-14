from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q['text'],q['answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():

    quiz_brain.next_question()

print(f'Congrats, you finished the quiz!\nYour final score was {quiz_brain.user_score}/{quiz_brain.question_number}')