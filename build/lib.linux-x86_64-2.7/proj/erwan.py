"""Module for overlapping game and player
"""
# -*- coding: UTF-8 -*-
import os
import pandas as pd


def for_test():
    """for test the test
    """
    return 'success'


def load_data(data_path):
    """ load data
    """
    path = data_path
    dirs = os.listdir(path)
    first = False
    for files in dirs:
        if first is False:
            dataframe = pd.read_csv(path + files, usecols=[2, 3], header=None)
            first = True
        else:
            df_temp = pd.read_csv(path + files, usecols=[2, 3], header=None)
            dataframe = dataframe.append(df_temp)
    return dataframe


def clean_data(dataframe):
    """ clean data
    """
    dataframe.columns = ['player', 'game']
    dataframe = dataframe.drop_duplicates(['player', 'game'])
    return dataframe


def overlapping(dataframe):
    """ make tot_x_y
    """
    df_merge = pd.merge(dataframe, dataframe, how='left', on=['player'])
    df_crosstab = pd.crosstab(df_merge['game_y'], df_merge['game_x'])
    result = df_crosstab.stack()
    result.name = 'tot_x_y'
    result = result.reset_index()
    number_of_player = list(dataframe.game.value_counts().values)
    result['tot_x'] = number_of_player * len(number_of_player)
    return result


def layout(dataframe):
    """cleaning and layout
    """
    dataframe = dataframe[dataframe['game_y'] != dataframe['game_x']]
    dataframe = dataframe[['game_x', 'game_y', 'tot_x', 'tot_x_y']]
    dataframe = dataframe[dataframe['tot_x_y'] != 0]
    dataframe = dataframe.sort('game_x')
    dataframe = dataframe.reset_index(drop=True)
    dataframe.insert(2, 'overlapping', 100 * dataframe.tot_x_y /
                     dataframe.tot_x)
    return dataframe


def make_csv(dataframe, filename):
    """export to csv
    """
    dataframe.to_csv(filename + '.csv', index=False)
    print 'csv created'


if __name__ == '__main__':
    """For introspections purpose to quickly get this functions on ipython
    with data
    """
    import proj
    datapath = os.path.dirname(os.path.abspath(proj.__file__)) + '/data'
    df01 = pd.read_csv('{}/20101101.over_player_day.csv'.format(datapath),
                       usecols=[2, 3],
                       header=None)
    df02 = pd.read_csv('{}/20101102.over_player_day.csv'.format(datapath),
                       usecols=[2, 3],
                       header=None)
    df = df01.append(df02)
