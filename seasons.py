
import pandas as pd

from statistics import mean, median

from teams import Team


class Season:

    most_points = []
    most_wins = []
    most_losses = []
    most_draws = []
    most_goals_scored = []
    most_goals_allowed = []
    least_points = []
    least_wins = []
    least_losses = []
    least_draws = []
    least_goals_scored = []
    least_goals_allowed = []

    def __init__(self, season_number, team_list):
        self.__season_number = season_number
        self.__teams_list = team_list
        # self.game_list = []
        self.team_data = []
        self.__df = None

    def __repr__(self):
        return str(self.__season_number)

    def set_season_data(self):
        df = pd.DataFrame(columns = ['Teams', 'Games', 'Points', 'Wins', 'Draws',
                                     'Losses', 'Goals Scored', 'Goals Allowed', 'Goal Difference'])
        for x in self.__teams_list:
            y = x.season_data[self.__season_number]
            for data in y:
                d1 = {
                    'Teams': data['team'],
                    'Games': len(data['results']),
                    'Points': data['points'],
                    'Wins': data['wins'],
                    'Draws': data['draws'],
                    'Losses': data['losses'],
                    'Goals Scored': data['gf'],
                    'Goals Allowed': data['ga'],
                    'Goal Difference': data['gd']
                }
                df_to_append = pd.DataFrame(d1, index=[0])
                df = pd.concat([df, df_to_append], ignore_index=True)
        self.__df = df

    def show_league_table(self):
        self.__df.sort_values(by=['Points', 'Goal Difference', 'Goals Scored', 'Wins'],
                       inplace=True, ascending=False, ignore_index=True)
        self.__df.index += 1
        return self.__df

    def get_season_number(self):
        return self.__season_number

    def set_champion(self):
        self.__df.sort_values(by=['Points', 'Goal Difference', 'Goals Scored', 'Wins'],
                       inplace=True, ascending=False, ignore_index=True)
        champ = self.__df.iat[0, 0]
        points = self.__df.iat[0, 2]
        for t in self.__teams_list:
            if t.name == champ:
                self.champion = champ
                x = [t, points, self.__season_number]
                self.most_points.append(x)

    def set_least_points(self):
        self.__df.sort_values(by=['Points', 'Goal Difference', 'Goals Scored', 'Wins'],
                       inplace=True, ascending=True, ignore_index=True)
        team = self.__df.iat[0, 0]
        least_points = self.__df.iat[0, 2]
        for t in self.__teams_list:
            if t.name == team:
                self.s_least_points = t
                x = [t, least_points, self.__season_number]
                self.least_points.append(x)

    def set_most_wins(self):
        self.__df.sort_values(by=['Wins', 'Points', 'Goal Difference', 'Goals Scored'],
                       inplace=True, ascending=False, ignore_index=True)
        team = self.__df.iat[0, 0]
        most_wins = self.__df.iat[0, 3]
        for t in self.__teams_list:
            if t.name == team:
                self.s_most_wins = t
                x = [t, most_wins, self.__season_number]
                self.most_wins.append(x)

    def set_least_wins(self):
        self.__df.sort_values(by=['Wins', 'Points', 'Goal Difference', 'Goals Scored'],
                       inplace=True, ascending=True, ignore_index=True)
        team = self.__df.iat[0, 0]
        least_wins = self.__df.iat[0, 3]
        for t in self.__teams_list:
            if t.name == team:
                self.s_least_wins = t
                x = [t, least_wins, self.__season_number]
                self.least_wins.append(x)

    def set_most_losses(self):
        self.__df.sort_values(by=['Losses', 'Goals Allowed', 'Goal Difference'],
                              inplace=True, ascending=False, ignore_index=True)
        team = self.__df.iat[0, 0]
        most_losses = self.__df.iat[0, 5]
        for t in self.__teams_list:
            if t.name == team:
                self.s_most_losses = t
                x = [t, most_losses, self.__season_number]
                self.most_losses.append(x)

    def set_least_losses(self):
        self.__df.sort_values(by=['Losses', 'Goals Allowed', 'Goal Difference'],
                       inplace=True, ascending=True, ignore_index=True)
        team = self.__df.iat[0, 0]
        least_losses = self.__df.iat[0, 5]
        for t in self.__teams_list:
            if t.name == team:
                self.s_least_losses = t
                x = [t, least_losses, self.__season_number]
                self.least_losses.append(x)

    def set_most_draws(self):
        self.__df.sort_values(by=['Draws', 'Points', 'Goals Allowed', 'Goal Difference'],
                              inplace=True, ascending=False, ignore_index=True)
        team = self.__df.iat[0, 0]
        most_draws = self.__df.iat[0, 4]
        for t in self.__teams_list:
            if t.name == team:
                self.s_most_draws = t
                x = [t, most_draws, self.__season_number]
                self.most_draws.append(x)

    def set_least_draws(self):
        self.__df.sort_values(by=['Draws', 'Points', 'Goals Allowed', 'Goal Difference'],
                       inplace=True, ascending=True, ignore_index=True)
        team = self.__df.iat[0, 0]
        least_draws = self.__df.iat[0, 4]
        for t in self.__teams_list:
            if t.name == team:
                self.s_least_draws = t
                x = [t, least_draws, self.__season_number]
                self.least_draws.append(x)

    def set_most_goals_scored(self):
        self.__df.sort_values(by=['Goals Scored', 'Points', 'Goal Difference', 'Wins'],
                              inplace=True, ascending=False, ignore_index=True)
        team = self.__df.iat[0, 0]
        most_goals_scored = self.__df.iat[0, 6]
        for t in self.__teams_list:
            if t.name == team:
                self.s_most_goals_scored = t
                x = [t, most_goals_scored, self.__season_number]
                self.most_goals_scored.append(x)

    def set_least_goals_scored(self):
        self.__df.sort_values(by=['Goals Scored', 'Points', 'Goal Difference', 'Wins'],
                       inplace=True, ascending=True, ignore_index=True)
        team = self.__df.iat[0, 0]
        least_goals_scored = self.__df.iat[0, 6]
        for t in self.__teams_list:
            if t.name == team:
                self.s_least_goals_scored = t
                x = [t, least_goals_scored, self.__season_number]
                self.least_goals_scored.append(x)

    def set_most_goals_allowed(self):
        self.__df.sort_values(by=['Goals Allowed', 'Points', 'Goal Difference', 'Wins'],
                              inplace=True, ascending=False, ignore_index=True)
        team = self.__df.iat[0, 0]
        most_goals_allowed = self.__df.iat[0, 7]
        for t in self.__teams_list:
            if t.name == team:
                self.s_most_goals_allowed = t
                x = [t, most_goals_allowed, self.__season_number]
                self.most_goals_allowed.append(x)

    def set_least_goals_allowed(self):
        self.__df.sort_values(by=['Goals Allowed', 'Points', 'Goal Difference', 'Wins'],
                       inplace=True, ascending=True, ignore_index=True)
        team = self.__df.iat[0, 0]
        least_goals_allowed = self.__df.iat[0, 7]
        for t in self.__teams_list:
            if t.name == team:
                self.s_least_goals_allowed = t
                x = [t, least_goals_allowed, self.__season_number]
                self.least_goals_allowed.append(x)

    def set_lig_positions(self):
        self.__df.sort_values(by=['Points', 'Goal Difference', 'Goals Scored', 'Wins'],
                       inplace=True, ascending=False, ignore_index=True)
        self.__df.index += 1
        total_strength = []
        for t in self.__teams_list:
            total_strength.append(t.strength)
            x = self.__df.index[self.__df['Teams'] == t.name].tolist()[0]
            if x == 1:
                t.strength += 3
            if x == 2:
                t.strength += 2
            if x == 3 or x == 4:
                t.strength += 1
            if x == 16 or x == 17:
                t.strength -= 1
            if x == 18:
                t.strength -= 2
            if x == 19:
                t.strength -= 3
            Team.set_lig_position(t, x, self.__season_number)
        t_mean = round(mean(total_strength))
        t_median = round(median(total_strength))
        for t in self.__teams_list:
            if t.strength <= t_mean * 0.15:
                t.strength = round(t_median)
            if t.strength >= t_mean * 1.85:
                t.strength = round(t_median)

    def set_season_stats(self):
        self.set_champion()
        self.set_lig_positions()
        self.set_most_wins()
        self.set_least_wins()
        self.set_least_points()
        self.set_most_losses()
        self.set_least_losses()
        self.set_most_draws()
        self.set_least_draws()
        self.set_most_goals_scored()
        self.set_least_goals_scored()
        self.set_most_goals_allowed()
        self.set_least_goals_allowed()

