import fiona
from shapely.geometry import mapping, Point, MultiPoint
import bng
from fiona.crs import from_epsg

def fix_flow(flow):

    '''
    Converts flows which can have the following values:
    - floats: a flow value in cumecs
    - NMF: indicates ponded water
    - Dry: indicates dry bed
    - -: a literal dash indicates missing data

    Into pure floating point values to support shapefile/dbf limits using the
    following LUT:

    - NMF = 0.0
    - Dry = 1000
    - - = 9999

    '''
    if flow.lower() == 'nmf':
        return 0.0
    elif flow.lower() == 'dry':
        return 1000.0
    elif flow.lower() == '-':
        return 9999.0
    else:
        return float(flow)


locations = {
    'site1':'SP 95228 01136',
    'site2':'SP 96072 02096',
    'site3':'SP 95819 01324',
    'site4':'SP 96068 01050',
    'site5a':'SP 96401 00644',
    'site6b':'SP 96518 00668',
    'site6c':'SP 96483 00715',
    'site7':'SP 97157 00334',
    'site8':'SP 97274 00191',
    'site8a':'SP 97268 00128',
    'site8b':'SP 97275 00136',
    'site8c':'SP 97268 00128',
    'site9':'SP 97723 00026',
    'site10':'SU 97608 99923',
    'site11':'SU 98464 99375',
    'site12':'SU 98481 99346'
    }

with open('inter-data-thinned.csv') as f:
    header = f.readline()
    data = f.readlines()

sites = header.split(',')[1:]

schema = {
    'geometry': 'Point',
    'properties': {'name': 'str', 'flow': 'float'},
}


crs = from_epsg(27700)

for row in data:

    flows = row.split(',')[1:]

    date = row.split(',')[0].replace('/', '-')

    with fiona.open('{}.shp'.format(date), 'w', 'ESRI Shapefile', schema, crs=crs) as c:
        for i, _ in enumerate(flows):

            pt = bng.to_osgb36(locations[sites[i].strip()].replace(' ', ''))

            c.write({
                'geometry': mapping(Point(pt)),
                'properties': {'name': sites[i], 'flow': fix_flow(flows[i])},
            })
