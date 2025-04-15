class QuizBrain():
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0 
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    def  answer_correction(self,user_res ,c_answer):
        if user_res == c_answer:
            self.user_score += 1
            print("You got it right")
            print(f"The correct answer is {c_answer}")
            print(f"your score is {self.user_score}/{self.question_number}")
        else:
            print("You got it wrong")
            print(f"The correct answer is {c_answer}")
            print(f"your score is {self.user_score}/{self.question_number}")
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_res = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ") 
        self.answer_correction(user_res , current_question.answer)
        print("\n")
        


    
    
