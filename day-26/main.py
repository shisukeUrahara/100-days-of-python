# list comprehension

# squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]
print(squared_numbers)

# getting even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)

# common numbers
list1 = []
list2 = []

with open('file1.txt') as file:
    content = file.readlines()
    print(content)
    list1 = [int(num) for num in content]
    print(list1)

with open('file2.txt') as file:
    content = file.readlines()
    print(content)
    list2 = [int(num) for num in content]
    print(list2)

result = [num for num in list1 if num in list1 and num in list2]

print(result)

#dictionary comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list=sentence.split()
print(word_list)
result = {item:len(item) for item in sentence.split()}
print(result)


# converting temperatures
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key:value*9/5+32 for (key,value) in weather_c.items()}

print(weather_f)

# iterate through pandas data frame
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [20, 25, 30]
})

for idx, row in df.iterrows():
    print(idx, row["name"], row["age"])
