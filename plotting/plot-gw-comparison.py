import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')


fig, ax = plt.subplots(2, 1)


gw_files = ['../data/ashley-green-gw-data.csv', '../data/wayside-gw-data.csv']
titles = ['Ashley Green', 'Wayside']


for i in range(2):

    ax = plt.subplot(2, 1, i + 1)

    gw = pd.read_csv(gw_files[i], parse_dates=['date'], date_parser=dateparse)

    gw_series = pd.Series(data=gw['measurement'].values, index=gw['date'])

    daily_gw = gw_series.groupby(gw_series.index.date).mean()
    gw_days = sorted(list(set(gw_series.index.date)))

    if i == 0:
        ax.get_xaxis().set_visible(False)
        ax.spines['bottom'].set_visible(False)
    else:
        ax.spines['bottom'].set_visible(True)
        ax.set_ylabel('                                               Groundwater level (mAOD)')

    ax.plot(gw_days, daily_gw.values, color='tab:blue')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


    ax.spines['left'].set_visible(True)

    plt.title(titles[i])

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.tight_layout()

plt.savefig('gw_comparison.png')
