import tkinter
from tkinter import ttk
import time
import platform
import os

class TkinterApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.window_width = 800
        self.window_height = 600
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_pos_x = int(self.screen_width/3 - self.window_width/2)
        self.window_pos_y = int(self.screen_height/3 - self.window_height/2)
        self.new_geo = f"{self.window_width}x{self.window_height}\
+{self.window_pos_x}+{self.window_pos_y}"
        self.geometry(self.new_geo)
        self.resizable(False, False)
        self.config(bg='white')
        self.title('KEY INPUT')

        self.frame = tkinter.Frame(self, 
                              width=self.window_width, 
                              height=self.window_height, 
                              relief="flat", background="white")
        self.frame.place(x=0, y=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=4)
        
        self.add_widgets()
        
        self.bind("<KeyPress>", self.get_key)
        # <Key>, <KeyRelease>, ... 

    def add_widgets(self):
        self.canvas = tkinter.Canvas(self.frame)
        self.canvas.config()
        self.canvas.grid(row=0, column=0)
        
        self.label = tkinter.Label(self.frame, text="Label", font="Comfortaa")
        self.label.grid(row=0, column=1)
        
        self.button = tkinter.Button(self.frame, text="Button", 
                                     font="comfortaa")
        self.button.grid(row=1, column=0)
        
        self.entry = tkinter.Entry(self.frame)
        self.entry.grid(row=1, column=1)
        
        self.text = tkinter.Text(self.frame)
        self.text.grid(row=2, column=0)
        
        self.check = tkinter.Checkbutton(self.frame, text="Check Button")
        self.check.grid(row=2, column=1)
        
    def get_key(self, event):
        key_symbol = event.keysym
        key_code = event.keycode
        self.text.insert("end", str(key_code)+'\n')
        self.label["text"] = str(key_symbol)
        

if __name__ == "__main__":
    tkinter_app = TkinterApp()
    tkinter_app.mainloop()