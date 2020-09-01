import os
import pandas as pd
from glob import glob


filenames = glob('data/TH-PC*.csv')

for filename in filenames:

    determinand_ids = ['0076', '0077', '0085', '0117', '9901', '9924']

    df = pd.read_csv(filename, dtype={'determinand_id': str})

    for d_id in determinand_ids:

        tmp_df = df.loc[lambda df: df['determinand_id'] == d_id]

        out_name = '{}_{}.csv'.format(os.path.splitext(filename)[0], d_id)

        if len(tmp_df['sample_date_time']) > 0:
            tmp_df.to_csv(out_name, index=False)
        else:
            print('No data in', out_name, 'for determinand_id', d_id)
