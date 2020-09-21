import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar
import datetime
import re

LUT = {'TH-PCNR0012': 'Chess above Chesham',
 'TH-PCNR0013': 'Chess above Colne',
 'TH-PCNR0014': 'Chess at Bois Mill, Chesham',
 'TH-PCNR0015': 'Chess at Chenies',
 'TH-PCNR0019': 'Chess at Road Bridge, Latimer',
 'TH-PCNR0020': 'Chess at Solesbridge Lane, Chorleywood',
 'TH-PCNR0145': 'Chess above Valley Farm Ford',
 'TH-PCNR0207': 'Old River Chess at Latimer Park Farm'}


dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')

det_files = ['../data/TH-PCNR0012_0117.csv', '../data/TH-PCNR0014_0117.csv',
              '../data/TH-PCNR0013_0117.csv']

for i, det_file in enumerate(det_files, start=1):

    det = pd.read_csv(det_file, parse_dates=['sample_date_time'],
                      date_parser=dateparse)

    sample_id = re.search('TH-PCNR[\d]+', det_file).group()
    out_name = re.search('TH-PCNR[\d]+_[\d]+', det_file).group()
    title = LUT[sample_id]

    det_series=pd.Series(data=det['value'].values,
                         index=det['sample_date_time'])

    daily_det = det_series.groupby(det_series.index.date).mean()
    det_days = sorted(list(set(det_series.index.date)))

    # 2012-11-28 is the last day of data for nitrate at TH-PCNR0012
    det_days = [d for d in det_days if d <= datetime.date(2012, 11, 28)]

    plt.gca().set_ylabel('{} ({})'.format(det['determinand_name'][0],
                                          det['unit'][0]))

    sns.lineplot(x=det_days, y=daily_det[det_days].values, label=title,
                 color=sns.color_palette("icefire", n_colors=20)[i**2])

plt.legend()
plt.tight_layout()
plt.savefig('nitrate.png')
