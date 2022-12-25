from random import randint, shuffle

from core.league import League
from core.cup import Cup
from core.competition import Competition


class Worldcup(Competition):
    def __init__(self):
        super().__init__()
        self.groups = [League() for i in range(8)]
        self.round_16 = Cup()
        self.is_simulation = False

    def groups_draw(self):
        """MAKES THE DRAW AND DIVIDE THE TEAMS INTO 8 GROUPS BASED ON STRENGTH"""
        if len(self.teams) != 32:
            print("32 teams must be available to make the draw")
            return

        # Sort team based on strength
        sorted_teams = self.teams.copy()
        sorted_teams = sorted(sorted_teams, key=lambda element: element.strength, reverse=True)
        class_a = sorted_teams[24:].copy()
        class_b = sorted_teams[16:24].copy()
        class_c = sorted_teams[8:16].copy()
        class_d = sorted_teams[:8].copy()
        shuffle(class_a)
        shuffle(class_b)
        shuffle(class_c)
        shuffle(class_d)
        for i, group in enumerate(self.groups):
            group.teams.append(class_a[i])
            group.teams.append(class_b[i])
            group.teams.append(class_c[i])
            group.teams.append(class_d[i])

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
