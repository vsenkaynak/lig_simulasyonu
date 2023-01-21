# from IPython.display import HTML, display
from pprint import pprint
from random import shuffle
# from tabulate import tabulate
from time import time

from constants import TEAM_LIST, BIG_TEAMS, BALANCED_TEAM_LIST, DERBY, ALL_EQUAL
from games import Game
from score_list import get_score_list
from seasons import Season
from teams import Team
from write_tables import write_all, get_team_positions, champions, h2h


def main():
    print('starting main function')
    start_time = time()
    # get most common scores
    all_time_scores = get_score_list()

    # create team object from list of teams
    teams_list = [Team(x[0], x[1]) for x in ALL_EQUAL]

    # get the derby teams in a list to create head to head tables
    derby_teams = []
    for t in teams_list:
        if t.name in DERBY:
            derby_teams.append(t)

    SEASONS = 1000 # number of seasons to simulate
    year = 1
    all_seasons = []
    failed = False
    total_games = []
    while True:
        shuffle(teams_list)

        # season object
        curr_season = Season(year, teams_list)
        all_seasons.append(curr_season)

        # create schedule for the current season
        yearly_schedule = []
        for x in range(len(teams_list)):
            if x + 1 == len(teams_list):
                break
            schedule_per_team = matches_per_team(teams_list[x:])
            for s in schedule_per_team:
                yearly_schedule.append(s)

        # create game(matches) object, set result of the games
        all_games = []
        for team in yearly_schedule:
            x = Game(team[0], team[1], year)
            x.set_odds()
            x.set_winner()
            x.add_score(all_time_scores)
            all_games.append(x)
            total_games.append(x)

        # close out season and update stats for the current season
        for t in teams_list:
            t.close_season(year)
        curr_season.set_season_data()
        curr_season.set_season_stats()

        if year >= SEASONS:
            break
        #print(year)
        year += 1

    print('starting after while loop')
    start_time2 = time()
    if failed:
        print(error)
        return

    # write tables to html for exceptional seasons
    write_all(all_seasons)

    # create html for each team's best and worst position
    get_team_positions(all_seasons, teams_list)

    # create html to show championship count for all seasons
    champions(all_seasons)

    # calculate head to head games
    for x in range(len(derby_teams)):
        if x == len(derby_teams):
            break
        get_h2h(derby_teams[x:])

    for t in teams_list:
        print(f'{t.name}: {t.strength}')

    end_time2 = time()
    print(f'Time to starting after while loop is {round(end_time2 - start_time2, 3)} seconds')
    end_time = time()
    print(f'Time to complete main function is {round(end_time - start_time, 3)} seconds')


def matches_per_team(team_list):
    number_of_teams = len(team_list)
    schedule = []
    for x in range(1, number_of_teams):
        home = [team_list[0], team_list[x]]
        schedule.append(home)
        away = [team_list[x], team_list[0]]
        schedule.append(away)
    return schedule


def get_h2h(teams_list):
    t_length = len(teams_list)
    for x in range(1, t_length):
        t1 = teams_list[0].all_match_schedule
        t2 = teams_list[x].all_match_schedule
        game_list = list(set(t1).intersection(set(t2)))
        h2h(game_list)


if __name__ == '__main__':
    main()
