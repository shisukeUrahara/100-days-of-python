from operator import truediv

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary['Bug'])
programming_dictionary['Loop']='Iterable in coding '
print(programming_dictionary['Loop'])
# emptying a dictionary
# programming_dictionary={}

print("************************************************************")


# looping through a dictionary
for key in programming_dictionary:
    print("value1 is ,",programming_dictionary[key])

print("************************************************************")

for key,value in programming_dictionary.items():
    print("key , ",key)
    print("value , ",value)

print("************************************************************")


# scores and grades
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


def get_grade_by_score(score):
    if (score >= 91 and score <= 100):
        return 'Outstanding'
    elif (score >= 80 and score <= 90):
        return 'Exceeds Expectations'
    elif (score >= 70 and score <= 80):
        return 'Acceptable'
    else:
        return 'Fail'


def return_list_of_grades(scores):
    grades = {}

    for key, value in scores.items():
        grades[key] = get_grade_by_score(scores[key])

    return grades


student_grades = return_list_of_grades(student_scores)
print(student_grades)



# ********************************** BLIND AUCTION *******************************
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
# TODO-1: Ask the user for input
bids={}
max_bid=0
winner={}
are_more_bidders_present=True

while(are_more_bidders_present):
    name=input("Enter your name: \n")
    bids[name]=int(input('Enter your bid: \n'))

    if(bids[name]>max_bid):
        winner['name']=bids[name]
        winner['max_bid']=bids[name]
        max_bid=bids[name]
    more_bidders= input("Are there any  more bidders? (y/n) \n")
    if(more_bidders=='y'):
        are_more_bidders_present=True
    elif(more_bidders=='n'):
        are_more_bidders_present=False
    else:
        print("Please enter either y or n")

print("max_bid is , ",max_bid)
print(f"winner is , {winner}")


