# In Python, because of GIL,
# Thread cannot give you a performance upgrade,
# but it still gives you a background music!

# Threads are players who can play something simultaneously
# (it looks simultaneous)
# The first player can play background music
# The second player can play an effect sound
# ...
# Process is a place where players can live
# (or a player can live)
# 
# Asynchronous means making a player do diffrent things continuously
# without taking a rest while a thing is not completed

import tkinter
from tkinter import ttk
import time

# pip install playsound==1.2.2
from playsound import playsound

import threading

import multiprocessing

# play 2 in named "play 2" Thread, play 2 will end when main program ends
def play_sound():
    playsound("bgm.mp3", block=True) # because the block set true

# play 3 repeat in Thread-1, Thread-2, ..., it will need a process to end
cnt_p2_thread = 0
def repeat_sound():
    global cnt_p2_thread
    cnt_p2_thread += 1
    playsound("bgm.mp3", block=False)
    threading.Timer(42, repeat_sound).start() # repeat every 42 seconds
    for th in threading.enumerate():
        print(th.name)
    print(cnt_p2_thread)

# for play 3 repeat, 
# the sound need end function to end when gui program ends    
def end_program():
    window.destroy()
    bgm_repeat.terminate()

def input_finished(event):
    canvas.itemconfig(text_2, text=input_box.get())
    input_box.delete(0, "end")

if __name__=="__main__":
    for th in threading.enumerate():
        print(th.name)
    
    # play 1 in MainThread, play 1 will end when MainThread ends
    playsound("bgm.mp3", block=False)
    time.sleep(0.1)
    
    # play 2
    bgm = threading.Thread(target=play_sound, daemon=True, name="play 2")
    bgm.start()
    
    # play 3 repeat, process needs to be in __main__ block to end properly
    # using process to end alive thread
    bgm_repeat = multiprocessing.Process(target=repeat_sound)
    bgm_repeat.start()
    
    window=tkinter.Tk()
    window.title("Canvas Box")
    window.geometry("420x460+100+100")
    window.resizable(False, False)
    window.config(background='white')
    
    canvas = tkinter.Canvas(window, width=400, height=400, background='white')
    canvas.place(x=8, y= 10)
    
    # a transparent text box, anchor default center
    text_1 = canvas.create_text(200, 200, text="Orange", fill="orange", 
                                font=("Comfortaa", 20, "bold"),
                                anchor="center")
    
    canvas.after(1000, canvas.itemconfig, text_1, {"text":"Ubuntu"})
    canvas.after(2000, canvas.itemconfig, text_1, {"text":"Great!"})
    
    text_2 = canvas.create_text(200, 240, text="", fill="silver",
                                font=("Comfortaa", 20, "bold"),
                                anchor="center")
    
    input_box=tkinter.Entry(window, width=51, 
                            relief="flat", borderwidth=0,
                            font=("calibri", 10, "bold"),)
    input_box.focus()
    input_box.bind("<Return>", input_finished)
    input_box.place(x=30, y=380)    
    
    # process having repeat thread terminate in end program function
    window.protocol("WM_DELETE_WINDOW", end_program)
    
    window.mainloop()
    