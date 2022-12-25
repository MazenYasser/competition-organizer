from tkinter import *
from PIL import Image, ImageTk
from core.league import League
from core.cup import Cup
from core.worldcup import Worldcup

from ui.team_ui import TeamGUI
from ui.utils_ui import center_window

FONT = ('arial', 16)
FONT_WELCOME = ('arial', 20, 'bold')


def create_league():
    league = League()
    TeamGUI(competition=league)


def create_cup():
    cup = Cup()
    TeamGUI(competition=cup)


def create_worldcup():
    worldcup = Worldcup()
    TeamGUI(competition=worldcup)


if __name__ == '__main__':
    root = Tk()

    center_window(root)

    root.title('Competition Organizer')

    welcome_label = Label(width=24, text='Welcome To \nCompetition Organizer', font=FONT_WELCOME)

    logo = Image.open('logo.png')
    logo = ImageTk.PhotoImage(logo)

    logo_label = Label(image=logo)
    logo_label.image = logo

    button_frame = Frame(root)

    league_button = Button(button_frame, width=35, text='Create League', font=FONT, command=create_league)
    cup_button = Button(button_frame, width=35, text='Create Cup', font=FONT, command=create_cup)
    world_cup_button = Button(button_frame, width=35, text='Create FIFA World Cup', font=FONT, command=create_worldcup)

    league_button.grid(row=0, column=0)
    cup_button.grid(row=1, column=0)
    world_cup_button.grid(row=2, column=0)

    welcome_label.grid(row=0, column=0)
    logo_label.grid(row=1, column=0)
    button_frame.grid(row=2, column=0)

    mainloop()
