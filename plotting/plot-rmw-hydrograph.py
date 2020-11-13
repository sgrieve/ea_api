import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')

flow = pd.read_csv('../data/rickmansworth-daily-flow.csv',
                    parse_dates=['dateTime'], date_parser=dateparse)

flow_series=pd.Series(data=flow['value'].values, index=flow['dateTime'])

daily_flow = flow_series.groupby(flow_series.index.dayofyear).mean()
flow_days = sorted(list(set(flow_series.index.dayofyear)))

ax = plt.gca()

ax.plot(flow_days[:365], daily_flow[:365].values, color='tab:blue')

ax.set_ylabel('Mean Daily River Flow (cumecs)')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

plt.savefig('rickmansworth-20-yr-daily-flow.png')
