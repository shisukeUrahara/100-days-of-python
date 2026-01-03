len("Hello")
word="hello"
print(word[0])
print(word[1])
print(word[-1])
# figure out type of data type
print(type("hello"))
print(type(len("hello")))
print(type(True))
print(type(1.25))

# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# type conversion
# print("your name is "+str(len(input("whats your name? ")))+" characters long")
print(5/3) # always results in floating point number
print(5//3) # // translates to python's version of parseInt

#  calculating bmi
weight_in_kg=84
height_in_m=1.65
bmi = weight_in_kg / height_in_m ** 2
print("your bmi is "+str(bmi))
print("your int bmi is "+str(int(bmi)))
print("your rounded bmi is "+str(round(bmi)))
print("your rounded bmi to 3 places is "+str(round(bmi,3)))

# f strings in python
score=100
print(f"Your score is {score}%")

# tip calculator
print("Welcome to tip calculator \n")
bill=float(input("whats your bill? \n"))
tip=(input("choose one of the tipping options ? 10% , 12% or 15% \n "))
num_of_people=int(input("how many people are in your group? \n"))
multiplier= 1.10
if(tip=="12"):
    multiplier=1.12
elif(tip=="15"):
    multiplier=1.15

total_bill=(round(bill*multiplier))
bill_per_person=total_bill/num_of_people
print(f"Your total bill is ${total_bill}")
print(f"each friend will pay {round(bill_per_person,2)}")



