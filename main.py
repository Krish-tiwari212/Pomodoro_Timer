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
    global reps
    window.after_cancel(timer)
    reps = 0
    checkmark_label.config(text="✔" * (reps // 2))
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text = "00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown_mech(long_break_sec)
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
    elif reps % 2 == 0:
        countdown_mech(short_break_sec)
        checkmark_label.config(text="✔" * (reps//2))
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
    else:
        countdown_mech(work_sec)
        checkmark_label.config(text="✔" * (reps // 2))
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_mech(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    global timer
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown_mech, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)
checkmark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
checkmark_label.grid(column=1, row=3)



window.mainloop()