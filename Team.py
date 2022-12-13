
#   Class Implementation
class Team ():

    #   Class Attributes
    WIN = 3
    DRAW = 1
    LOSS = 0

    #   Class Constructor
    def __init__(self):
        self.name = ''
        self.strength = 0
        self.point = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.win_count = 0
        self.loss_count = 0
        self.draw_count = 0

    #   method documentation:
    #       Name:           set_name
    #       Paramenters:    {self} object reference, {name} which will be initialized not modified more than one time
    #       Discription:    Set {name} attribute of the passed {team object reference}
    #       Return:         None
    def set_name(self, name):
        #   Flag to limit modification times to just one time
        if self.name == '':
            self.name = name
        #   Notify that team name is initialized and con't be modified
        else:
            #   Initially use consol for notification
            print("Can't modify the Team {name} in runtime.")

    #   method documentation:
    #       Name:           set_strength
    #       Paramenters:    {self} object reference, {strength} which will be initialized and modified
    #       Discription:    Set {strength} attribute of the passed {team object reference}
    #       Return:         None

    def set_strength(self, strength):
        if strength >= 0:
            self.strength = strength
        else:
            print("invalid {strength} value inserted.")

    #   method documentation:
    #       Name:           set_point
    #       Paramenters:    {self} object reference, {point} which will be initialized and modified
    #       Discription:    Set {point} attribute of the passed {team object reference} the passed {point} parameter options
    #           Parameters options: Team.WIN, Team.LOSS, Team.DRAW
    #       Return:         None

    def set_point(self, point=LOSS):
        #   If team is winner and parameter passed is Team.WIN
        if point == Team.WIN:
            #   Add value of 2 to {point}
            self.point += Team.WIN
            #   Incremets the {win_count} value by 1
            self.set_win_count()

        #   If team is Drawn and parameter passed is Team.DRAW
        elif point == Team.DRAW:
            #   Add value of 1 to {point}
            self.point += Team.DRAW
            #   no add to {point} value
            self.set_draw_count()

        #   If team is Loss and parameter passed is Team.LOSS
        elif point == Team.LOSS:
            #   no add to {point} value
            self.point += Team.LOSS
            #   Incremets the {loss_count} value by 1
            self.set_loss_count()

        #   If Passed value is not supported
        else:
            print("invalid inserted {point} value.")

    #   method documentation:
    #       Name:           set_goals_scored
    #       Paramenters:    {self} object reference, {goals_scored} which will be initialized and modified
    #       Discription:    Set {goals_scored} attribute of the passed {team object reference} the passed {goals_scored} parameter options
    #       Return:         None
    def set_goals_scored(self, goals_scored):
        #   Validation for the passes parameter {goals_scored}
        if goals_scored >= 0:
            self.goals_scored += goals_scored
        #   If the inserted value is not valid
        else:
            print("invalid inserted {goals_scored} value.")

    #   method documentation:
    #       Name:           set_goals_conceded
    #       Paramenters:    {self} object reference, {goals_conceded} which will be initialized and modified
    #       Discription:    Set {goals_conceded} attribute of the passed {team object reference} the passed {goals_conceded} parameter options
    #       Return:         None
    def set_goals_conceded(self, goals_conceded):
        #   Validation for the passes parameter {goals_conceded}
        if goals_conceded >= 0:
            self.goals_conceded += goals_conceded
        #   If the inserted value is not valid
        else:
            print("invalid inserted {goals_conceded} value.")

    #   method documentation:
    #       Name:           get_win_count
    #       Paramenters:    {self} object reference
    #       Discription:    find and return the {win_count} attribute of the passed {team object reference}
    #       Return:         {win_count} attribute value
    def get_win_count(self):
        return self.win_count

    #   method documentation:
    #       Name:           get_loss_count
    #       Paramenters:    {self} object reference
    #       Discription:    find and return the {loss_count} attribute of the passed {team object reference}
    #       Return:         {loss_count} attribute value
    def get_loss_count(self):
        return self.loss_count

    #   method documentation:
    #       Name:           get_draw_count
    #       Paramenters:    {self} object reference
    #       Discription:    find and return the {draw_count} attribute of the passed {team object reference}
    #       Return:         {draw_count} attribute value
    def get_draw_count(self):
        return self.draw_count

    #set the win count manually 
    def set_win_count(self):
        self.win_count += 1

    #set the draw count manually 
    def set_draw_count(self):
        self.draw_count += 1

    #set the loss count manually 
    def set_loss_count(self):
        self.loss_count += 1

    #   method documentation:
    #       Name:           __call__
    #       Paramenters:    {self} object reference
    #       Discription:    A Dunder function to make the {team object} callable to display all data in about team
    #       Return:         return the list of 2 elements team element 1 is a dectionary of the team data, element 2 is data in string representation

    def __call__(self):
        self.team_data = {
            "Name": self.name,
            "STRENGTH": self.strength,
            "POINT": self.point,
            "WIN_COUNT": self.win_count,
            "DRAW_COUNT": self.draw_count,
            "LOSS_COUNT": self.loss_count,
            "GOALS_SCORED": self.goals_scored,
            "GOALS_CONCEDED": self.goals_conceded
        }
        return [
            self.team_data,
            'Name: {},\tStrength: {},\tPoints: {},\tWin Matches: {},\tDraw Matches: {},\tLoss Matches: {},\tGoals Scored: {},\tGoals Conceded: {}.'.format(self.name, self.strength, self.point,
                                                                                                                                                           self.win_count, self.draw_count, self.loss_count,
                                                                                                                                                           self.goals_scored, self.goals_conceded)
        ]
    
    
    #   method documentation:
    #       Name:           __str__
    #       Paramenters:    {self} object reference
    #       Discription:    A Dunder function to print the team data in string representation
    #       Return:         return the the {team object} data in string representation

    def __str__(self):
        return 'Name: {},\tStrength: {},\tPoints: {},\tWin Matches: {},\tDraw Matches: {},\tLoss Matches: {},\tGoals Scored: {},\tGoals Conceded: {}.'.format(self.name, self.strength, self.point,
                                                                                                                                                           self.win_count, self.draw_count, self.loss_count,
                                                                                                                                                           self.goals_scored, self.goals_conceded)

##################    Application Test    ##################
# t1 = Team()
# t1.set_name("Alberta")
# t1.set_name("Alberta2")
# t1.set_point(Team.WIN)
# t1.set_point(Team.LOSS)
# t1.set_point(Team.DRAW)
# print (t1)
# print (t1())
# print (t1()[0])
# print (t1()[1])
