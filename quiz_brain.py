class quizes:
    def __init__(self, q_list):
        self.question_number=0
        self.user_score=0
        self.q_list=q_list

    #this method prints out the next  question.
    def next_question(self):
        current_question=self.q_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True or False?): ")
        self.check_answer(user_answer, current_question.answer)

    #CHECKS IF THERE ARE STILL MORE QUESTIONS IN QUESTION LIST
    def still_has_question(self):

        # this returns true if the number we are on is still less than the length of the question list.
        return self.question_number<len(self.q_list)
        
    #this checks if our answer is correct or not.    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.user_score+=1
            print("You got it right!")
        else:
            print("Oops.. That is Wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.user_score}/{self.question_number}") 
        print("\n")  