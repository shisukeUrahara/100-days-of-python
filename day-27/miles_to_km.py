import tkinter as tk

window = tk.Tk()
window.minsize(width=300, height=200)
window.title("Miles to Km")

my_input = tk.Entry(width=10, bg="white")
my_input.grid(row=0,column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0,column=2)

label1=tk.Label(text='Is equal to')
label1.grid(row=1,column=0)

km_value=0
km_label=tk.Label(text=km_value)
km_label.grid(row=1,column=1)

km__string_label = tk.Label(text='Km')
km__string_label.grid(row=1,column=2)

def convert_units():
    miles_value=float(my_input.get())
    km_value=miles_value*1.60934
    km_label.config(text=km_value)



convert_button=tk.Button(text='Convert',command=convert_units,bg="white",fg="black")
convert_button.grid(row=2,column=1)



window.mainloop()
