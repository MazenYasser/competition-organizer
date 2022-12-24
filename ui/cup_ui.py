import sys
sys.path.append('D:\Engineering\Fourth Year\Python\Tournament Organizer Project\Competation_Organizer')
from tkinter import *
from tkinter import messagebox
from core.team import Team
from core.match import Match
from core.league import League
from core.competition import Competition
from core.cup import Cup
import re

def render_next_group(cup: Cup):
    global current_list
    global groups_list

    for i in range(len(cup.rounds)):
        groups_list[i].delete(0,END)
        for team in cup.rounds[i]['teams']:
            groups_list[i].insert(END, team.name)
        current_list = i


def to_next_round(cup: Cup):
    # round_matches=competition.rounds[0].get('matches')
    # round_winners=list()
    # for match in round_matches:
    #     if match.result == 'Home Win':
    #         round_winners.append(match.home_team)
    #     elif match.result == 'Away Win':
    #         round_winners.append(match.away_team)
    cup.generate_next_round()
    if (cup.isFinished == False):
        render_next_group(cup)
    else:
        messagebox.showinfo("Cup Completed", f"Winner is: {cup.get_winner().name}")
        sys.exit(0)

# Function documentation:
# name result_check(result) , arguments: result: string in the format --> HomeGoals-AwayGoals
# Description: This function matches the user submitted result to the regex and returns true if it matches
# the regex and false otherwise
# This flag is to be used later in the function to display an error message
def result_check(result : str):
    result_format= re.compile('[0-9]+-[0-9]+')
    if(result_format.match(result)!= None):
        if(result[0] != result[2]):
            return True
    else:
        messagebox.showerror("Format error","Please enter the match result in the correct format!")
        return False
            
# Function documentation:
# name: show_matches(team) , arguments: team : str
# Description: Takes team name and displays a window that has a listbox containing the team's matches

def show_matches(competition: Cup,team):
    #Intializing UI
    
    team_matches_window= Toplevel()
    matches_frame= Frame(team_matches_window)
    matches_scroll= Scrollbar(matches_frame, orient=VERTICAL)
    team_matches_box= Listbox(matches_frame, yscrollcommand=matches_scroll.set)
    lbl= Label(team_matches_window,text='{} matches'.format(team))
    matches_scroll.config(command=team_matches_box.yview)
    btn_add_result= Button(team_matches_window,height=1, text='Add Result', command= lambda x=0: match_result(competition,team_matches_box.get(ANCHOR)))
    

    #Packing things
    lbl.pack()
    matches_frame.pack()
    matches_scroll.pack(side=RIGHT, fill=Y)
    team_matches_box.pack()
    btn_add_result.pack()

    #Finding the team's matches in the league matches list and adding them to their own matches listbox
    current_round_matches= competition.rounds[-1]['matches']
    for i in range(len(current_round_matches)):
        if (current_round_matches[i].home_team.name == team or current_round_matches[i].away_team.name == team):
            team_matches_box.insert(i, current_round_matches[i])
    
  
# Function documentation
# name: match_result(team), arguments: teams: str {Note: the string is in the format: 'Home goals-Away goals'}
# Description: This function takes the mentioned string, and configures the results as specified by the user in the entry widget 
# Note: The basis is that the match's Home team and Away team are unique, meaning that no other match will have the same Home team and away team

def match_result(competition: Cup,teams):
    #Initializing the UI
    match_data_window= Toplevel()
    result_frame= Frame(match_data_window)
    lbl_result= Label(result_frame, text='Result (Home-Away): ')
    txt_result= Entry(result_frame, bd=3) # HomeGoals-AwayGoals
    

    btn_submit_result= Button(match_data_window, height=1, text='Submit')

    #Packing things up
    result_frame.grid(row=0)
    btn_submit_result.grid(row=1, padx=15)
    lbl_result.grid(row=0,column=0)
    txt_result.grid(row=0, column=1)

    #Extracting team names from the string
    current_teams= teams.split('-')

    current_round_matches= competition.rounds[-1]['matches']

    #Finding the match and setting the button to update the result of that match, then close the window
    for match in current_round_matches:
        if (match.home_team.name == current_teams[0] and match.away_team.name == current_teams[1]):
            #Note: To make a lambda function perform multiple functions sequentially, wrap the functions in a list in the body of the lambda function
            # If result_check flag is True, the result is submitted. If result_check flag is False, ...
            # the function displays an error message, clears the text field and discards the result that was submitted in the wrong format
            btn_submit_result.configure(command= lambda : [match.set_result(int(txt_result.get()[0]), int(txt_result.get()[2])), match_data_window.destroy()]
            if result_check(txt_result.get()) == True else txt_result.delete(0,END))
            break
    #To see current match info in the console before and after submitting it
    #Uses __call__() function
    print(match())

# Function documentation:
# name: show_cup_matches_window(cup)    arguments: cup: Cup
# Description: This is the main function that initializes the window
def show_cup_matches_window(cup: Cup):

    #Initializing UI
    cup.start_cup()
    league_teams=Tk()
    groups_frame= Frame(league_teams)
    buttons_frame= Frame(league_teams)
    lbls_frame= Frame(league_teams)

    lbl_32= Label(lbls_frame,text="Group 32")
    lbl_16= Label(lbls_frame,text="Group 16")
    lbl_8= Label(lbls_frame,text="Group 8")
    lbl_4= Label(lbls_frame,text="Group 4")
    lbl_2= Label(lbls_frame,text="Group 2")

    lbl_32.grid(row=0,column=0,padx=(20,70))
    lbl_16.grid(row=0,column=1,padx=(0,70))
    lbl_8.grid(row=0,column=2, padx=(0,70))
    lbl_4.grid(row=0,column=3, padx=(10,70))
    lbl_2.grid(row=0,column=4, padx=(0,10))


    group_32= Listbox(groups_frame)
    group_16= Listbox(groups_frame)
    group_8= Listbox(groups_frame)
    group_4= Listbox(groups_frame)
    group_2= Listbox(groups_frame)

    group_32.grid(row=0, column=0)
    group_16.grid(row=0, column=1)
    group_8.grid(row=0, column=2)
    group_4.grid(row=0, column=3)
    group_2.grid(row=0, column=4)


    #This list is used to track the round progress and exclude unneeded listboxes from rendering on the window
    global groups_list
    groups_list=[group_32,group_16,group_8,group_4,group_2]
    #lbls_list=[lbl_32,lbl_16,lbl_8,lbl_4,lbl_2]

    #This stops the rendering of unnecessary listboxes and labels according to teams count
    if(len(cup.teams) == 32):
        pass
    elif(len(cup.teams) == 16):
        groups_list.remove(group_32)
        group_32.grid_remove()
        lbl_32.grid_remove()

    elif(len(cup.teams) == 8):
        groups_list.remove(group_32)
        group_32.grid_remove()
        lbl_32.grid_remove()

        groups_list.remove(group_16)
        group_16.grid_remove()
        lbl_16.grid_remove()

    elif(len(cup.teams) == 4):
        groups_list.remove(group_32)
        group_32.grid_remove()
        lbl_32.grid_remove()

        groups_list.remove(group_16)
        group_16.grid_remove()
        lbl_16.grid_remove()

        groups_list.remove(group_8)
        group_8.grid_remove()
        lbl_8.grid_remove()

    elif(len(cup.teams) == 2):
        groups_list.remove(group_32)
        group_32.grid_remove()
        lbl_32.grid_remove()

        groups_list.remove(group_16)
        group_16.grid_remove()
        lbl_16.grid_remove()

        groups_list.remove(group_8)
        group_8.grid_remove()
        lbl_8.grid_remove()

        groups_list.remove(group_4)
        group_4.grid_remove()
        lbl_4.grid_remove()
    
    #Adding the first group to its appropriate listbox
    render_next_group(cup)

    btn_show_matches= Button(buttons_frame, text='Show Matches',height=1, command= lambda x=0 : show_matches(cup,groups_list[current_list].get(ANCHOR)))
    btn_next_round= Button(buttons_frame, text='To next round',height=1, command= lambda x=0 : to_next_round(cup))
    
    #Placing things on the window
    lbls_frame.grid(row=0,pady=5, columnspan=5)
    groups_frame.grid(row=1,padx=0, columnspan=5)
    btn_show_matches.grid(row=0,column=0, padx=(5,50))
    btn_next_round.grid(row=0,column=1)
    buttons_frame.grid(row=2, columnspan=5)
    mainloop()

#If you want to test the code, run this function
def test_code():
    team_names=[f'Team {i}' for i in range(1,33)]

    cup = Cup()
    for i in range(int(len(team_names)/1)):
        current= Team(name=team_names[i],strength=i*2)
        cup.add_team(current)

    show_cup_matches_window(cup)

# test_code()

#Dumped code (To be removed)
# listbox_frame.grid()
# lbl_32.grid(row=0,column=0)
# group_32.grid(row=1, column=0)
# league_scroll.grid(row=1, fill=Y)
# btn_show_matches.grid(row=2, column=0)

# league_teams.geometry("800x600")
#---------------------------------
# To be removed
# lbls_frame=Frame(league_teams, border=15, borderwidth=10, bg='red')
# lbl_32= Label(lbls_frame,text="Group 32")
# lbl_16= Label(lbls_frame,text="Group 16")
# lbl_8= Label(lbls_frame,text="Group 8")
# lbl_4= Label(lbls_frame,text="Group 4")
# lbl_2= Label(lbls_frame,text="Group 2")
#--------------------------------
# lbl_16= Label(league_teams,text="Group 16")
# lbl_8= Label(league_teams,text="Group 8")
# lbl_4= Label(league_teams,text="Group 4")
# lbl_2= Label(league_teams,text="Group 2")

#----------------------------------------------------------------
#To be removed
# groups_frame= Frame(league_teams, border=15, borderwidth=10, bg='black')
# group_32= Listbox(groups_frame)
# group_16= Listbox(groups_frame)
# group_8= Listbox(groups_frame)
# group_4= Listbox(groups_frame)
# group_2= Listbox(groups_frame)
#----------------------------------------------------------------
# group_16= Listbox(league_teams)
# group_8= Listbox(league_teams)
# group_4= Listbox(league_teams)
# group_2= Listbox(league_teams)
#----------------------------------------------------------------
# To be removed
# group_16.bind("<<ListboxSelect>>", func=lambda x=0: show_matches(group_32.get(group_32.curselection())))
# group_8.bind("<<ListboxSelect>>", func=lambda x=0: show_matches(group_32.get(group_32.curselection())))
# group_4.bind("<<ListboxSelect>>", func=lambda x=0: show_matches(group_32.get(group_32.curselection())))
# group_2.bind("<<ListboxSelect>>", func=lambda x=0: show_matches(group_32.get(group_32.curselection())))
#-----------------------------------------------------------------

#----------------------------------------------------------------
# To be removed
# lbls_frame.grid(row=0, column=0, columnspan=10)
# lbl_16.grid(row=0,column=1)
# lbl_8.grid(row=0,column=2)
# lbl_4.grid(row=0,column=3)
# lbl_2.grid(row=0,column=4)
# lbls_frame.grid_columnconfigure(0,weight=1)
#----------------------------------------------------------------

#----------------------------------------------------------------
# To be removed
# groups_frame.grid(row=1, column=1)
# group_16.grid(row=1, column=1)
# group_8.grid(row=1, column=2)
# group_4.grid(row=1, column=3)
# group_2.grid(row=1, column=4)
# btn_generate_matches.pack()
#----------------------------------------------------------------
