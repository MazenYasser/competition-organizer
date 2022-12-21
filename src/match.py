from src.team import Team

class Match():
    
    #Class attributes
    home_team= Team()
    away_team= Team()
    home_team_goals = 0
    away_team_goals = 0
    winner= Team()
    result={}
    

    #Class Constructor
    def __init__(self, home_team, away_team):
        self.home_team= home_team
        self.away_team= away_team
    
    
    #Function documentation
    # Name: set_result
    # Arguments: home_team_goals, away_team_goals
    # Description: sets the result of the match according to the scored goals given as arguments
    # Then sets the associated home and away team's attributes accordingly,
    # namely: win, loss, draw counts and points depending on the result of the match
    # goals scored and conceded by both teams


    def set_result(self, home_team_goals, away_team_goals):
        self.result={self.home_team: home_team_goals, self.away_team: away_team_goals}

        #Home team win condition
        if(self.result.get(self.home_team) > self.result.get(self.away_team)):
            self.winner = self.home_team
            self.home_team.set_point(self.home_team.WIN)
            self.away_team.set_point(self.away_team.LOSS)

        #Away team win condition
        elif(self.result.get(self.home_team) < self.result.get(self.away_team)):
            self.winner = self.away_team
            self.home_team.set_point(self.home_team.LOSS)
            self.away_team.set_point(self.away_team.WIN)

        #Draw condition
        elif(self.result.get(self.home_team) ==  self.result.get(self.away_team)):
            self.winner = 'Draw'
            self.home_team.set_point(self.home_team.DRAW)
            self.away_team.set_point(self.away_team.DRAW)
        
        #Setting match goals
        self.home_team_goals= home_team_goals
        self.away_team_goals= away_team_goals

        #Updating total goals scored and conceded for each team
        self.home_team.set_goals_scored(home_team_goals)
        self.home_team.set_goals_conceded(away_team_goals)

        self.away_team.set_goals_conceded(home_team_goals)
        self.away_team.set_goals_scored(away_team_goals)

    #Added for easy access to match data
    def __call__(self):
        self.match_data={
            "Home team": self.home_team.name,
            "Away team": self.away_team.name,
            "Home team goals": self.home_team_goals,
            "Away team goals": self.away_team_goals,
            "Winner": self.winner.name
        }
        return self.match_data

    #Added for showing string representation of class
    def __str__(self):
        return f'{self.home_team}-{self.away_team}'
        
        
        

#Driver code
if __name__=="__main__":
    match1= Match(home_team='Egypt', away_team='France')
    match1.set_result(3,2)
    print(match1.home_team.name)
    print(match1.away_team.name)

