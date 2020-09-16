import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter
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

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.bar(monthly_totals.index, monthly_totals.values, width=30,
       color=sns.color_palette("Blues_d")[3])


plt.xlabel('')
plt.ylabel('Total Rainfall (mm)')

plt.savefig('rainfall.pdf')
