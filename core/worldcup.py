from core.league import League
from core.cup import Cup
from core.competition import Competition


class Worldcup(Competition):
    def __init__(self):
        super().__init__()
        self.groups = [League() for i in range(8)]
        self.round_16 = Cup()

    def groups_draw(self):
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
