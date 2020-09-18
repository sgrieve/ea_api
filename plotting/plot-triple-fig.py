import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')

rain = pd.read_csv('../data/rainfall_chenies.csv',
                    parse_dates=['date'], date_parser=dateparse)

rain_series = pd.Series(data=rain['measurement'].values, index=rain['date'])

# Data has nans represented as ---
rain_series = rain_series.replace('---', np.nan)
rain_series = rain_series.astype(float)

# M groups by month and S records the date as the start of the month, so each
# monthly sum is stored as the first of the month
monthly_totals = rain_series.groupby(pd.Grouper(freq="MS")).sum()

fig, ax = plt.subplots(3, 1)

ax = plt.subplot(3, 1, 1)

ax.bar(monthly_totals.index, monthly_totals.values, width=30,
       color='tab:blue')


plt.xlabel('')
plt.ylabel('Total Rainfall (mm)')
ax.get_xaxis().set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)


ax = plt.subplot(3, 1, 2)

gw_file = '../data/ashley-green-gw-data.csv'

gw = pd.read_csv(gw_file, parse_dates=['date'], date_parser=dateparse)

gw_series=pd.Series(data=gw['measurement'].values, index=gw['date'])

daily_gw = gw_series.groupby(gw_series.index.date).mean()
gw_days = sorted(list(set(gw_series.index.date)))

ax.set_ylabel('Groundwater level (mAOD)')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax.get_xaxis().set_visible(False)

ax.plot(gw_days, daily_gw.values, color='tab:blue')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)


ax = plt.subplot(3, 1, 3)

flow = pd.read_csv('../data/rickmansworth-daily-flow.csv',
                    parse_dates=['dateTime'], date_parser=dateparse)

flow_series=pd.Series(data=flow['value'].values, index=flow['dateTime'])

daily_flow = flow_series.groupby(flow_series.index.date).sum()
flow_days = sorted(list(set(flow_series.index.date)))

ax.plot(flow_days, daily_flow.values, color='tab:blue')

ax.set_ylabel('River Flow (cumecs)')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.savefig('triple.png')
