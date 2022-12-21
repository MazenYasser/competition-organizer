from competition import Competition


class League(Competition):
    # take scoreboard as a dictionary
    def __init__(self):
        super().__init__()

    def update_scoreboard(self):
        """function for updating the scoreboard"""
        # Sort teams list based on points
        scoreboard = sorted(self.teams, key=lambda element: element.point, reverse=True)
        return scoreboard


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
# scoreboard = league.update_scoreboard()
# for team in scoreboard:
#     print(team)


