import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar
from datetime import datetime
from glob import glob

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')

rain = pd.read_csv('../data/278744TP-rainfall-tipping_bucket_raingauge-t-15_min-mm.csv',
                    parse_dates=['date'], date_parser=dateparse)

rain_series=pd.Series(data=rain['measurement'].values, index=rain['date'])

for gw_file in glob('../data/*gw-data.csv'):

    if 'ashley' in gw_file:
        title = 'Ashley Green'
    else:
        title = 'Wayside'

    gw = pd.read_csv(gw_file, parse_dates=['date'], date_parser=dateparse)

    gw_series=pd.Series(data=gw['measurement'].values, index=gw['date'])

    daily_gw = gw_series.groupby(gw_series.index.date).mean()
    gw_days = sorted(list(set(gw_series.index.date)))

    daily_rain = rain_series.groupby(rain_series.index.date).sum()
    rain_days = sorted(list(set(rain_series.index.date)))


    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.set_ylabel('Groundwater level (mAOD)')
    ax2.set_ylabel('Rainfall (mm)')


    ax1.plot(gw_days, daily_gw.values)
    ax2.bar(rain_days, daily_rain.values)

    ax1.set_ylim(min(daily_gw.values) - 10, max(daily_gw.values)+5)

    plt.title(title)

    plt.savefig('{}-groundwater-rainfall.png'.format(title.replace(' ', '-')))
    plt.clf()
