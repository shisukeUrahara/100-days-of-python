class User:
    def __init__(self,id, name):
        self.id = id
        self.name = name
        self.followers=0
        self.following=0

    def follow(self,user):
        self.following+=1
        user.followers+=1

user_1=User(1,"shisuke")
print(user_1.name)


user_2=User(2,"toji")
print(user_2.name)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

# quiz app
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
# initializing questions
for question in question_data:
    current_question= Question(question["text"],question["answer"])
    question_bank.append(current_question)

quiz = QuizBrain(question_bank)

def start_quiz(quiz):
    while quiz.still_has_questions():
        quiz.next_question()

    print(f"Quiz completed , your score is {quiz.score}.")

start_quiz(quiz)




