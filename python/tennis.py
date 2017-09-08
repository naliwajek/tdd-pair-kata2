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


class TennisGame:
    def __init__(self, player_1_name, player_2_name):
        self.player_1 = Player(player_1_name)
        self.player_2 = Player(player_2_name)

    def won_point(self, player_name):
        if player_name == self.player_1.name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):

        result = ""
        if (self.player_1.points == self.player_2.points and self.player_1.points < 3):
            if (self.player_1.points==0):
                result = "Love"
            if (self.player_1.points==1):
                result = "Fifteen"
            if (self.player_1.points==2):
                result = "Thirty"
            result += "-All"
        if (self.player_1.points==self.player_2.points and self.player_1.points>2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.player_1.points > 0 and self.player_2.points==0):
            if (self.player_1.points==1):
                P1res = "Fifteen"
            if (self.player_1.points==2):
                P1res = "Thirty"
            if (self.player_1.points==3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.player_2.points > 0 and self.player_1.points==0):
            if (self.player_2.points==1):
                P2res = "Fifteen"
            if (self.player_2.points==2):
                P2res = "Thirty"
            if (self.player_2.points==3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res


        if (self.player_1.points>self.player_2.points and self.player_1.points < 4):
            if (self.player_1.points==2):
                P1res="Thirty"
            if (self.player_1.points==3):
                P1res="Forty"
            if (self.player_2.points==1):
                P2res="Fifteen"
            if (self.player_2.points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.player_2.points>self.player_1.points and self.player_2.points < 4):
            if (self.player_2.points==2):
                P2res="Thirty"
            if (self.player_2.points==3):
                P2res="Forty"
            if (self.player_1.points==1):
                P1res="Fifteen"
            if (self.player_1.points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res

        if self.player_1.advantage_over(self.player_2):
            result = "Advantage " + self.player_1.name

        if self.player_2.advantage_over(self.player_1):
            result = "Advantage " + self.player_2.name

        if self.player_1.won(self.player_2):
            result = "Win for " + self.player_1.name

        if self.player_2.won(self.player_1):
            result = "Win for " + self.player_2.name
        return result

    def SetP1Score(self, number):
        self.player_1.points = number

    def SetP2Score(self, number):
        self.player_2.points = number

    def P1Score(self):
        self.player_1.points += 1

    def P2Score(self):
        self.player_2.points += 1
