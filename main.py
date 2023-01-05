from question_model import Question
from data import question_data
from quiz_brain import quizes

question_bank=[]
for questions in question_data:
    my_quest=questions["text"]
    my_answer=questions["answer"]
    model=Question(my_quest, my_answer)
    question_bank.append(model)

my_quizes=quizes(question_bank)

# this calls next question method while true.
while my_quizes.still_has_question():
    my_quizes.next_question()

print("You've completed the Quiz")
print(f"Your Total Score is {my_quizes.user_score}/{my_quizes.question_number}")