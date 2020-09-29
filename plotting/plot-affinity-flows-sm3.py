import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar
import datetime
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates


LUT = {'Site4': 'Downstream of meades water garden',
       'Site7': 'Pump lane (downstream of Lords Mill)',
       'Site12': 'Bois Mill main channel'}

dateparse = lambda x: datetime.datetime.strptime(x, '%d/%m/%Y')

headers = ['Site4', 'Site7', 'Site12']

flow = pd.read_csv('../data/Affinity-water-flows-Storymap-3.csv', parse_dates=['date'], date_parser=dateparse)

fig, ax = plt.subplots(3, 1)

for i in range(3):

    flow_series=pd.Series(data=flow[headers[i]].values, index=flow['date'])

    daily_flow = flow_series.groupby(flow_series.index.date).mean()
    flow_days = sorted(list(set(flow_series.index.date)))

    ax = plt.subplot(3, 1, i + 1)

    sns.lineplot(x=flow_days, y=daily_flow.values, color='tab:blue')

    plt.title(LUT[headers[i]])

    if i == 0:
        ax.get_xaxis().set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

    if i == 1:
        ax.set_ylabel('Flow (cumecs)\n')
        ax.get_xaxis().set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)


    if i == 2:
        plt.xlabel('')
        ax.get_xaxis().set_visible(True)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # plt.legend(loc=3)
    # plt.ylim(3, 15)
plt.tight_layout()
plt.savefig('affinity-flows.png')
