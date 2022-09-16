"""
Author: Hongyuan Qiu
Time: 09/16/2022
"""
from datetime import datetime

import pandas as pd
from pytrends.request import TrendReq

from project_constants import GEO, COULD_NOT_GET_DATA, SUCCESSFUL_MESSAGE,\
    ASK_USER_FOR_SEARCH_RANGE, WRONG_INPUT


def collect_bitcoin_trends(
        search_range: str = '',
        start_time: str = "2015-01-01", kw: str = "Bitcoin"
) -> pd.DataFrame:
    """
    Get bitcoin daily data by using pytrends API, remove the duplicated data,
    and then save the data into a csv file.

    :param search_range: Two letter country abbreviation
    :param start_time: Date to start from in string, default "2015-01-01"
    :param kw: keyword to get data for, default Bitcoin
    :return: a pandas DataFrame object
    """
    now = datetime.now()
    start_y, start_m, start_d = [int(item) for item in start_time.split("-")]
    my_pytrends = TrendReq(hl='en-US', tz=360, timeout=(5, 7))
    df = my_pytrends.get_historical_interest(
        [kw], year_start=start_y, month_start=start_m, day_start=start_d,
        year_end=now.year, month_end=now.month, day_end=now.day,
        geo=search_range, frequency="daily"
    )

    if len(df) == 0:
        print(COULD_NOT_GET_DATA)
        return df

    new_df = df[~df.index.duplicated(keep='first')]
    new_df.to_csv('bitcoin_daily_trends_data.csv')

    return new_df
# End collect_bitcoin_trends function


def generate_bitcoin_weekly_trends_data(daily_data: pd.DataFrame) -> None:
    """Generate a csv file of bitcoin weekly data

    :param daily_data: a pandas DataFrame object
    """
    daily_data_2 = daily_data.loc[:, ['Bitcoin']]
    daily_data_2['Date'] = pd.to_datetime(daily_data.index, format="%Y%m%d")
    logic = {
        'Bitcoin': 'mean',
        'Date': 'first',
    }
    weekly_data = daily_data_2.groupby(
        [daily_data_2['Date'].dt.isocalendar().year,
         daily_data_2['Date'].dt.isocalendar().week]).agg(logic)
    weekly_data.set_index('Date', inplace=True)
    weekly_data['Bitcoin'] = weekly_data['Bitcoin'].map(
        lambda x: '{0:.2f}'.format(x))
    weekly_data.to_csv('bitcoin_weekly_trends_data.csv')
# End generate_bitcoin_weekly_trends_data function


if __name__ == "__main__":
    searching_range = input(ASK_USER_FOR_SEARCH_RANGE)
    try:
        bc_sr = GEO[searching_range]
    except KeyError:
        print(WRONG_INPUT)
    else:
        bitcoin_daily_data = collect_bitcoin_trends(search_range=bc_sr)
        if len(bitcoin_daily_data) != 0:
            generate_bitcoin_weekly_trends_data(bitcoin_daily_data)
            print(SUCCESSFUL_MESSAGE)
