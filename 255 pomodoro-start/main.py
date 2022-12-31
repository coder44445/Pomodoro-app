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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timetext,text=f"00:00")
    tick.config(text=f"{'✓'*reps}")
    time.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timermech():
    global reps
    reps+=1
    WORK_sec = WORK_MIN *60
    SHORT_BREAK_sec = SHORT_BREAK_MIN * 60
    LONG_BREAK_sec = LONG_BREAK_MIN*60
    if reps%2!=0:
        time.config(text="Work",fg=GREEN)
        counter(WORK_sec)
    elif reps%2==0:
        if reps%8 != 0 :
            counter(SHORT_BREAK_sec)
            time.config(text="Short Break",fg=PINK)
    else:
        time.config(text="Long break",fg=RED)
        counter(LONG_BREAK_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(timecount):
    min = timecount//60
    sec = timecount%60
    if min < 10:
        min = f"{0}{min}"
    if sec < 10:
        min = f"{0}{sec}"
    canvas.itemconfig(timetext, text = f"{min}:{sec}")
    if timecount > 0:
        global timer
        timer = window.after(1000,counter,timecount-1)
    else:
        timermech()
        tick.config(text=f"{'✓'*reps}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
time = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,30,"bold"))
time.grid(row=0,column= 1)
tick  = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,30,"bold"))
tick.grid(column= 1,row= 2)
start = Button(text="Start",command=timermech)
start.grid(column=0,row=2)
resetbutton = Button(text="Reset",command=reset)
resetbutton.grid(column=2,row=2)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tamatoimg = PhotoImage(file="Enter your file path")
canvas.create_image(100,112,image = tamatoimg)
timetext = canvas.create_text(100,130,text=f"00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(column=1,row=1)
window.mainloop()
