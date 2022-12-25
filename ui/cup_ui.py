import sys
from tkinter import *
from tkinter import messagebox
from core.team import Team
from core.cup import Cup
from ui.match_data_ui import show_matches

CURRENT_LIST = 0
GROUP_LISTBOX_LIST = []
GROUP_FRAME_LIST = []


def render_next_group(cup: Cup):
    global CURRENT_LIST
    global GROUP_LISTBOX_LIST

    for i in range(len(cup.rounds)):
        GROUP_LISTBOX_LIST[i].delete(0, END)
        for team in cup.rounds[i]['teams']:
            GROUP_LISTBOX_LIST[i].insert(END, team.name)
        CURRENT_LIST = i


def to_next_round(cup: Cup):
    if not cup.generate_next_round():
        messagebox.showerror(title='Error', message='All matches in the last round must be played')
    if not cup.isFinished:
        render_next_group(cup)
    else:
        messagebox.showinfo("Cup Completed", f"Winner is: {cup.get_winner().name}")
        sys.exit(0)


def create_group_frame(parent_frame, label_text):
    group_frame = Frame(parent_frame)

    group_label = Label(group_frame, text=label_text)
    group_list = Listbox(group_frame)

    group_label.grid(row=0, column=0)
    group_list.grid(row=1, column=0)
    return group_frame, group_list


def show_cup_matches_window(cup: Cup):
    """
    name: show_cup_matches_window(cup)
    Description: This is the main function that initializes the window
    :param cup: Cup
    :return:
    """
    # Initializing UI
    cup.start_cup()
    cup_window = Toplevel()
    cup_window.iconbitmap('icon.ico')
    cup_window.resizable(False, False)
    cup_window.title('CUP')
    groups_frame = Frame(cup_window)
    buttons_frame = Frame(cup_window)
    global GROUP_LISTBOX_LIST
    global GROUP_FRAME_LIST
    GROUP_LISTBOX_LIST = []
    stages = [32, 16, 8, 4, 2]
    for i, stage in enumerate(stages):
        if stage <= len(cup.teams):
            group_frame, group_list = create_group_frame(groups_frame, "STAGE " + str(stage))
            group_frame.grid(row=0, column=i)
            GROUP_LISTBOX_LIST.append(group_list)
            GROUP_FRAME_LIST.append(group_frame)

    # Adding the first group to its appropriate listbox
    render_next_group(cup)

    btn_show_matches = Button(buttons_frame, text='Show Matches', height=1,
                              command=lambda x=0: show_matches(cup, GROUP_LISTBOX_LIST[CURRENT_LIST].get(ANCHOR)))
    btn_next_round = Button(buttons_frame, text='To next round', height=1, command=lambda x=0: to_next_round(cup))

    btn_show_matches.grid(row=0, column=0, padx=(5, 50))
    btn_next_round.grid(row=0, column=1)

    groups_frame.grid(row=0, padx=0, columnspan=5)
    buttons_frame.grid(row=1, columnspan=5)
    mainloop()


# If you want to test the code, run this function
def test_code():
    team_names = [f'Team {i}' for i in range(1, 33)]

    cup = Cup()
    for i in range(int(len(team_names) / 16)):
        current = Team(name=team_names[i], strength=i * 2)
        cup.add_team(current)

    show_cup_matches_window(cup)


# test_code()
