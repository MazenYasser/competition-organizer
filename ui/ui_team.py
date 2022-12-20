
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import *
class TeamGUI:
    #   Some class attributes for control the GUI flow, fonts, and all added values from GUI
    NATIONAL = 1
    CUP = 2
    font = ("Times New Roman", 25)
    all_teams = []

    #   Class constructor
    def __init__(self, width=1000, height=750, mode=NATIONAL):

        #   Validate The {mode} of Competition whether it's {NATIONAL}, {CUP}
        if mode == TeamGUI.CUP or mode == TeamGUI.NATIONAL:
            self.mode = mode
        #   Generate Error indicates that the {mode} is not available
        else:
            showerror(title="Competition Type Error", message="Competition type have to be only one of these choices "
                                                              "!\nCUP, NATIONAL")
            print("Competition type have to be only one of these choices CUP, NATIONAL")
            return

        #   call a method to generate window only
        self.generate_window(width=width, height=height)
        #   call a method to generate frames only
        self.initate_frames()

        #   Build all needed variables to fetch the data from the Ui
        self.team_name = StringVar()
        self.team_strength = StringVar()
        self.combo_choice = StringVar()

        #   Initialize all widgets Label, Button, Combobox, ScrolledText and so on
        self.initate_widgets()

        #   Pack and put the initialized widgets on its frames
        self.put_on_frames()

        #   View the main window to be appeared to user
        self.run_main_window()

    #   Core Method
    #   method documentation:
    #       Name:           generate_window
    #       Parameters:     {self} object reference, {width} and {height} with default values 1000, 720
    #       Description:    Method to generate all necessary windows with flexable geometry
    #       Return:         None
    def generate_window(self, width=1000, height=720):
        # creating the application main window.
        self.mainwindow = Tk()
        self.mainwindow.geometry(str(width)+'x'+str(height))
        self.mainwindow.title("Teams")

    #   Service Method
    #   method documentation:
    #       Name:           run_main_window
    #
    #       Parameters:     {self} object reference
    #       Description:    run the {mainwindow}
    #       Return:         None
    def run_main_window(self):
        # Entering the event main loop
        self.mainwindow.mainloop()

    #   Core Method
    #   method documentation:
    #       Name:           initate_widgets
    #       Parameters:     {self} object reference
    #       Description:    Build all needed widgets: Labels, Buttons, Combobox and Scrolled Texet
    #       Return:         None
    def initate_widgets(self):
        ###     {team_data_frame} part  ###
        #   Team {name} part
        self.team_name_lbl = Label(self.team_data_frame, text="Team Name", font=TeamGUI.font)
        self.team_name_entry = Entry(self.team_data_frame, font=TeamGUI.font, textvariable=self.team_name)

        #   Team {strength} part
        self.team_strength_lbl = Label(self.team_data_frame, text="Team Strength", font=TeamGUI.font)
        self.team_strength_entry = Entry(self.team_data_frame, font=TeamGUI.font, textvariable=self.team_strength)

        #   Team modification part
        self.team_modify_lbl = Label(self.team_data_frame, text="Team To Modify", font=TeamGUI.font)
        self.team_modify_combobox = ttk.Combobox(self.team_data_frame, values=TeamGUI.all_teams, width=27,
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
        self.next_btn = Button(self.team_data_frame, text="Next", command=self.next, font=TeamGUI.font)

        ###     {summary_data_frame} part   ###
        #   Scrolled Text widget
        self.scrltxt_summary_data = scrolledtext.ScrolledText(self.summary_data_frame, font=TeamGUI.font,
                                                              state="disabled")

    #   Service Method
    #   method documentation:
    #       Name:           initate_frames
    #       Parameters:     {self} object reference
    #       Description:    Build all needed widgets: Frames only
    #       Return:         None
    def initate_frames(self):

        self.team_data_frame = Frame(self.mainwindow)
        self.summary_data_frame = Frame(self.mainwindow)

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

    #   Core Method
    #   method documentation:
    #       Name:           modify_team_list
    #       Parameters:     {self} object reference, name, strength
    #       Description:    update the combobox list values from which its data is entered before
    #                       from entry {name}, {strength}
    #       Return:         True: if the name is unique,
    #                       False: if it is repeated.
    def modify_team_list(self, name, strength=0):
        if name not in self.team_modify_combobox['values']:
            TeamGUI.all_teams.append([name, strength])
            self.team_modify_combobox['values'] = [TeamGUI.all_teams[i][0] for i in range(0, len(TeamGUI.all_teams))]
            return True
        else:
            return False

    #   Core Method
    #   method documentation:
    #       Name:           modify_board
    #       Parameters:     {self} object reference
    #       Description:    update the {modify_board} to show all added Teams with its corresponding strength
    #       Return:         None
    def modify_board(self):
        #   Enable Edit mode
        self.scrltxt_summary_data.config(state="normal")

        #   Clear All previous textbox data
        self.scrltxt_summary_data.delete('1.0', END)

        #   Update the textbox data with the new data which is saved in class attribute {TeamGUI.all_teams}
        self.scrltxt_summary_data.insert(INSERT,
                                         f"Teams\t\tStrength\n_______________________________\n{self.string_for_board()}")
        #   Re-disable Edit mode
        self.scrltxt_summary_data.config(state="disabled")

    #   Core Method
    #   method documentation:
    #       Name:           delete_team
    #       Parameters:     {self} object reference
    #       Description:    Delete team from Combobox list, Scrolled Text and the class attribute {TeamGUI.all_teams}
    #       Return:         None
    def delete_team(self):
        #   Fetch the team from the current selection of combobox list
        to_remove = self.combo_choice.get()

        #   Identifier for start scanning the list which contains the team data to delete it
        index_to_delete = -1

        #   Loop for scanning
        for i in range(0, len(TeamGUI.all_teams)):
            #   Check if the team which is needed to be deleted is added before
            if to_remove == TeamGUI.all_teams[i][0]:
                index_to_delete+=1
                #   Show and delete the team which will be deleted
                print(f"Team {TeamGUI.all_teams[index_to_delete][0]} is Deleted")
                #   delete the team
                del TeamGUI.all_teams[index_to_delete]
                #   update the board
                self.modify_board()
                #   delete that team from the combobox list
                self.delete_team_list(to_remove)
                #   Show a popup message to verify deletion
                showinfo(title="Successful Deletion", message="Done !")
                #   no more loop needed so break the loop
                break

            #   Check if the team which is needed to be deleted is not found anymore
            else:
                #   Increments the identifier {index_to_delete} to test the next item in the list
                index_to_delete += 1
        #   Check if the index_to_delete
        if index_to_delete == len(TeamGUI.all_teams):
            #   If the loop is ended or the list is empty, just notify the user that is no data to delete
            showinfo(title="Deletion info", message="No Team to delete")

    #   Service Method
    #   method documentation:
    #       Name:           delete_team_list
    #       Parameters:     {self} object reference, {to_remove}
    #       Description:    The logic to Delete team from Combobox list
    #       Return:         None
    def delete_team_list(self, to_remove):
        #   copy all combobox values {team_modify_combobox} in a temporary holder {combo_choice}
        combo_choice = list(self.team_modify_combobox['values'])

        #   Check if the {combo_choice} is not empty
        if len(combo_choice) > 0:
            #   Remove the current selection which is saved in {to_remove}
            combo_choice.remove(to_remove)

            #   Re-assign the {combo_choice} to the combobox choices {team_modify_combobox} after deletion
            self.team_modify_combobox['values'] = combo_choice

            #   No set of the current selection
            self.team_modify_combobox.current()

        #   Check if the {combo_choice} is empty
        else:
            showerror(title="Deletion Error", message="No element to be Deleted !")
            print("No element to Delete...")

    #   Service Method
    #   Core Method
    #   method documentation:
    #       Name:           string_for_board
    #       Parameters:     {self} object reference
    #       Description:    The logic for convert the class attribute {TeamGUI.all_teams} names and strength into string
    #       Return:         {data} in string format represents the names and strengths
    def string_for_board(self):
        #   data initially is empty
        data = ''
        #   Loop for adding and appending the next team data
        for team_data in TeamGUI.all_teams:
            #   Append the next team data to the {data} to be returned
            data = data + team_data[0] + "\t\t" + str(team_data[1]) + "\n"
        #   Return full string after generating the string representation of the class attribute {TeamGUI.all_teams}
        return data

    #   Core Method
    #   method documentation:
    #       Name:           add_team
    #       Parameters:     {self} object reference
    #       Description:    Get a new Team data from Entry {name}, {strength} element and
    #                       add it to the class attribute {TeamGUI.all_teams} and
    #                       add it as choice in the combobox elements
    #                       then refactor the scrollable textbox with addition the inserted Team data
    #       Return:         None
    def add_team(self):
        #   Get the new team name
        name = self.get_name()
        #   Get the new team Strength
        strength = self.get_strength()

        #   Check the {self.get_strength()} return to validate input
        #   If the fetched {strength} is valid
        if strength != -1:
            #   Add that {team name} as a new option to the list of combobox options
            #   If that new {team name} is unique
            if self.modify_team_list(name=name, strength=strength):
                #   Print all fetched data
                print(f"Team {name}, {strength} is added..")
                #   Refactor the Scrollable data with adding the new team data
                self.modify_board()
                #   A Popup message for notify the user that the last insertion is valid
                showinfo(title="Successful Addition", message="Done.")

            #   If that new {team name} is used before
            else:
                # A Popup message notifies the user that there are an error in the new {team name} field
                showerror(title="Add Error", message="The team name is already used !")
                #   Print an error message to user
                print("Can't add the same name twice")
        else:
            # A Popup message notifies the user that there are an error in the new {team strength} field
            showerror(title="Strength Error", message="The strength index is invalid !")
            #   Print an error message to user
            print("Strength Invalid")

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
            if name_to_modify not in [Team[0] for Team in TeamGUI.all_teams]:
                #   Get the index of choice in combobox choices to be changed by the new values
                index_to_modify = combo_choice.index(choice_to_modify)
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

    #   Core Method
    #   method documentation:
    #       Name:           get_name
    #       Parameters:     {self} object reference
    #       Description:    Get a Team data from Entry {name}
    #       Return:         {name_data} Team Name in upper case
    def get_name(self):
        #   Fetch the new name from the entry {Team name}
        name_data = self.team_name.get()
        #   Return the Fetched name from the entry {Team name}
        return name_data.upper()

    #   Core Method
    #   method documentation:
    #       Name:           get_strength
    #       Parameters:     {self} object reference
    #       Description:    Get a Team data from Entry {strength},
    #                       validate the input to ensure that was a numerical values only
    #       Return:         If valid :{strength_data} Team strength in integer format
    #                       If not valid : -1
    def get_strength(self):
        #   Fetch the new strength from the entry {Team strength}
        strength_data = self.team_strength.get()
        #   Check if the fetched {strength} is valid (only integers)
        if strength_data.isdecimal():
            #   Return the Fetched strength from the entry {Team strength}
            return int(strength_data)
        #   Check if the fetched {strength} is not valid
        else:
            #   Return -1 as an indication of invalid strength value
            return -1
    #   Service method
    #   method documentation:
    #       Name:           __call__
    #       Parameters:     {self} object reference
    #       Description:    make the object class as callable
    #       Return:         None
    def __call__(self):
        return TeamGUI.all_teams

    #   Service method
    #   method documentation:
    #       Name:           next
    #       Parameters:     {self} object reference
    #       Description:    Ends the GUI application and depending on the object {mode} identifier {mode}: CUP, NATIONAL
    #       Return:         None
    def next(self):
        #   Check the {mode} is NATIONAL
        if self.mode == TeamGUI.NATIONAL:
            #   Check if the number of teams is greater than 1
            if len(TeamGUI.all_teams) > 1:
                #   A popup message notifies that mission has been done successfully
                showinfo(title="Done", message=f"All {len(TeamGUI.all_teams)} teams are added")
                #   Quite the GUI application
                self.mainwindow.quit()
            #   Check if the number of teams is not greater than 1
            else:
                #   A popup message notifies that the error
                showerror(title="Total Teams",
                          message=f"There are an issue in Team number\nNational have {len(TeamGUI.all_teams)} Teams")

        #   Check the {mode} is CUP
        elif self.mode == TeamGUI.CUP:
            #   Check if the number of teams is only 32 teams
            if len(TeamGUI.all_teams) == 32:
                #   A popup message notifies that mission has been done successfully
                showinfo(title="Done", message=f"All {len(TeamGUI.all_teams)} teams are added")
                #   Quite the GUI application
                self.mainwindow.quit()
            #   Check if the number of teams is not 32 teams
            else:
                #   A popup message notifies that the error
                showerror(title="Total Teams",
                          message=f"There are an issue in Team number\nCup have {len(TeamGUI.all_teams)} Teams")


##################    Application Test    ##################
tgui = TeamGUI(width="1500", height="780", mode=TeamGUI.NATIONAL)
print(tgui())
