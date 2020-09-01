import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar
from datetime import datetime
from glob import glob
import re

LUT = {'TH-PCNR0012': 'Chess above Chesham',
 'TH-PCNR0013': 'Chess above Colne',
 'TH-PCNR0014': 'Chess at Bois Mill, Chesham',
 'TH-PCNR0015': 'Chess at Chenies',
 'TH-PCNR0019': 'Chess at Road Bridge, Latimer',
 'TH-PCNR0020': 'Chess at Solesbridge Lane, Chorleywood',
 'TH-PCNR0145': 'Chess above Valley Farm Ford',
 'TH-PCNR0207': 'Old River Chess at Latimer Park Farm'}


dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')

for det_file in glob('../data/TH-PCNR*_*.csv'):

    det = pd.read_csv(det_file, parse_dates=['sample_date_time'], date_parser=dateparse)

    sample_id = re.search('TH-PCNR[\d]+', det_file).group()
    out_name = re.search('TH-PCNR[\d]+_[\d]+', det_file).group()
    title = LUT[sample_id]

    det_series=pd.Series(data=det['value'].values, index=det['sample_date_time'])

    daily_det = det_series.groupby(det_series.index.date).mean()
    det_days = sorted(list(set(det_series.index.date)))

    plt.gca().set_ylabel('{} ({})'.format(det['determinand_name'][0], det['unit'][0]))

    plt.plot(det_days, daily_det.values)

    plt.title(title)

    plt.savefig('{}-determinand.png'.format(out_name))
    plt.clf()
