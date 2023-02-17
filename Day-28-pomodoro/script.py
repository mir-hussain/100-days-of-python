from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 48), bg=YELLOW)
label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


def countdown(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)


def start_timer():
    countdown(5)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=3, column=3)


check_label = Label(text="✓", fg=GREEN, font=(FONT_NAME, 24), bg=YELLOW)
check_label.grid(row=4, column=2)
window.mainloop()
