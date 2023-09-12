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
        self.title('Background Scroll')

        self.frame = tkinter.Frame(self, 
                              width=self.window_width, 
                              height=self.window_height, 
                              relief="flat", background="gray")
        self.frame.place(x=0, y=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=4)
        
        self.add_canvas()
        
        self.x = 0
        self.scroll_background()
        
        self.bind("<KeyPress>", self.get_key)
        # <Key>, <KeyRelease>, ... 

    def add_canvas(self):    
        self.canvas = tkinter.Canvas(self.frame, width=400, height=300,
                                     background="white", border=0,
                                     relief="flat")
        self.canvas.place(x=200, y=150)
        
        src_path = os.path.abspath(__file__)
        src_dir = os.path.dirname(src_path)
        img_path = os.path.join(src_dir, "background_image.png")
        # Don't use local variable to reference PhotoImage
        self.background_image = tkinter.PhotoImage(file=img_path)
        image_0 = self.canvas.create_image(202, 152, 
                           image=self.background_image)
        # practice canvas tag_bind
        self.canvas.tag_bind(image_0, "<Button-1>",
                             lambda event: self.canvas.delete(
                                    image_0))
        
    def scroll_background(self):
        
        self.x += 2
        if self.x == 400:
            self.x = 0
        self.canvas.delete("background_images")
        self.canvas.create_image(self.x - 202, 152, 
                                 image=self.background_image,
                                 tag="background_images")
        self.canvas.create_image(self.x + 197, 152, 
                                 image=self.background_image,
                                 tag="background_images")
        self.after(10, self.scroll_background)
        
        
    def get_key(self, event):
        key_symbol = event.keysym
        key_code = event.keycode
        print(key_symbol)
        print(key_code)
        

if __name__ == "__main__":
    tkinter_app = TkinterApp()
    tkinter_app.mainloop()