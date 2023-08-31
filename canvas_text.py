import tkinter
from tkinter import ttk
import time

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

def input_finished(event):
    canvas.itemconfig(text_2, text=input_box.get())
    input_box.delete(0, "end")

input_box=tkinter.Entry(window, width=51, 
                        relief="flat", borderwidth=0,
                        font=("calibri", 10, "bold"),)
input_box.focus()
input_box.bind("<Return>", input_finished)
input_box.place(x=30, y=380)    

window.mainloop()
