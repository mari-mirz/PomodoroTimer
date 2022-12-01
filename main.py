from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    titleLabel.config(text="Timer")
    canvas.itemconfig(timerText, text="00:00")
    sessionLabel.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 > 0:
        countdown(work_sec)
        titleLabel.config(text="Work")

    elif reps == 8:
        countdown(long_break_sec)
        titleLabel.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        titleLabel.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count, check=""):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    if 10 > int(seconds) > 0:
        seconds = f"0{seconds}"

    canvas.itemconfig(timerText, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check = ""

        work_sessions = math.floor(reps / 2)
        for rep in range(work_sessions):
            check += "✔"
            sessionLabel.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# image and text setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons and labels
titleLabel = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
titleLabel.grid(column=1, row=0)

startButton = Button(text="start", bg=YELLOW, command=start_timer)
startButton.grid(column=0, row=2)

resetButton = Button(text="reset", bg=YELLOW, command=reset_timer)
resetButton.grid(column=2, row=2)

sessionLabel = Label(text="", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
sessionLabel.grid(column=1, row=3)

window.mainloop()
