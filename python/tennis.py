# -*- coding: utf-8 -*-


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def won(self, other_player):
        return self.points >= 4 and other_player.points >= 0 and \
            (self.points - other_player.points) >= 2

    def advantage_over(self, other_player):
        return self.points > other_player.points and other_player.points >= 3


class Translator:
    def __init__(self):
        pass

    def score_to_word(self, score):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }[score]

    def translate(self, score_1, score_2):
        if score_1 == score_2 and score_1 < 3:
            return self.score_to_word(score_1) + "-All"
        if score_1 == score_2 and score_1 > 2:
            return "Deuce"

        return self.score_to_word(score_1) + "-" + self.score_to_word(score_2)


class TennisGame:
    def __init__(self, player_1_name, player_2_name):
        self.player_1 = Player(player_1_name)
        self.player_2 = Player(player_2_name)
        self.translator = Translator()

    def won_point(self, player_name):
        if player_name == self.player_1.name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        if self.player_1.won(self.player_2):
            return "Win for " + self.player_1.name

        if self.player_2.won(self.player_1):
            return "Win for " + self.player_2.name

        if self.player_1.advantage_over(self.player_2):
            return "Advantage " + self.player_1.name

        if self.player_2.advantage_over(self.player_1):
            return "Advantage " + self.player_2.name

        return self.translator.translate(
            self.player_1.points,
            self.player_2.points)

    def P1Score(self):
        self.player_1.points += 1

    def P2Score(self):
        self.player_2.points += 1
