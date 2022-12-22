import sys
sys.path.append('D:\Engineering\Fourth Year\Python\Tournament Organizer Project\Competation_Organizer')
from src.team import Team

class Match:

    #Class Constructor
    def __init__(self, home_team, away_team):
        self.home_team = Team()
        self.home_team= home_team
        self.away_team = Team()
        self.away_team= away_team
        self.home_team_goals = 0
        self.away_team_goals = 0
        self.winner= Team()
        self.isPlayed = False
        self.result=''
    
    #Function documentation
    # Name: set_result
    # Arguments: home_team_goals, away_team_goals
    # Description: sets the result of the match according to the scored goals given as arguments
    # Then sets the associated home and away team's attributes accordingly,
    # namely: win, loss, draw counts and points depending on the result of the match
    # goals scored and conceded by both teams


    def set_result(self, home_team_goals, away_team_goals):

        #Setting match goals
        self.home_team_goals= home_team_goals
        self.away_team_goals= away_team_goals

        #Home team win condition
        if(self.home_team_goals > self.away_team_goals):
            self.winner = self.home_team
            self.home_team.set_point(self.home_team.WIN)
            self.away_team.set_point(self.away_team.LOSS)
            self.result='Home Win'

        #Away team win condition
        elif(self.home_team_goals < self.away_team_goals):
            self.winner = self.away_team
            self.home_team.set_point(self.home_team.LOSS)
            self.away_team.set_point(self.away_team.WIN)
            self.result='Away Win'

        #Draw condition
        elif(self.home_team_goals == self.away_team_goals):
            self.winner.set_name('None')
            self.home_team.set_point(self.home_team.DRAW)
            self.away_team.set_point(self.away_team.DRAW)
            self.result='Draw'

        #Updating total goals scored and conceded for each team
        self.home_team.set_goals_scored(home_team_goals)
        self.home_team.set_goals_conceded(away_team_goals)

        self.away_team.set_goals_scored(away_team_goals)
        self.away_team.set_goals_conceded(home_team_goals)

        #Updating isPlayed flag
        self.isPlayed= True
        

    #Added for easy access to match data
    def __call__(self):
        self.match_data={
            "Home team": self.home_team.name,
            "Away team": self.away_team.name,
            "Home team goals": self.home_team_goals,
            "Away team goals": self.away_team_goals,
            "Winner": self.winner.name,
            "Result": self.result
        }
        return self.match_data

    #Added for showing string representation of class
    def __str__(self):
        return f'{self.home_team}-{self.away_team}'

        
        
        

#Driver code
if __name__=="__main__":
   match1= Match(home_team='Egypt', away_team='France')
   match1.set_result(0,0)
   print(match1.home_team.name)
   print(match1.away_team.name)
   print(match1())

