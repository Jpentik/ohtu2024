class TennisGame:

    score_names = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
        4: "Game"
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.tied_score()
        elif self.player1_score > 3 or self.player2_score > 3:
            return self.extended_score()
        else:
            return self.game_score()

    def tied_score(self):
        if self.player1_score > 2:
            return "Deuce"
        else:
            return f"{self.score_names[self.player1_score]}-All"
        
    def extended_score(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def game_score(self):
        return f"{self.score_names[self.player1_score]}-{self.score_names[self.player2_score]}"