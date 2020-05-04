from datetime import datetime, timedelta
from glob import glob

for g in glob('data/*.csv'):
    dates = []
    with open(g) as f:
        f.readline()
        data = f.readlines()
        for d in data:
            tmp = datetime.strptime(d.split(',')[0], '%Y-%m-%dT%H:%M:%S')
            dates.append(tmp)


    previous = dates[0]
    for current in dates[1:]:
        diff = (current - previous).seconds / 60
        if diff != 15.0:
            print(current, previous, g)
        previous = current
