from tkinter import *
from core.league import *
from core.team import *
from ui.match_data_ui import show_league_teams_window
from ui.utils_ui import center_window


def render_scoreboard(league):
    league.generate_matches()
    header_font = ('arial', 18, 'bold')
    team_font = ('arial', 16)

    scoreboard_window = Tk()
    center_window(scoreboard_window, w=1115, h=600)
    scoreboard_window.title('Scoreboard')

    buttons_frame = Frame(scoreboard_window)
    buttons_frame.grid(row=0, column=0)
    next_button = Button(buttons_frame, text='Matches Info', command=lambda x=league: render_matches_window(x),
                         height=1, font=('arial', 18), borderwidth=2, relief=RAISED, bg='#2b2b2b', fg='#FFFFFF')
    next_button.grid(row=0, column=0, ipadx=355)

    scoreboard_frame = Frame(scoreboard_window)
    render_lines(header_font, league, scoreboard_window, team_font, scoreboard_frame)

    def update():
        render_lines(header_font, league, scoreboard_window, team_font, scoreboard_frame)
        league.update_scoreboard()
        scoreboard_window.after(1000, update)

    update()
    mainloop()


def render_lines(header_font, league, scoreboard_window, team_font, scoreboard_frame):
    scoreboard_frame.destroy()
    scoreboard_frame = Frame(scoreboard_window)
    scoreboard_frame.grid(row=1, column=0)
    headers = ['RANK', '          NAME          ', 'POINTS', 'GOALS SCORED', 'GOALS CONCEDED', 'WIN', 'LOSE', 'DRAW']
    for i, header in enumerate(headers):
        label = Label(scoreboard_frame, text=' ' + header + ' ', font=header_font, foreground='#FFFFFF',
                      background='#FF0000', borderwidth=0.5, relief="solid")
        label.grid(row=0, column=i)
    for i, team in enumerate(league.update_scoreboard()):
        for j, header in enumerate(headers):
            label = Label(scoreboard_frame, text=team[header.strip()], font=team_font)
            label.grid(row=i + 1, column=j)


def render_matches_window(league):
    show_league_teams_window(league)


def test_ui_scoreboard():
    t1 = Team()
    t1.set_name("zama")
    t1.point = 15
    t2 = Team()
    t2.set_name("Manchiseter United")
    t2.point = 20
    t3 = Team()
    t3.set_name("isma")
    t3.point = 10

    league = League()
    league.add_team(t1)
    league.add_team(t2)
    league.add_team(t3)
    render_scoreboard(league)

# test_ui_scoreboard()
