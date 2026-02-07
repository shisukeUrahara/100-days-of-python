
with open('weather_data.csv') as file:
    content=file.readlines()
    print(content)
print("***************************************************************")

import csv
with open('weather_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    temp=[]
    # loop through csv reader object
    for row in csvreader:
        print(row)
        if(row[1]!='temp'):
            temp.append(int(row[1]))

    print(temp)

print("***************************************************************")

# pandas library for better functionality to deal with data
import pandas
data=pandas.read_csv('weather_data.csv')
print(data)
print(data['temp'])
# we can check type of data returned by panda
print("***************************************************************")
# dataframe i.e the whole table
print(type(data))
# series i.e a single column in the table
print(type(data['temp']))
# converting data tp dict
dict_data= data.to_dict()
print(dict_data)

#converting series to list
series_list_data=data['temp'].to_list()
print(series_list_data)

#finding average temperature using pandas
average= data['temp'].mean()
print(average)

#create a dataframe from scratch
data_dict={
    "students":['joe','ross'],
    "scores":[56,85]
}

new_data_frame= pandas.DataFrame(data_dict)
print(new_data_frame)
# write this new data frame to a csv file
new_data_frame.to_csv('score_data.csv')

