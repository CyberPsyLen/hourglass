import time
from tkinter import *
import threading
root = Tk()


def cd(timer_label_obj,ts):
    while ts > 0:
        timer_label_obj.config(text=ts)
        ts-=1
        timer_label_obj.pack()
        time.sleep(1)
        if ts ==0:
            timer_label_obj.destroy()
            completeTimer = Label(timerFrame, text="Time is complete")
            completeTimer.pack()

def countdown(t):
    timer = Label(timerFrame)
    ts = int(t)
    th = threading.Thread(target=cd,args=[timer,ts])
    th.start()


timerFrame = LabelFrame(root, padx=50, pady=50, bd=0)


timerFrameText = Label(timerFrame,
    text="Enter time in seconds for countdown",
    font=("Arial", 20, "bold")
)
countdownBox= Entry(timerFrame, bd=3)


submitCountdown = Button(timerFrame,
    padx=5,
    pady=5,
    text="Submit",
    font=("Arial", 20),
    command= lambda:countdown(countdownBox.get())
   )




timerFrame.pack()


timerFrameText.pack()
countdownBox.pack()
submitCountdown.pack()


root.mainloop()