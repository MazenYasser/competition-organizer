
class League():
    # take scoreboard as a dictionary
    def __init__(self ,scoreboard):
        self.scoreboard=scoreboard
    # function for updating the scoreboard
    def update_scoreboard(self):
        # here I used a list to store the dictionary
        updt_scoreboard=[(value, key) for key, value in self.scoreboard.items()]
        updt_scoreboard.sort(reverse=True)
        return updt_scoreboard

   # this code for testing the class
# d={'Ahly':15,'Ayman':20,'Mazen':1,'zamalek':17,'magdy':25}
# test =League(d)
# for i in range(len(d)):
#     print(test.update_scoreboard()[i][1])
