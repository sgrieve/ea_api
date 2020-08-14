import os
import sys
import requests

units_LUT = {
'http://environment.data.gov.uk/water-quality/def/units/0205': 'mg/l',
'http://environment.data.gov.uk/water-quality/def/units/0349': 'cel',
'http://environment.data.gov.uk/water-quality/def/units/0906': 'percent',
'http://environment.data.gov.uk/water-quality/def/units/0586': 'us/cm'
}

location_id = 'TH-PCNR0013'  # sys.argv[1]
base_path = '/Users/stuart/ea_api/data'  # sys.argv[2]

csv_path = os.path.join(base_path, '{}.csv'.format(location_id))

root = 'http://environment.data.gov.uk/water-quality'

# Call the API to get the new data
r = requests.get('{}/id/sampling-point/{}/samples?_limit=1000'.format(root, location_id))

location_data = r.json()

sample_ids = []

determinand_ids_to_log = ['0076', '0077', '0085', '0117', '9901', '9924']

for sample in location_data['items']:
    sample_ids.append(sample['@id'])

out_rows = []

# use each sample id url to get the required determinands
for sample_id in sample_ids:
    r = requests.get(sample_id).json()
    for item in r['items']:
        sample_date_time = item['sampleDateTime']
        lat = item['samplingPoint']['lat']
        long = item['samplingPoint']['long']
        if isinstance(item['measurement'], list):
            for inner_item in item['measurement']:
                if inner_item['determinand']['notation'] in determinand_ids_to_log:
                    unit_url = inner_item['determinand']['unit']['@id']
                    value = inner_item['result']

                    out_rows.append('{},{},{},{},{},{},{}\n'.format(lat,long,sample_date_time,inner_item['determinand']['notation'],
                          inner_item['determinand']['label'],value, units_LUT[unit_url]))
        else:
            if item['measurement']['determinand']['notation'] in determinand_ids_to_log:
                unit_url = item['measurement']['determinand']['unit']['@id']
                value = item['measurement']['result']

                out_rows.append('{},{},{},{},{},{},{}\n'.format(lat,long,sample_date_time,item['measurement']['determinand']['notation'],
                      item['measurement']['determinand']['label'],value, units_LUT[unit_url]))


if os.path.isfile(csv_path):
    # Back up previous data, overwriting previous backup
    os.replace(csv_path, '{}.bak'.format(csv_path))

with open(csv_path, 'w') as w:
    w.write('lat,long,sample_date_time,determinand_id,determinand_name,value,unit\n')
    for row in out_rows:
        w.write('{}'.format(row))
