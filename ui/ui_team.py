from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import *

from src.competition import Competition
from src.cup import Cup
from src.league import League
from src.team import Team
from ui.scoreboard import render_scoreboard
from ui.cup_ui import show_cup_matches_window


class TeamGUI:

    font = ("Times New Roman", 25)

    def __init__(self, competition, width=1000, height=750):

        self.competition = competition
        #   call a method to generate window only
        self.generate_window(width=width, height=height)
        #   call a method to generate frames only
        self.initialize_frames()
        #   Build all needed variables to fetch the data from the Ui
        self.team_name = StringVar()
        self.team_strength = StringVar()
        self.combo_choice = StringVar()
        #   Initialize all widgets Label, Button, Combobox, ScrolledText and so on
        self.initialize_window()
        #   Pack and put the initialized widgets on its frames
        self.put_on_frames()
        #   View the main window to be appeared to user
        self.team_window.mainloop()

    def generate_window(self, width=1000, height=720):
        # creating the team ui windows.
        self.team_window = Toplevel()
        self.team_window.geometry(str(width) + 'x' + str(height))
        self.team_window.title("Teams")

    def initialize_window(self):
        #     {team_data_frame} part
        # Team {name} part
        self.team_name_lbl = Label(self.team_data_frame, text="Team Name", font=TeamGUI.font)
        self.team_name_entry = Entry(self.team_data_frame, font=TeamGUI.font, textvariable=self.team_name)

        #   Team {strength} part
        self.team_strength_lbl = Label(self.team_data_frame, text="Team Strength", font=TeamGUI.font)
        self.team_strength_entry = Entry(self.team_data_frame, font=TeamGUI.font, textvariable=self.team_strength)

        #   Team modification part
        self.team_modify_lbl = Label(self.team_data_frame, text="Team To Modify", font=TeamGUI.font)
        teams_names = [team.name for team in self.competition.teams]
        self.team_modify_combobox = ttk.Combobox(self.team_data_frame, values=teams_names, width=27,
                                                 textvariable=self.combo_choice, state="readonly")
        #   Modification Button
        self.modify_btn = Button(self.team_data_frame, text="Modify", command=lambda: self.modify_team(),
                                 font=TeamGUI.font)

        #   Delete Button
        self.delete_btn = Button(self.team_data_frame, text="Delete", command=lambda: self.delete_team(),
                                 font=TeamGUI.font)

        #   Addition Button
        self.add_btn = Button(self.team_data_frame, text="Add", command=lambda: self.add_team(), font=TeamGUI.font)

        #   Next Button
        self.next_btn = Button(self.team_data_frame, text="Next", command=self.next_call, font=TeamGUI.font)

        ###     {summary_data_frame} part   ###
        #   Scrolled Text widget
        self.scrltxt_summary_data = scrolledtext.ScrolledText(self.summary_data_frame, font=TeamGUI.font,
                                                              state="disabled")

    def initialize_frames(self):
        self.team_data_frame = Frame(self.team_window)
        self.summary_data_frame = Frame(self.team_window)

    #   Service Method
    #   method documentation:
    #       Name:           put_on_frames
    #       Parameters:     {self} object reference
    #       Description:    Build all widgets and arranges it on its Frames as it designed in {initate_widgets}
    #       Return:         None
    def put_on_frames(self):

        #   Pack the main containers: Frames
        self.team_data_frame.pack(side=LEFT)
        self.summary_data_frame.pack(side=RIGHT)

        #   Pack {name} widgets
        self.team_name_lbl.pack()
        self.team_name_entry.pack()

        #   Pack {strength} widgets
        self.team_strength_lbl.pack()
        self.team_strength_entry.pack()

        #   Pack modify label
        self.team_modify_lbl.pack()

        #   Pack modification combobox
        self.team_modify_combobox.pack()

        #   Pack control buttons: add, delete, modify, next
        self.delete_btn.pack(side=LEFT)
        self.modify_btn.pack(side=LEFT)
        self.add_btn.pack(side=LEFT)
        self.next_btn.pack()

        #   Pack the scrolled text widget on its frame
        self.scrltxt_summary_data.pack(side=RIGHT)

    def refresh_page(self):
        self.update_teams_combox()
        self.modify_board()

    def update_teams_combox(self):
        """Updates team_modify_combobox based on competition teams."""
        self.team_modify_combobox['values'] = [team.name for team in self.competition.teams]

    def modify_board(self):
        """Update summary scrolled text with teams"""
        #   Enable Edit mode
        self.scrltxt_summary_data.config(state="normal")

        #   Clear All previous textbox data
        self.scrltxt_summary_data.delete('1.0', END)

        #   Update the textbox data with the new data which is saved in class attribute {TeamGUI.all_teams}
        self.scrltxt_summary_data.insert(INSERT,
                                         f"Teams\t\tStrength"
                                         f"\n_______________________________\n"
                                         f"{self.generate_board_data()}")
        #   Re-disable Edit mode
        self.scrltxt_summary_data.config(state="disabled")

    def generate_board_data(self):
        #   data initially is empty
        data = ''
        #   Loop for adding and appending the next team data
        for team in self.competition.teams:
            #   Append the next team data to the {data} to be returned
            data = data + team.name + "\t\t" + str(team.strength) + "\n"
        #   Return full string after generating the string representation of the class attribute {TeamGUI.all_teams}
        return data

    def delete_team(self):
        #   Fetch the team from the current selection of combobox list
        to_remove = self.combo_choice.get()

        #   Identifier for start scanning the list which contains the team data to delete it
        index_to_delete = -1

        #   Loop for scanning
        for team in self.competition.teams:
            # Check if the team which is needed to be deleted is added before
            index_to_delete += 1
            if to_remove == team.name:
                # Show and delete the team which will be deleted
                self.competition.remove_team(team)
                # refresh page contents
                self.refresh_page()
                # Show a popup message to verify deletion
                showinfo(title="Successful Deletion", message="Done !")
                #  no more loop needed so break the loop
                break

        # Check if the index_to_delete
        if index_to_delete == len(self.competition.teams):
            # If the loop is ended or the list is empty, just notify the user that is no data to delete
            showinfo(title="Deletion info", message="No Team to delete")

    def add_team(self):
        #   Get the new team name
        name = self.team_name.get()
        #   Get the new team Strength
        strength = self.team_strength_entry.get()

        if not self.name_is_valid(name):
            showerror(title="Add Error", message="The team name is already used!")
            return

        if not self.strength_is_valid(strength):
            showerror(title="Add Error", message="Invalid strength!")
            return

        new_team = Team(name, int(strength))
        self.competition.add_team(new_team)

        self.refresh_page()

    def name_is_valid(self, name):
        for team in self.competition.teams:
            if team.name.lower() == name.lower():
                return False
        return True

    def strength_is_valid(self, strength):
        if not strength.isdecimal():
            return False
        return True


    #   Core Method
    #   method documentation:
    #       Name:           modify_team
    #       Parameters:     {self} object reference
    #       Description:    Get a Team data from Entry {name}, {strength} element and
    #                       Get the selected choice of the combobox list,
    #                       Then update the value of the chose team element {name}, {strength}
    #                       And refactor the {scrolled text} data
    #       Return:         None
    def modify_team(self):
        #   Get a copy of the choices list
        combo_choice = list(self.team_modify_combobox['values'])
        #   check if the list is not empty
        if len(combo_choice) > 0:
            #   Fetch new data from Ui get choice, new name to modify, new strength to modify
            choice_to_modify = self.combo_choice.get()
            name_to_modify = self.get_name().upper()
            strength_to_modify = self.get_strength()

            #   Check if the new name to modify if found
            if name_to_modify not in [team[0] for team in TeamGUI.all_teams]:
                #   Get the index of choice in combobox choices to be changed by the new values
                index_to_modify = combo_choice.index(choice_to_modify)

                #   >>>@Issue Competition remove_team() ?!??!?!?!??!?!
                TeamGUI.competition.remove_team(TeamGUI.all_teams[index_to_modify])

                #   >>>@Issue Competition add_team()
                TeamGUI.all_teams[index_to_modify].name = name_to_modify
                TeamGUI.all_teams[index_to_modify].strength = strength_to_modify
                TeamGUI.competition.add_team(TeamGUI.all_teams[index_to_modify])

                #   Modify the choice in Combobox
                combo_choice[index_to_modify] = name_to_modify
                #   Modify the choice name in the general list
                TeamGUI.all_teams[index_to_modify][0] = name_to_modify
                #   Modify the choice strength in the general list
                TeamGUI.all_teams[index_to_modify][1] = strength_to_modify
                #   Update the combobox list
                self.team_modify_combobox['values'] = combo_choice
                #   Update the scrollable text data with the modified team data
                self.modify_board()

                print("Modify Team")
                #   A popup message to notify the user the task has been done successfully
                showinfo(title="Successful Modification", message="Done !")
            #   Check if the name to update is already used
            else:
                #   A popup message notifies the error
                showerror(title="Error Modification", message="Can't modify team data, The new name is already used !")
                #   Print the error message to console
                print("Can't Modify this team, the name is already used...")
        #   Check if the team to be modified is not found
        else:
            #   A popup message notifies the error
            showinfo(title="Modification info", message="No element to Modify !")
            #   Print the error message to console
            print("No element to Modify...")

    def __call__(self):
        return TeamGUI.all_teams

    def next_call(self):
        self.team_window.destroy()
        if isinstance(self.competition, Cup):
            show_cup_matches_window(self.competition)
        else:
            render_scoreboard(self.competition)




def ui_team_test():
    tgui = TeamGUI(width="1500", height="780", mode=TeamGUI.NATIONAL)
    print(tgui())

