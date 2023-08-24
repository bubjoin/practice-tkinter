import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("Text Box")
window.geometry("400x500+100+100")
window.resizable(False, False)
window.config(background='white')

text_box_yscrollbar = tkinter.Scrollbar(window, orient="vertical")

text_box=tkinter.Text(window, borderwidth=1, 
                      background='white', 
                      width=50, height=20,
                      relief="solid",
                      padx=5, pady=5,
                      spacing1=5,
                      yscrollcommand=text_box_yscrollbar.set)

text_box_yscrollbar.config(command=text_box.yview)
text_box_yscrollbar.place(x=380, y=20, height=372)

text_box.insert("end", "Hello, World!\n")
text_box.insert("end", "This is a text box\n")
text_box.tag_add("entire", "1.0", "end")
text_box.tag_config("entire", foreground="#333333", font=("calibri", 10, "bold"))
text_box.insert("end", "Yes! Yes! Yes! Yes! Yes! Yes! Yes! Yes! Yes! Yes! \n")
text_box.insert("end", "0123456789"*5)

text_box['state'] = 'disabled' # <-> 'normal'
text_box.place(x=20, y=20)

def put_str(event):
    text_box['state'] = 'normal'
    text_box.insert("end", str(input_box.get())+'\n')
    text_box['state'] = 'disabled'
    text_box.see("end")
    input_box.delete(0, "end")

input_box=tkinter.Entry(window, width=51, relief="solid",
                        font=("calibri", 10, "bold"),)
input_box.focus()
input_box.bind("<Return>", put_str)
input_box.place(x=20, y=420)

window.mainloop()