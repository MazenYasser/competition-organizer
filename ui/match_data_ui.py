import re
from tkinter import *
from tkinter import messagebox

from core.team import Team
from core.league import League


def result_check(result):
    """
    This function matches the user submitted result to the regex and returns true if it matches the regex
    and false otherwise
    :param result: str  format --> HomeGoals-AwayGoals
    :return: (TRUE) on regex match
    This flag is to be used later in the function to display an error message
    """
    result_format = re.compile('[0-9]+-[0-9]+')
    if result_format.match(result) is not None:
        return True
    else:
        messagebox.showerror("Format error", "Please enter the match result in the correct format!")
        return False


def show_matches(competition, team):
    """
    Takes team name and displays a window that has a listbox containing the team's matches
    :param competition:
    :param team: str
    :return:
    """
    # Initializing the UI
    team_matches_window = Toplevel()
    matches_frame = Frame(team_matches_window)
    matches_scroll = Scrollbar(matches_frame, orient=VERTICAL)
    team_matches_box = Listbox(matches_frame, yscrollcommand=matches_scroll.set)
    lbl = Label(team_matches_window, text='{} matches'.format(team))
    matches_scroll.config(command=team_matches_box.yview)

    btn_add_result = Button(team_matches_window, height=1, text='ADD RESULT',
                            command=lambda x=0: match_result(competition, team_matches_box.get(ANCHOR)))

    # Finding the team's matches in the league matches list and adding them to their own matches listbox
    all_matches = competition.matches
    current_team_matches = list()
    for i in range(len(all_matches)):
        if all_matches[i].home_team.name == team or all_matches[i].away_team.name == team:
            current_team_matches.append(all_matches[i])
            team_matches_box.insert(i, all_matches[i])
    
    # Packing things
    lbl.pack()
    matches_frame.pack()
    matches_scroll.pack(side=RIGHT, fill=Y)
    team_matches_box.pack()
    btn_add_result.pack()


def match_result(competition, teams):
    """
    This function takes the mentioned string, and configures the results as specified by the user in the entry widget
    Note: The basis is that the match's Home team and Away team are unique,
     meaning that no other match will have the same Home team and away team
    :param competition:
    :param teams: str {Note: the string is in the format: 'Home goals-Away goals'}
    :return:
    """
    # Initializing the UI
    match_data_window= Toplevel()
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

    # Finding the match and setting the button to update the result of that match, then close the window
    for match in competition.matches:
        if match.home_team.name == current_teams[0] and match.away_team.name == current_teams[1]:
            # Note: To make a lambda function perform multiple functions sequentially,
            # wrap the functions in a list in the body of the lambda function
            # If result_check flag is True, the result is submitted. If result_check flag is False, ...
            # the function displays an error message,
            # clears the text field and discards the result that was submitted in the wrong format
            btn_submit_result.configure(
                command=lambda: [match.set_result(int(txt_result.get()[0]),
                                                  int(txt_result.get()[2])),
                                 competition.update_scoreboard(),
                                 match_data_window.destroy()] if result_check(txt_result.get()) else
                txt_result.delete(0, END))
            break
    # To see current match info in the console before and after submitting it
    # Uses __call__() function
        print(match())


def show_league_teams_window(competition):

    league_teams = Toplevel()
    lbl_league = Label(league_teams, text="League teams")
    listbox_frame = Frame(league_teams)
    league_scroll = Scrollbar(listbox_frame, orient=VERTICAL)
    league = Listbox(listbox_frame, yscrollcommand=league_scroll.set)

    league_scroll.config(command=league.yview)
    btn_show_matches = Button(league_teams, text='Show Matches', height=1,
                              command=lambda x=0: show_matches(competition, league.get(ANCHOR)))

    lbl_league.pack()

    listbox_frame.pack()
    league_scroll.pack(side=RIGHT, fill=Y)
    league.pack()
 
    btn_show_matches.pack()
    for team in competition.teams:
        league.insert(END, team.name)
    # competition.generate_matches()   # TO BE REFACTORED
    mainloop()

# If you want to test the code, run this function


def test_code():
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
    show_league_teams_window(league)
