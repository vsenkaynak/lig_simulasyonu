from random import choice

from teams import Team


class Game:

    def __init__(self, home_team=None, away_team=None, season=None):
        self._home_team = home_team
        self._away_team = away_team
        self.season = season
        self._score = None
        self._h_win_odd = None
        self._a_win_odd = None
        self._winner = None
        Team.set_match_schedule(self._home_team, self)
        Team.set_match_schedule(self._away_team, self)

    def __repr__(self):
        match = f'{self._home_team} - {self._away_team}'
        return match

    def get_random_score(self, score_list):
        self._score = choice(score_list)
        h_goals = self._score[0]
        a_goals = self._score[1]
        return h_goals, a_goals

    def add_score(self, score_list):
        h_goal, a_goal = self.get_random_score(score_list)
        while True:
            if self._winner == 'home':
                if h_goal > a_goal:
                    Team.add_win(self._home_team)
                    Team.add_loss(self._away_team)
                    break
                else:
                    h_goal, a_goal = self.get_random_score(score_list)
            elif self._winner == 'draw':
                if h_goal == a_goal:
                    Team.add_draw(self._home_team)
                    Team.add_draw(self._away_team)
                    break
                else:
                    h_goal, a_goal = self.get_random_score(score_list)
            elif self._winner == 'away':
                if a_goal > h_goal:
                    Team.add_win(self._away_team)
                    Team.add_loss(self._home_team)
                    break
                else:
                    h_goal, a_goal = self.get_random_score(score_list)
            else:
                print('there is a problem at score')
        Team.set_goals_scored(self._home_team, h_goal)
        Team.set_goals_scored(self._away_team, a_goal)
        Team.set_goals_allowed(self._home_team, a_goal)
        Team.set_goals_allowed(self._away_team, h_goal)

    def set_odds(self):
        h_str = self._home_team.strength * 1.2
        a_str = self._away_team.strength * .8
        divider = h_str + a_str
        self._h_win_odd = round((h_str * 100 / divider) * .8)
        self._a_win_odd = round((a_str * 100 / divider) * .8)
        luck_list = [-15, -10, -5, 0, 5, 10, 15]
        game_luck = choice(luck_list)
        if 0 <= (self._h_win_odd + game_luck) <= 80:
            self._h_win_odd += game_luck
            self._a_win_odd -= game_luck
        elif self._h_win_odd + game_luck < 0:
            self._h_win_odd = 0
            self._a_win_odd = 80
        elif self._h_win_odd + game_luck > 80:
            self._h_win_odd = 80
            self._a_win_odd = 0

    def set_winner(self):
        d = range(self._h_win_odd + 1, self._h_win_odd + 21)
        a = range(self._h_win_odd + 21, 101)
        win_number = choice(range(1, 101))
        if win_number in a:
            self._winner = 'away'
        elif win_number in d:
            self._winner = 'draw'
        else:
            self._winner = 'home'

    def show_score(self):
        x = f'{self._home_team}: {self._score[0]} - ' \
            f'{self._away_team}: {self._score[1]}'
        return x



