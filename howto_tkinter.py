import tkinter as tk
from tkinter import ttk # Tk Themed Widgets, newer than classic widgets
from tkinter.messagebox import showinfo

# Root Window Instance and Title
root = tk.Tk()
root.title('Digital Stopwatch 2023')

# Label to pack
ttk_label = ttk.Label(root, text = 'I am Themed Label')
ttk_label.pack()

# Geometry
# root.geometry('300x200+200+200')
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

print(root.geometry()) # why 1x1?

# Size
# root.resizable(0, 0)
root.minsize(300, 200)
root.maxsize(600, 400)

# Icon
root.iconbitmap('./top.ico')

# Attributes
root.attributes('-alpha', 0.8)
root.attributes('-topmost', 1)
# root.lower()
# root.lift()

# Button
def green_btn_clicked():
    showinfo(title="Info", message="You clicked the green button!")

btn_img = tk.PhotoImage(file="./btn_img.png")

green_btn = ttk.Button(
    root, 
    text="GREEN", 
    image=btn_img, 
    compound=tk.TOP,
    command=green_btn_clicked)
# parameter 'compound' to display image and text together(pos of img)

green_btn.pack(ipadx=1, ipady=2, expand=True)

exit_btn = ttk.Button(root, text="EXIT", command=lambda: root.quit())
exit_btn.pack(ipadx=10, ipady=10, expand=True)


# Root Window Mainloop
root.mainloop()