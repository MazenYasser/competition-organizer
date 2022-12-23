from tkinter import *
from some_other_frame import render
from src.league import League
from src.cup import Cup
from ui.ui_team import TeamGUI

FONT = ('', 16)


def create_league():
    league = League()
    team_ui = TeamGUI(competition=league)


def create_cup():
    cup = Cup()
    team_ui = TeamGUI(competition=cup)

if __name__ == '__main__':
    root = Tk()

    root.title('Competition Organizer')

    welcome_label = Label(width=35, text='WELCOME TO COMPETITION ORGANIZER', font=FONT)

    league_button = Button(width=35, text='Create League', font=FONT, command=create_league)
    cup_button = Button(width=35, text='Create Cup', font=FONT, command=create_cup)
    world_cup_button = Button(width=35, text='Create World Cup', font=FONT, command=render)

    welcome_label.grid(row=0, column=0)

    league_button.grid(row=1, column=0)
    cup_button.grid(row=2, column=0)
    world_cup_button.grid(row=3, column=0)

    mainloop()
