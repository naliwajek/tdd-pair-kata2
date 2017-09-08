# -*- coding: utf-8 -*-

# introduce player objecto
# move translation to other class


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

    def translate(self, score_1, score_2):
        result = ""
        if (score_1 == score_2 and score_1 < 3):
            if (score_1==0):
                result = "Love"
            if (score_1==1):
                result = "Fifteen"
            if (score_1==2):
                result = "Thirty"
            result += "-All"
        if (score_1==score_2 and score_1>2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (score_1 > 0 and score_2==0):
            if (score_1==1):
                P1res = "Fifteen"
            if (score_1==2):
                P1res = "Thirty"
            if (score_1==3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (score_2 > 0 and score_1==0):
            if (score_2==1):
                P2res = "Fifteen"
            if (score_2==2):
                P2res = "Thirty"
            if (score_2==3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res


        if (score_1>score_2 and score_1 < 4):
            if (score_1==2):
                P1res="Thirty"
            if (score_1==3):
                P1res="Forty"
            if (score_2==1):
                P2res="Fifteen"
            if (score_2==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (score_2>score_1 and score_2 < 4):
            if (score_2==2):
                P2res="Thirty"
            if (score_2==3):
                P2res="Forty"
            if (score_1==1):
                P1res="Fifteen"
            if (score_1==2):
                P1res="Thirty"
            result = P1res + "-" + P2res

        return result


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

        return self.translator.translate(self.player_1.points, self.player_2.points)

    def P1Score(self):
        self.player_1.points += 1

    def P2Score(self):
        self.player_2.points += 1
