import os
import sys
import requests
import json
from collections import OrderedDict
from datetime import datetime, timedelta

measurement_id = sys.argv[1]
base_path = sys.argv[2]

json_path = os.path.join(base_path, '{}.json'.format(measurement_id))
csv_path = os.path.join(base_path, '{}.csv'.format(measurement_id))

if os.path.exists(json_path):
    with open(json_path) as f:
        data = json.load(f)
else:
    # create blank dict
    data = {}

start = datetime(2020, 1, 1)

n_days = (datetime.now() - start).days  # This is the number of days between today and 1st of Jan

for _ in range(n_days):

    url = 'http://environment.data.gov.uk/flood-monitoring/archive/readings-{}.csv'.format(start.strftime('%Y-%m-%d'))
    r = requests.get(url)


    # grab our day's rainfall data and add it to the master json
    lines = r.text.split('\n')
    for l in lines:
        if measurement_id in l:
            sample_time = datetime.strptime(l.split(',')[0], '%Y-%m-%dT%H:%M:%SZ')
            data[sample_time.isoformat()] = float(l.split(',')[2])

    start += timedelta(days=1)

# Write the data to a json file
with open(json_path, 'w') as f:
     f.write(json.dumps(data))

# Sort the json by date and write it to csv
sorted_dict = OrderedDict(sorted(data.items()))
with open(csv_path, 'w') as w:
    w.write('date,measurement\n')
    for date, measurement in sorted_dict.items():
        w.write('{},{}\n'.format(date, measurement))
