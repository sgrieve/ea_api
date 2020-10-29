import numpy as np
import pandas as pd
from scipy import ndimage, spatial
import fiona
from shapely.geometry import shape, MultiPoint, LineString, mapping
from shapely.ops import nearest_points
from fiona.crs import from_epsg
from glob import glob

schema = {
    'geometry': 'LineString',
    'properties': {'name': 'str', 'flow': 'float'},
}

crs = from_epsg(27700)


with fiona.open('chess.shp') as c:
    chess = shape(c[0]['geometry'])[0]

chess_pts = MultiPoint(chess._get_coords())

filenames = glob('*-*-*.shp')

for filename in filenames:
    counter = 0
    with fiona.open('{}-line.shp'.format(filename[:-4]), 'w', 'ESRI Shapefile', schema, crs=crs) as w:

        with fiona.open(filename) as s:
            for s_ in s:
                sample = shape(s_['geometry'])
                flow = s_['properties']['flow']
                name = s_['properties']['name'].strip()

                nearest = nearest_points(sample, chess_pts)

                tmp_pts = []

                for c in chess_pts[counter:]:

                    tmp_pts.append(c)
                    if c == nearest[1]:
                        counter = list(chess_pts).index(c)
                        break

                if len(tmp_pts) > 1 and flow > 0. and flow < 1000. and flow != 9999.:
                    segment = LineString(tmp_pts)
                    w.write({
                        'geometry': mapping(segment),
                        'properties': {'name': name, 'flow': flow},
                    })
