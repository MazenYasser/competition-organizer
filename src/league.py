from src.Competition import Competition
from src.Team import Team


class League(Competition):
    # take scoreboard as a dictionary
    def __init__(self):
        super().__init__()
        self.scoreboard = []

    def update_scoreboard(self):
        """function for updating the scoreboard"""
        # Sort teams list based on points
        sorted_teams = sorted(self.teams, key=lambda element: element.point, reverse=True)
        for i, team in enumerate(sorted_teams):
            self.scoreboard.append({
                'RANK': i + 1,
                'NAME': team.name,
                'POINTS': team.point,
                'GOALS SCORED': team.goals_scored,
                'GOALS CONCEDED': team.goals_conceded,
                'WIN': team.win_count,
                'LOSE': team.loss_count,
                'DRAW': team.draw_count
            })
        return self.scoreboard


# t1 = Team()
# t1.set_name("zama")
# t1.point = 15
# t2 = Team()
# t2.set_name("ahly")
# t2.point = 20
# t3 = Team()
# t3.set_name("isma")
# t3.point = 10
#
# league = League()
# league.add_team(t1)
# league.add_team(t2)
# league.add_team(t3)
#
# print(league.update_scoreboard())


