import tkinter as tk
from os import times_result

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def handle_reset():
    global timer
    print('reset handler called')
    if(timer!=None):
        window.after_cancel(timer)
        header_label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text,text = "00:00")


    # header_label.config(text="Timer",fg=GREEN)
    # canvas.itemconfig(times_text text="00:00",fg=PINK)

def handle_start():
    global rep
    print('start handler called')
    rep+=1
    # count_down(WORK_MIN)
    WORK_MIN_IN_SECONDS = WORK_MIN *60
    SHORT_BREAK_MIN_IN_SECONDS = SHORT_BREAK_MIN *60
    LONG_BREAK_MIN_IN_SECONDS = LONG_BREAK_MIN *60
    if(rep%8==0):
        count_down(LONG_BREAK_MIN_IN_SECONDS)
        header_label.config(text="Break",fg=RED)
    elif(rep%2==0):
        count_down(SHORT_BREAK_MIN_IN_SECONDS)
        header_label.config(text="Break",fg=PINK)
    else:
        count_down(WORK_MIN_IN_SECONDS)
        header_label.config(text="Work",fg=GREEN)


# ------------------------
# ---- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global rep
    print('count down handler called')
    minutes=count//60
    seconds=count%60
    canvas.itemconfig(timer_text,text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count - 1)
    else:
        # optionally trigger next session here:
        handle_start()


# ---------------------------- UI SETUP ------------------------------- #
window= tk.Tk()
# window.minsize(width=600, height=600)
window.config(padx=100,pady=100,bg=YELLOW)

window.title("Pomodoro app")

canvas= tk.Canvas(window,width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=tk.PhotoImage(file="./tomato.png")

canvas.create_image(100,100,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,'bold'),fill='white')

canvas.grid(row=1,column=1)


# header label
header_label= tk.Label(text='TIMER',font=(FONT_NAME,40,'bold'),bg=YELLOW,fg=GREEN)
header_label.grid(row=0,column=1)

#start button
start_button=tk.Button(text='start',font=(FONT_NAME,20,'italic'),bg=YELLOW,command=handle_start,borderwidth=0,highlightthickness=0)
start_button.grid(row=3,column=0)

# # tick label
# tick_label=tk.Label(text= '✅',font=(FONT_NAME,40,'bold'),bg=YELLOW)
# tick_label.grid(row=4,column=1)

# reset  button
reset_button=tk.Button(text='RESET',font=(FONT_NAME,20,'italic'),bg=YELLOW,command=handle_reset,borderwidth=0,highlightthickness=0)
reset_button.grid(row=3,column=2)



window.mainloop()