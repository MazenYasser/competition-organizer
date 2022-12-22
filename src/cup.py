from src.competition import Competition
from random import shuffle
from src.match import Match
from src.team import Team


class Cup(Competition):
    def __init__(self):
        super().__init__()
        self.rounds = []
        self.winner = ''
        self.isFinished = False

    def start_cup(self):
        """Validates teams number and creates first round of the cup."""

        # Validate competition size
        valid_cup_size = [32, 16, 8, 4, 2]
        if len(self.teams) not in valid_cup_size:
            print("Invalid teams size.")
            return

        # Create first round
        shuffle(self.teams)
        self.generate_round()

    def generate_round(self):
        """Create a round and adds a new round to rounds"""
        # Create matches list for the first round
        matches = [Match(self.teams[i], self.teams[i + 1]) for i in range(0, len(self.teams), 2)]
        # create this round dictionary
        current_round = {
            'stage': len(self.teams),
            'teams': self.teams.copy(),
            'matches': matches
        }
        # Append the round to list of round
        self.rounds.append(current_round)

    def generate_next_round(self):
        """Generates next round teams and matches."""
        if len(self.rounds) < 1:
            print("Please start the competition.")
            return

        last_round = self.rounds[-1]

        # Check if all last_round matches were played
        for match in last_round['matches']:
            if not match.isPlayed:
                print('All matches in the last round must be played, the match between '
                      '{} vs {} is not yet played.'.format(match.home_team.name,
                                                           match.away_team.name))
                return

            if match.away_team == match.home_team_goals:
                print('Cup match can not be a tie.'
                      'The match between {} vs {} is a draw.'.format(match.home_team.name,
                                                                     match.away_team.name))
                return

        # Get winner_teams and update current competition teams
        winner_teams = []
        for match in last_round['matches']:
            if match.home_team_goals > match.away_team_goals:
                winner_teams.append(match.home_team)
            else:
                winner_teams.append(match.away_team)

        self.teams = winner_teams
        if len(self.teams) > 1:
            self.generate_round()
        else:
            self.isFinished = True

    def get_winner(self):
        """Returns cup winner"""
        if not self.isFinished:
            print('Competition not ended yet.')

        return self.teams[0]


def test_class_cup():
    t1 = Team()
    t1.set_name("Real Madrid")
    t2 = Team()
    t2.set_name("FC Barcelona")
    t3 = Team()
    t3.set_name("Manchester United")
    t4 = Team()
    t4.set_name("Liverpool")

    cup = Cup()
    cup.add_team(t1)
    cup.add_team(t2)
    cup.add_team(t3)
    cup.add_team(t4)

    cup.start_cup()

    for match in cup.rounds[-1]['matches']:
        match.home_team_goals = 4
        match.away_team_goals = 2
        match.isPlayed = True

    cup.generate_next_round()

    for match in cup.rounds[-1]['matches']:
        match.home_team_goals = 4
        match.away_team_goals = 2
        match.isPlayed = True

    cup.generate_next_round()

    print(cup.isFinished)
    print(cup.get_winner())

    print(cup.rounds)
