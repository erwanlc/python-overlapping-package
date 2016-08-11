# -*- coding: UTF-8 -*-
# Copyright (C) 2016 Luis Arturo Belmar-Letelier <luis@zettafox.com>
""" Project skeleton for Zettafox Projects
"""

from datetime import datetime
import os
import pandas as pd

# from zettatools.logger import get_logger
# from zettatools.utils import duration

def get_data():
    """ Create data
    """
    return 'tons of data'


def clean_data(data):
    """ clean data
    """
    return data.upper()


def make_result(df, filename):
    """ write output result in filename
    """
    df.drop(['datetime', 'timestamp', 'score_value'], axis=1, inplace=True)
    df['player'] = df.player.str.upper()
    df.to_csv(filename)
    print '  {} Made'


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    # with data
    import proj
    datapath = os.path.dirname(os.path.abspath(proj.__file__)) + '/data'
    data = '{}/data.csv'.format(datapath)
    df = pd.read_csv(data)
    data = get_data()
    clean_data = clean_data(data)
    print 'df, data and clean_data made'
