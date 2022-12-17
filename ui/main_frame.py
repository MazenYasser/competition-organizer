from tkinter import *
from some_other_frame import render
FONT = ('Verdana', 16)
root = Tk()
root.title('Competition Organizer')
message_label = Label(width=35, text='WELCOME TO COMPETITION ORGANIZER', font=FONT)
teams_button = Button(width=35, text='Teams', font=FONT, command=render)
league_button = Button(width=35, text='Create League', font=FONT, command=lambda i: i)
cup_button = Button(width=35, text='Create Cup', font=FONT, command=lambda i: i)
message_label.grid(row=0, column=0)
teams_button.grid(row=1, column=0)
league_button.grid(row=2, column=0)
cup_button.grid(row=3, column=0)
mainloop()
