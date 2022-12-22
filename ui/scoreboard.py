from tkinter import *
from src.league import *
from src.team import *
from ui.match_data_ui import show_league_teams_window


def render_scoreboard(league):
    header_font = ('Verdana', 14, 'bold')
    team_font = ('Verdana', 12, 'bold')

    scoreboard_window = Toplevel()
    scoreboard_window.config(bg='#0F0F33')
    scoreboard_window.geometry('800x600')
    headers = ['RANK', 'NAME', 'POINTS', 'GOALS SCORED', 'GOALS CONCEDED', 'WIN', 'LOSE', 'DRAW']
    for i, header in enumerate(headers):
        label = Label(scoreboard_window, text=header, font=header_font, foreground='#FFFFFF', background='#FF0000',
                      borderwidth=0.5, relief="solid")
        label.grid(row=0, column=i)

    for i, team in enumerate(league.update_scoreboard()):
        for j, header in enumerate(headers):
            label = Label(scoreboard_window, text=team[header], font=team_font, foreground='#FFFFFF', bg='#0F0F33')
            label.grid(row=i+1, column=j)
    next_button = Button(scoreboard_window, text='next', command=lambda x=league: render_matches_window(x))
    next_button.grid(row=10, column=5)
    mainloop()


def render_matches_window(league):
    show_league_teams_window(league)


def test_ui_scoreboard():
    t1 = Team()
    t1.set_name("zama")
    t1.point = 15
    t2 = Team()
    t2.set_name("ahly")
    t2.point = 20
    t3 = Team()
    t3.set_name("isma")
    t3.point = 10

    league = League()
    league.add_team(t1)
    league.add_team(t2)
    league.add_team(t3)
    render_scoreboard(league)
