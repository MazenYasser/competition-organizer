from tkinter import *
from src.league import *
from src.team import *

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


header_font = ('Verdana', 14, 'bold')
team_font = ('Verdana', 12, 'bold')

root = Tk()
root.config(bg='#0F0F33')
root.geometry('800x600')
headers = ['RANK', 'NAME', 'POINTS', 'GOALS SCORED', 'GOALS CONCEDED', 'WIN', 'LOSE', 'DRAW']
for i, header in enumerate(headers):
    label = Label(text=header, font=header_font, foreground='#FFFFFF', background='#FF0000',
                  borderwidth=0.5, relief="solid")
    label.grid(row=0, column=i)

for i, team in enumerate(league.update_scoreboard()):
    for j, header in enumerate(headers):
        label = Label(text=team[header], font=team_font, foreground='#FFFFFF', bg='#0F0F33')
        label.grid(row=i+1, column=j)



mainloop()
