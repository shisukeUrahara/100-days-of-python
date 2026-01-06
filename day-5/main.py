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

# password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
