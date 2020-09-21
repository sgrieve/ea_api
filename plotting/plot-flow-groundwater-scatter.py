import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar
from datetime import datetime
from glob import glob

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')

flow = pd.read_csv('../data/rickmansworth-daily-flow.csv',
                    parse_dates=['dateTime'], date_parser=dateparse)

flow_series=pd.Series(data=flow['value'].values, index=flow['dateTime'])

gw_file = '../data/ashley-green-gw-data.csv'

gw = pd.read_csv(gw_file, parse_dates=['date'], date_parser=dateparse)

gw_series=pd.Series(data=gw['measurement'].values, index=gw['date'])

daily_gw = gw_series.groupby(gw_series.index.date).mean()
gw_days = sorted(list(set(gw_series.index.date)))

daily_flow = flow_series.groupby(flow_series.index.date).sum()
flow_days = sorted(list(set(flow_series.index.date)))

ax = sns.scatterplot(x=daily_gw[gw_days], y=daily_flow[gw_days], size=5,
                     linewidth=0.1, alpha=1, color='tab:blue', edgecolor='k',
                     legend=False)

ax.set_xlabel('Groundwater level (mAOD)')
ax.set_ylabel('River Flow (cumecs)')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('groundwater-flow-scatter.png')
