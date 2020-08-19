import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')

rain = pd.read_csv('../data/278744TP-rainfall-tipping_bucket_raingauge-t-15_min-mm.csv',
                    parse_dates=['date'], date_parser=dateparse)

rain_series=pd.Series(data=rain['measurement'].values, index=rain['date'])

monthly_totals = rain_series.groupby(rain_series.index.month).sum()

# Get month names (switch to month_abbr for month abbreviations)
monthly_totals.index = [calendar.month_name[i] for i in monthly_totals.index]

ax = sns.barplot(x=monthly_totals.index, y=monthly_totals.values,
                 saturation=0.8, color=sns.color_palette("Blues_d")[3])


sns.despine()

plt.xlabel('')
plt.ylabel('Total Rainfall (mm)')

plt.savefig('rainfall.png')
