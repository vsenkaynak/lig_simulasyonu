#from games import Game
class Team:

    def __init__(self, name, strength):
        self.name = name
        self.__strength = strength
        self.goals_scored = 0
        self.goals_allowed = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0
        self.best_position = None
        self.worst_position = None
        self.match_schedule = []
        self._match_results = []
        self.season_data = dict()
        self.all_points = []
        self.all_wins = []
        self.all_draws = []
        self.all_losses = []
        self.all_goals_scored = []
        self.all_goals_allowed = []
        self.all_match_results = []
        self.all_match_schedule = []

    def __repr__(self):
        return self.name

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        self.__strength = strength

    def set_match_schedule(self, match):
        self.match_schedule.append(match)

    def match_results(self):
        for r in self.match_schedule:
            self._match_results.append(r.show_score())
        return self._match_results

    def set_goals_scored(self, goal):
        self.goals_scored += goal

    def set_goals_allowed(self, goal):
        self.goals_allowed += goal

    def add_win(self):
        self.wins += 1
        self.points += 3

    def add_draw(self):
        self.draws += 1
        self.points += 1

    def add_loss(self):
        self.losses += 1

    def set_lig_position(self, pos, season):
        self.season_data[season][0]['position'] = pos
        if self.best_position is None or pos < self.best_position[1]:
            self.best_position = [self, pos, season]
        if self.worst_position is None or pos > self.worst_position[1]:
            self.worst_position = [self, pos, season]

    def close_season(self, season):
        self.season_data[season] = []
        data = {
            'year': season,
            'team': self.name,
            'points': self.points,
            'wins': self.wins,
            'draws': self.draws,
            'losses': self.losses,
            'gf': self.goals_scored,
            'ga': self.goals_allowed,
            'gd': self.goals_scored - self.goals_allowed,
            'matches': self.match_schedule,
            'results': self.match_results()
        }
        self.season_data[season].append(data)
        self.all_points.append(self.points)
        self.points = 0
        self.all_wins.append(self.wins)
        self.wins = 0
        self.all_draws.append(self.draws)
        self.draws = 0
        self.all_losses.append(self.losses)
        self.losses = 0
        self.all_goals_scored.append(self.goals_scored)
        self.goals_scored = 0
        self.all_goals_allowed.append(self.goals_allowed)
        self.goals_allowed = 0
        for m in self._match_results:
            self.all_match_results.append(m)
        self._match_results = []
        for m in self.match_schedule:
            self.all_match_schedule.append(m)
        self.match_schedule = []


