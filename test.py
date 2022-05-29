from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from datetime import datetime
from threading import Timer
import time
import threading
from PIL import ImageTk, Image


# importing strftime function to 
# retrieve system's time 
from time import strftime 

# creating tkinter window 
root = Tk()
root.title('BG Hourglass Time Control')


# todo: draw hourglass or line animation
# todo: highlighting to show who's turn it is
# todo: add warning sound "play wav file - "5 seconds left" - "hurry hurry!"- "play song with building volume"
# todo: redo layout - make it look nice

# time is stored as seconds
start_time = 30
p1_time = start_time
p2_time = start_time

p1_name = "Len"
p2_name = "Chlore"

turn_timer = 0
turn_number = 0

on_turn = "p1"

delay = 5   # dice rolling delay
delay_time = 5



# draw clocks
p1_clock_lbl = Label(root, font = ('calibri', 90, 'bold'),
                     background = 'purple',
                     foreground = 'white')


p2_clock_lbl = Label(root, font = ('calibri', 90, 'bold'),
                     background = 'purple',
                     foreground = 'white')

p1_name_lbl = Label(root, font = ('calibri', 40, 'bold'),
                     background = 'purple',
                     foreground = 'white')

p2_name_lbl = Label(root, font = ('calibri', 40, 'bold'),
                     background = 'purple',
                     foreground = 'white')

p1_delay_lbl = Label(root, font = ('calibri', 40, 'bold'),
                     background = 'purple',
                     foreground = 'white')

p2_delay_lbl = Label(root, font = ('calibri', 40, 'bold'),
                     background = 'purple',
                     foreground = 'white')


p1_name_lbl.config(text = p1_name)
p2_name_lbl.config(text = p2_name)


# Pause Button
def pause_button_action(event=None):
    print('pause button pressed')
    global turn_number
    turn_number += 1

pause_button = Button(root, text ="Pause", command = pause_button_action)


# Reset Button
def reset_button_action():
    print('reset button pressed')
    # set clocks back to start values
    # kill any running threads
    global turn_number
    global p1_time
    global p2_time

    turn_number += 1

    p1_time = start_time
    p2_time = start_time
    pack_all()

reset_button = Button(root, text="Reset", command=reset_button_action)


# End Turn Button
def end_button_action(event=None):
    global turn_number
    global p1_time
    global p2_time
    global on_turn
    turn_number += 1
    # print('end button pressed, turn', turn_number)
    print('end button action: player on turn is', on_turn)
    print('event was', event)

    # swap the player on turn
    if on_turn == "p1":
        on_turn = "p2"
    else:
        on_turn = "p1"

    th = threading.Thread(target=cd, args=[turn_number])
    th.start()

# end_button = Button(root, text="End Turn", command=end_button_action)

root.bind("<space>", end_button_action)




def cd(this_turn):
    global p1_time
    global p2_time
    global p1_clock_lbl
    global p2_clock_lbl
    global delay
    global on_turn

    print('player on turn now is ', on_turn)

    delay = delay_time

    while p1_time > 0 and p2_time > 0:



        if this_turn != turn_number:
            # kill this thread
            # print('killing thread for turn', this_turn)
            break

        time.sleep(1)

        # print('adding time values for turn', this_turn)
        if on_turn == "p1":
            p1_name_lbl.config(font=('calibri', 40, 'bold', 'underline'), foreground = 'cyan')
            p2_name_lbl.config(font=('calibri', 30, 'bold'), foreground = 'white')

            if delay > 0:
                delay -= 1
                p1_delay_lbl.config(text=delay)
                p2_delay_lbl.config(text="")

            else:
                p1_time -= 1
                p2_time += 1
        else:
            p2_name_lbl.config(font=('calibri', 40, 'bold', 'underline'), foreground = 'cyan')
            p1_name_lbl.config(font=('calibri', 30, 'bold'), foreground = 'white')
            if delay > 0:
                delay -= 1
                p2_delay_lbl.config(text=delay)
                p1_delay_lbl.config(text="")
            else:
                p1_time += 1
                p2_time -= 1

        # colour the labels - red if short, green is long, white otherwise
        if p1_time <= 10:
            p1_clock_lbl.config(foreground = 'red')
            p2_clock_lbl.config(foreground= 'green')
        if p2_time <= 10:
            p2_clock_lbl.config(foreground='red')
            p1_clock_lbl.config(foreground='green')
        if p1_time > 10 and p2_time > 10:
            p1_clock_lbl.config(foreground='white')
            p2_clock_lbl.config(foreground='white')



        p1_clock_lbl.config(text=p1_time)
        p2_clock_lbl.config(text=p2_time)

        p1_delay_lbl.pack()
        p2_delay_lbl.pack()
        p1_clock_lbl.pack()
        p2_clock_lbl.pack()

    # print('now ending cd function for turn', this_turn)


def pack_all():
    # Placing clock at the centre
    # of the tkinter window
    p1_name_lbl.pack(padx=5, pady=15, side=LEFT)
    p2_name_lbl.pack(padx=5, pady=15, side=RIGHT)
    p1_clock_lbl.pack(padx=5, pady=15, side=LEFT)
    p2_clock_lbl.pack(padx=5, pady=15, side=RIGHT)
    p1_delay_lbl.pack(padx=5, pady=15, side=LEFT)
    p2_delay_lbl.pack(padx=5, pady=15, side=RIGHT)

    reset_button.pack(padx=30, pady=15, side=TOP)
    pause_button.pack(padx=30, pady=15, side=TOP)
    # end_button.pack(padx=30, pady=15, side=BOTTOM)

    p1_clock_lbl.config(text=p1_time)
    p2_clock_lbl.config(text=p2_time)



pack_all()

# time()

mainloop() 