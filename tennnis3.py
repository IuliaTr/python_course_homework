class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_n = player1_name
        self.p2_n = player2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == "player1":
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if self.p1 == self.p2:
            return "Deuce" if self.p1 >= 3 else ["Love", "Fifteen", "Thirty"][self.p1] + "-All"
        
        if self.p1 >= 4 or self.p2 >= 4:
            s = self.p1_n if self.p1 > self.p2 else self.p2_n
            return f"Advantage {s}" if abs(self.p1 - self.p2) == 1 else f"Win for {s}"

        return ["Love", "Fifteen", "Thirty", "Forty"][self.p1] + "-" + ["Love", "Fifteen", "Thirty", "Forty"][self.p2]


match = TennisGame3("Player A", "Player B")
match.won_point("Player A")
match.won_point("Player B")
match.won_point("Player A")
match.won_point("Player A")
print(match.score())

