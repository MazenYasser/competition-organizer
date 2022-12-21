from tkinter import *


def render():
    FONT = ('Verdana', 16)
    new_window = Toplevel()
    new_window.title('Competition Organizer')
    message_label = Label(new_window,width=35, text='OTHER FRAME TEST', font=FONT)
    message_label.grid(row=0, column=0)
    mainloop()



