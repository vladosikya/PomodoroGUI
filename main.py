import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer_core = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, marks, timer_core
    window.after_cancel(timer_core)
    start_button.config(command=start_timer)

    marks = ""
    reps = 1
    canvas.itemconfig(timer, text="00:00")
    check_mark.config(text=marks)
    timer_label.config(text='Timer')

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, marks, timer_core

    start_button.config(command="")

    if reps <= 7 and reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)
    elif reps <=6 and reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        timer_label.config(text="Break", fg=PINK)
        countdown(LONG_BREAK_MIN * 60)

    check_mark.config(text=f"{marks}")
    if reps % 2 != 0:
        marks = f"{marks}" + "✔"
    reps+=1

    if reps > 8:
        reps = 1
        marks = ""

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer_core

    min = int(count / 60)
    sec = count % 60

    if min < 10:
        min_form = f"0{min}"
    else:
        min_form = min

    if sec < 10:
        sec_form = f"0{sec}"
    else:
        sec_form = sec

    canvas.itemconfig(timer, text=f"{min_form}:{sec_form}")

    if count > 0:
        timer_core = window.after(1000, countdown, count-1)

    if min == 0 and sec == 0:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(pady=50, padx=100, background=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)
timer_label = tkinter.Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)
check_mark = tkinter.Label(text=marks, bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

window.mainloop()