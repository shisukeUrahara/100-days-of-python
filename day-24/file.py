# this methods needs file to be closed
file= open("my_file.txt")
content= file.read()
print(content)
file.close()

print("********************************************************************")
# this method does file.close automatically
with open("my_file.txt") as file2:
    content2= file2.read()
    print(content2)

print("*******************write mode**********************************")
# with open("my_file.txt",'w') as file3:
#     #this overwrites everything
#     file3.write("I like anime")
#
print("***********************append mode******************************")
with open("my_file.txt",'a') as file3:
    #this overwrites everything
    file3.write("\n I like anime")

print("**********************************************************")
