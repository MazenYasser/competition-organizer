from itertools import permutations, combinations

from match import Match


class Competition:
    """
    Class Competition
    Contains:
        - Teams in the competition.
        - Matches to be played between teams.
    """

    def __init__(self):
        self.teams = []
        self.matches = []

    def add_team(self, team):
        """Adds a team to the competition."""
        if team in self.teams:
            print("{} already exists in the competition.".format(team))
        self.teams.append(team)
        print("{} has been successfully added to the competition.".format(team))

    def remove_team(self, team):
        """Removes a team participating in the competition."""
        if team not in self.teams:
            print("{} doesn't exists.".format(team))
        self.teams.remove(team)
        print("{} has been successfully removed from the competition.".format(team))

    def get_teams(self):
        """Returns teams participating in the competition."""
        return self.teams

    def generate_matches(self, home_away_mode=True):
        """Generates list of matches to be played.
        Parameters
        ----------
            :param home_away_mode: Controls number of matches between every 2 teams.
            (True) 2 matches between every 2 teams.
            (False) 1 matches between every 2 teams.
        """
        if home_away_mode:
            self.matches = [Match(p[0], p[1]) for p in permutations(self.teams, 2)]
        else:
            self.matches = [Match(p[0], p[1]) for p in combinations(self.teams, 2)]


