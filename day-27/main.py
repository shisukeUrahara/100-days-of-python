import tkinter

screen = tkinter.Tk()
screen.title("My First GUI")
screen.minsize(width=500,height=500)

# labels
my_label = tkinter.Label(text='label1',font=('arial',24,'bold'))
#attach label to window
# my_label.pack()
my_label.grid(column=1,row=1)

# button click handler
def button_click_handler():
    my_label.config(text='button clicked')
    print(input_element.get())


# creating buttom
my_button= tkinter.Button(text='my button',font=('arial',14,'bold'),command=button_click_handler)
# my_button.pack()
# place using coordinates , top left is (0,0)
# my_button.place(x=0,y=0)

# place using grid
my_button.grid(row=0,column=2)

# updating labe;
my_label['text'] = 'label1 modified'
my_label.config(font=('arial',24,'bold'))

# entry / input component
input_element=tkinter.Entry(width=20,font=('arial',14,'bold'))

def handle_input_element():
    print(input_element.get())

# print(input_element.get())
# input_element.pack()

input_element.grid(row=0,column=1)

# unlimited args
# her *args in unlimited positional args
def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum

print(add(1,3,4))
print(add(1,2,3,4))
print(add(1,2,3,4,5,6,7,8,9))





# keep the window open and always at the end
screen.mainloop()