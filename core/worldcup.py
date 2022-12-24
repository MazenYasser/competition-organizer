from random import randint

from core.league import League
from core.cup import Cup
from core.competition import Competition


class Worldcup(Competition):
    def __init__(self):
        super().__init__()
        self.groups = [League() for i in range(8)]
        self.round_16 = Cup()

    def groups_draw(self):
        """MAKES THE DRAW AND DIVIDE THE TEAMS INTO 8 GROUPS BASED ON STRENGTH"""
        if len(self.teams) != 32:
            print("32 teams must be available to make the draw")
            return

        # Sort team based on strength

        sorted_teams = sorted(self.teams, key=lambda element: element.strength, reverse=True)
        for i, group in enumerate(self.groups):
            group.teams.append(sorted_teams[i])
            group.teams.append(sorted_teams[8+i])
            group.teams.append(sorted_teams[16+i])
            group.teams.append(sorted_teams[24+i])

    def groups_stage_completed(self):
        """RETURNS TRUE IF ALL MATCHES IN GROUP STAGE WERE PLAYED"""
        for group in self.groups:
            if not group.is_finished():
                return False
        return True

    def get_16_stage_teams(self):
        """RETURN THE 16 QUALIFIED TEAMS AFTER COMPLETING GROUP STAGE"""
        if not self.groups_stage_completed():
            print('GROUP STAGE NOT ENDED YET!')
            return
        qualified_teams = []
        for group in self.groups:
            sorted_teams = sorted(group.teams, key=lambda element: element.point, reverse=True)
            qualified_teams.append(sorted_teams[0])
            qualified_teams.append(sorted_teams[1])
        return qualified_teams

    def simulate_groups_results(self):
        for group in self.groups:
            for match in group.matches:
                match.set_result(randint(0, 5), randint(0, 5))
                print(match.home_team_goals, '..', match.away_team_goals)
