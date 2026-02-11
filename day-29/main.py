import tkinter as tk
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def handle_generate_password():
    print("Generating password")
    letter_count=5
    symbol_count=2
    number_count=4
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    # Hard Level
    password_list = []

    for char in range(1, letter_count + 1):
        password_list.append(random.choice(letters))

    for char in range(1, symbol_count + 1):
        password_list += random.choice(symbols)

    for char in range(1, number_count + 1):
        password_list += random.choice(numbers)

    print(password_list)
    random.shuffle(password_list)
    print(password_list)

    password = ""
    for char in password_list:
        password += char

    password_input.insert(0,password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def handle_save_password():
    print("Saving password")
    confirm_input=messagebox.askokcancel(title=website_input.get(),message="Are you sure you want to save this password?")
    print(f"input {confirm_input}")

    if confirm_input == True:
        with open('password.txt', 'a') as f:
            f.write(email_input.get() + " | " + password_input.get() + " | " + website_input.get() + '\n')

        website_input.delete(0, 'end')
        password_input.delete(0, 'end')
        print('Saved password')
    else:
        print('Not saved')





# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
# window.minsize(500,500)
window.config(padx=50,pady=50)
window.configure(background="white")


# adding the image
canvas= tk.Canvas(window,width=200,height=200,highlightthickness=0,bg="white")
logo_img=tk.PhotoImage(file="./logo.png")

canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# website label
website_label= tk.Label(window,text="Website:",bg="white")
website_label.grid(row=1,column=0)

# website input
website_input= tk.Entry(window,width=35,bg="white",fg='black')
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

# email label
email_label= tk.Label(window,text="Email/Username:",bg="white")
email_label.grid(row=2,column=0)

# email input
email_input= tk.Entry(window,width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"test@gmail.com")

# password label
password_label= tk.Label(window,text="Password:",bg="white")
password_label.grid(row=3,column=0)

# password input
password_input= tk.Entry(window,width=21)
password_input.grid(row=3,column=1)

# generate buttton
generate_button=tk.Button(text='Generate',command=handle_generate_password,highlightthickness=0,bg="white",fg="black")
generate_button.grid(row=3,column=2)


# add button
add_button=tk.Button(text='Add',width=33,command=handle_save_password,bg="white",fg="black",highlightthickness=0)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
