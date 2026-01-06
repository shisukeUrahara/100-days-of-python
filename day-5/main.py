import random
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)


#  highest scores
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
total_exam_score=sum(student_scores)
averge_score=total_exam_score/len(student_scores)
max_score=max(student_scores)
max_loop_score=0;
# implementing max function from above
for score in student_scores:
    if score > max_loop_score:
        max_loop_score=score

print(f"total score is {total_exam_score}")
print(f"average score is {averge_score}")
print(f"maximum score is {max_score}")
print(f"loop max score is {max_loop_score}")

# ranges
for number in range(1, 11):
    print(number)

#  range step with 2
for number in range(1, 11,2):
    print(number)

# fizzBuzz test
for number in range(1,101):
    temp_result=''
    if(number%3==0):
        temp_result+='Fizz'
    if(number%5==0):
        temp_result+='Buzz'
    print(temp_result or number)

