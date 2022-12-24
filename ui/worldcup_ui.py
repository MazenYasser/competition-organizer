from tkinter import *
from core.worldcup import Worldcup


def render_worldcup_window(worldcup):
    worldcup_window = Toplevel()
    worldcup_window.title('FIFA WORLD CUP')
    groups_frame = Frame(worldcup_window)

    worldcup.groups_draw()

    for i, group in enumerate(worldcup.groups):
        group_frame = create_group_frame(groups_frame, 'GROUP ' + chr(65+i), group.teams)
        group_frame.grid(row=0, column=i)

    groups_frame.grid(row=1, padx=0, columnspan=5)
    mainloop()


def create_group_frame(parent_frame, group_name, teams):
    group_frame = Frame(parent_frame)

    group_label = Label(group_frame, text=group_name)
    group_list = Listbox(group_frame)

    for team in teams:
        group_list.insert(END, team.name)

    group_label.grid(row=0, column=0)
    group_list.grid(row=1, column=0)
    return group_frame

