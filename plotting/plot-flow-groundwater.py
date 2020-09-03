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

for gw_file in glob('../data/*gw-data.csv'):

    if 'ashley' in gw_file:
        title = 'Ashley Green'
    else:
        title = 'Wayside'

    gw = pd.read_csv(gw_file, parse_dates=['date'], date_parser=dateparse)

    gw_series=pd.Series(data=gw['measurement'].values, index=gw['date'])

    daily_gw = gw_series.groupby(gw_series.index.date).mean()
    gw_days = sorted(list(set(gw_series.index.date)))

    daily_flow = flow_series.groupby(flow_series.index.date).sum()
    flow_days = sorted(list(set(flow_series.index.date)))


    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.set_ylabel('Groundwater level (mAOD)', color='tab:blue')
    ax2.set_ylabel('River Flow (cumecs)')


    ax1.plot(gw_days, daily_gw.values)
    ax2.plot(flow_days, daily_flow.values, color='k')

    plt.title(title)

    plt.savefig('{}-groundwater-flow-{}.png'.format(title.replace(' ', '-'), 'rickmansworth'))
    plt.clf()
