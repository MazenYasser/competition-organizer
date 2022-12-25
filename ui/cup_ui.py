import sys
import re
from tkinter import *
from tkinter import messagebox
from core.team import Team
from core.cup import Cup

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
    cup.generate_next_round()
    if not cup.isFinished:
        render_next_group(cup)
    else:
        messagebox.showinfo("Cup Completed", f"Winner is: {cup.get_winner().name}")
        sys.exit(0)


def result_check(result: str):
    """
    name result_check(result) , arguments: result: string in the format --> HomeGoals-AwayGoals
    Description: This function matches the user submitted result to the regex and returns true if it matches
    the regex and false otherwise
    This flag is to be used later in the function to display an error message
    :param result: str
    :return:
    """
    result_format = re.compile('[0-9]+-[0-9]+')
    if result_format.match(result) is not None:
        if result[0] != result[2]:
            return True
    else:
        messagebox.showerror("Format error", "Please enter the match result in the correct format!")
        return False


def show_matches(competition: Cup, team):
    """
    Function documentation:
    name: show_matches(team) , arguments: team : str
    Description: Takes team name and displays a window that has a listbox containing the team's matches
    :param competition: Cup
    :param team: str
    :return:
    """
    # Initializing UI
    team_matches_window = Toplevel()
    matches_frame = Frame(team_matches_window)
    matches_scroll = Scrollbar(matches_frame, orient=VERTICAL)
    team_matches_box = Listbox(matches_frame, yscrollcommand=matches_scroll.set)
    lbl = Label(team_matches_window, text='{} matches'.format(team))
    matches_scroll.config(command=team_matches_box.yview)
    btn_add_result = Button(team_matches_window, height=1, text='Add Result',
                            command=lambda x=0: match_result(competition, team_matches_box.get(ANCHOR)))

    # Packing things
    lbl.pack()
    matches_frame.pack()
    matches_scroll.pack(side=RIGHT, fill=Y)
    team_matches_box.pack()
    btn_add_result.pack()

    # Finding the team's matches in the league matches list and adding them to their own matches listbox
    current_round_matches = competition.rounds[-1]['matches']
    for i in range(len(current_round_matches)):
        if current_round_matches[i].home_team.name == team or current_round_matches[i].away_team.name == team:
            team_matches_box.insert(i, current_round_matches[i])


def match_result(competition: Cup, teams):
    """
    Function documentation
    name: match_result(team)
    Description: This function takes the mentioned string,
    and configures the results as specified by the user in the entry widget
    Note: The basis is that the match's Home team and Away team are unique,
    meaning that no other match will have the same Home team and away team
    :param competition: Cup
    :param teams: str
    str {Note: the string is in the format: 'Home goals-Away goals'}
    :return:
    """
    # Initializing the UI
    match_data_window = Toplevel()
    result_frame = Frame(match_data_window)
    lbl_result = Label(result_frame, text='Result (Home-Away): ')
    txt_result = Entry(result_frame, bd=3)  # HomeGoals-AwayGoals

    btn_submit_result = Button(match_data_window, height=1, text='Submit')

    # Packing things up
    result_frame.grid(row=0)
    btn_submit_result.grid(row=1, padx=15)
    lbl_result.grid(row=0, column=0)
    txt_result.grid(row=0, column=1)

    # Extracting team names from the string
    current_teams = teams.split('-')

    current_round_matches = competition.rounds[-1]['matches']

    # Finding the match and setting the button to update the result of that match, then close the window
    for match in current_round_matches:
        if match.home_team.name == current_teams[0] and match.away_team.name == current_teams[1]:
            # Note: To make a lambda function perform multiple functions sequentially,
            # wrap the functions in a list in the body of the lambda function
            # If result_check flag is True, the result is submitted. If result_check flag is False, ...
            # the function displays an error message, clears the text field and discards the result
            # that was submitted in the wrong format
            btn_submit_result.configure(
                command=lambda:
                [match.set_result(int(txt_result.get()[0]),
                                  int(txt_result.get()[2])),
                 match_data_window.destroy()] if result_check(txt_result.get()) else txt_result.delete(0, END)
            )
            break
    # To see current match info in the console before and after submitting it
    # Uses __call__() function
        print(match())


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
    for i in range(int(len(team_names) / 1)):
        current = Team(name=team_names[i], strength=i * 2)
        cup.add_team(current)

    show_cup_matches_window(cup)


# test_code()
