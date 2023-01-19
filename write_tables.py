import pandas as pd

from seasons import Season
from teams import Team


def write_all(seasons: list):
    my_max = 'max'
    my_min = 'min'
    my_season, table = get_metrics(Season.most_points, seasons, my_max)
    success = write_to_file(my_season, "most_points", table)

    my_season, table = get_metrics(Season.least_points, seasons, my_min)
    success = write_to_file(my_season, "least_points", table)

    my_season, table = get_metrics(Season.most_wins, seasons, my_max)
    success = write_to_file(my_season, "most_wins", table)

    my_season, table = get_metrics(Season.least_wins, seasons, my_min)
    success = write_to_file(my_season, "least_wins", table)

    my_season, table = get_metrics(Season.most_losses, seasons, my_max)
    success = write_to_file(my_season, "most_losses", table)

    my_season, table = get_metrics(Season.least_losses, seasons, my_min)
    success = write_to_file(my_season, "least_losses", table)

    my_season, table = get_metrics(Season.most_draws, seasons, my_max)
    success = write_to_file(my_season, "most_draws", table)

    my_season, table = get_metrics(Season.least_draws, seasons, my_min)
    success = write_to_file(my_season, "least_draws", table)

    my_season, table = get_metrics(Season.most_goals_scored, seasons, my_max)
    success = write_to_file(my_season, "most_goals_scored", table)

    my_season, table = get_metrics(Season.least_goals_scored, seasons, my_min)
    success = write_to_file(my_season, "least_goals_scored", table)

    my_season, table = get_metrics(Season.most_goals_allowed, seasons, my_max)
    success = write_to_file(my_season, "most_goals_allowed", table)

    my_season, table = get_metrics(Season.least_goals_allowed, seasons, my_min)
    success = write_to_file(my_season, "least_goals_allowed", table)


def get_metrics(metric_list, seasons, min_max):
    if min_max == 'max':
        x_max = max([z[1] for z in metric_list])
    else:
        x_max = min([z[1] for z in metric_list])
    for subarray in metric_list:
        if x_max == subarray[1]:
            idx = metric_list.index(subarray)
    my_season = metric_list[idx]
    table = get_season_table(my_season, seasons)
    return my_season, table


def get_team_positions(seasons, team_list):
    for t in team_list:
        best = t.best_position
        best_table = get_season_table(best, seasons)
        write_to_file(best, 'best_position', best_table)

        worst = t.worst_position
        worst_table = get_season_table(worst, seasons)
        write_to_file(worst, 'worst_position', worst_table)


def write_to_file(season, metric, table):
    team = season[0]
    value = season[1]
    year = season[2]
    html = table.to_html(col_space=85, justify='center')
    text = '\n<ul style="font-size:120%">'
    for m in team.season_data[year][0]['results']:
        text += f'\n<li>{m}</li>'
    text += '\n</ul>'
    # write html to file
    with open(f'lig_tables/{metric}_{team.name}_{year}_{value}.html', "w") as f:
        f.write(html + text)
    return True


def get_season_table(data: list, seasons: list):
    year = data[2]
    for s in seasons:
        if s.get_season_number() == year:
            table = s.show_league_table()
    return table


def champions(seasons):
    champ_list = [s.champion for s in seasons]
    count = pd.Series(champ_list).value_counts()
    df = count.to_frame('# of Championships')
    html = df.to_html(col_space=100, justify='center')
    with open(f'lig_tables/all_champions.html', "w") as f:
        f.write(html)


def h2h(match_list):
    df = pd.DataFrame(columns=['Team', 'Games', 'Wins', 'Draws',
                               'Losses', 'Goals Scored', 'Goals Allowed', 'Difference'])
    t_matches = len(match_list)
    t1 = match_list[0]._home_team
    t2 = match_list[0]._away_team
    t1_win = 0
    t1_draw = 0
    t1_loss = 0
    t1_goals_scored = 0
    t1_goals_allowed = 0
    for m in match_list:
        if m._home_team == t1:
            t1_goals_scored += m._score[0]
            t1_goals_allowed += m._score[1]
            if m._winner == 'home':
                t1_win += 1
            elif m._winner == 'away':
                t1_loss += 1
            else:
                t1_draw += 1
        if m._away_team == t1:
            t1_goals_scored += m._score[1]
            t1_goals_allowed += m._score[0]
            if m._winner == 'away':
                t1_win += 1
            elif m._winner == 'home':
                t1_loss += 1
            else:
                t1_draw += 1

    d1 = {
        'Team': t1.name,
        'Games': t_matches,
        'Wins': t1_win,
        'Draws': t1_draw,
        'Losses': t1_loss,
        'Goals Scored': t1_goals_scored,
        'Goals Allowed': t1_goals_allowed,
        'Difference': t1_goals_scored - t1_goals_allowed
    }
    d2 = {
        'Team': t2.name,
        'Games': t_matches,
        'Wins': t1_loss,
        'Draws': t1_draw,
        'Losses': t1_win,
        'Goals Scored': t1_goals_allowed,
        'Goals Allowed': t1_goals_scored,
        'Difference': t1_goals_allowed - t1_goals_scored
    }
    df1 = pd.DataFrame(d1, index=[0])
    df2 = pd.DataFrame(d2, index=[1])
    df = pd.concat([df, df1, df2], ignore_index=True)
    df.sort_values(by=['Wins', 'Difference', 'Goals Scored'],
                   inplace=True, ascending=False, ignore_index=True)
    html = df.to_html(index=False, col_space=85, justify='center')
    with open(f'lig_tables/H2H_{t1}_{t2}.html', "w") as f:
        f.write(html)
