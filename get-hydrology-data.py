import os
import sys
import logging
import requests

measurement_id = sys.argv[1]
base_path = sys.argv[2]
shortname = sys.argv[3]

# Setting up our logfile
logging.basicConfig(filename=os.path.join(base_path, '{}.log'.format(shortname)),
                    level=logging.WARNING, format='%(levelname)s:%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

csv_path = os.path.join(base_path, '{}.csv'.format(shortname))

root = 'http://environment.data.gov.uk/hydrology'

# Call the API to get the new data
r = requests.get('{}/id/measures/{}/readings.csv?mineq-date=2000-01-01'.format(root, measurement_id))

# Removing missing data to make our lives easier
data = []
for row in r.text.splitlines():
    if 'Incomplete' in row:
        logging.warning('Incomplete data removed: {}'.format(row))
    else:
        s = row.split(',')
        data.append(('{},{},{},{},{},{}'.format(s[0], s[1].strip('Z'), s[2], s[3], s[4], s[5])))

if os.path.isfile(csv_path):
    # Back up previous data, overwriting previous backup
    os.replace(csv_path, '{}.bak'.format(csv_path))

with open(csv_path, 'w') as w:
    for row in data:
        w.write('{}\n'.format(row))
