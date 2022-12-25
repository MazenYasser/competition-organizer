from tkinter import *
from tkinter.messagebox import showerror

from ui.cup_ui import show_cup_matches_window
from ui.scoreboard_ui import render_scoreboard


def render_16_stage(worldcup):
    if worldcup.is_simulation:
        worldcup.simulate_groups_results()
    if not worldcup.groups_stage_completed():
        showerror(title="Add Error", message="GROUP STAGE NOT YET DONE")
        return
    worldcup.round_16.teams = worldcup.get_16_stage_teams()
    show_cup_matches_window(worldcup.round_16)


def render_worldcup_window(worldcup):
    worldcup_window = Toplevel()
    worldcup_window.title('FIFA WORLD CUP')
    worldcup_window.iconbitmap('icon.ico')
    worldcup_window.resizable(False, False)
    groups_frame = Frame(worldcup_window)

    for i, group in enumerate(worldcup.groups):
        group_frame = create_group_frame(groups_frame, "GROUP " + chr(65 + i), group.teams, group)
        group_frame.grid(row=0, column=i)

    groups_frame.grid(row=1, padx=0, columnspan=5)

    btn_go_to_16 = Button(worldcup_window, text='GO TO 16 STAGE', height=1,
                          command=lambda x=worldcup: render_16_stage(x))

    btn_go_to_16.grid(row=2, padx=0, columnspan=5, rowspan=2)

    mainloop()


def create_group_frame(parent_frame, label_text, teams, league):
    group_frame = Frame(parent_frame)

    group_label = Label(group_frame, text=label_text)
    group_list = Listbox(group_frame)

    for team in teams:
        group_list.insert(END, team.name)

    btn_go_to_group = Button(group_frame, text='GO TO ' + label_text, height=1,
                             command=lambda x=league: render_scoreboard(x))

    group_label.grid(row=0, column=0)
    group_list.grid(row=1, column=0)
    btn_go_to_group.grid(row=2, column=0)
    return group_frame
