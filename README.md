### Live Data

#### Gauges being processed

- Chesham: 2852TH-level-stage-i-15_min-mASD
- Rickmansworth: 2859TH-level-downstage-i-15_min-mASD
- Rickmansworth: 2859TH-level-stage-i-15_min-mASD
- Unnamed: 278744TP-rainfall-tipping_bucket_raingauge-t-15_min-mm

- Only run `rainfall-archive.py` via driving scripts `archive-run.sh` or `borehole-getter.sh`, but local paths need to be updated
- `update-data.py` should be run once per day, ideally in the middle of the night to capture complete daily telemetry
- The code backs up the json data daily, but does no content testing to ensure the backup is valid

### Borehole Data

#### Gauges being processed

- SP90_64-level-groundwater-i-1_h-mAOD
- SP90_56-level-groundwater-i-1_h-mAOD

- There is currently no live data coming in from our boreholes, so there is no code to do daily updates.
- Run `borehole-getter.sh` (after local paths have been updated) to grab all the data we have access to, which amounts to approximately the last year.

### Daily Flow Data

#### Gauge being processed

- 2859TH (Rickmansworth)
  - Unique ID: b0a28c3c-b5dc-4a94-a661-2ef0639049c7-flow-m-86400-m3s-qualified

- `get-hydrology-data.py`, driven by `hydrology-getter.sh`, downloads all of the daily flow data since 1/1/2020 to the present, removing any missing data rows.

### Requirements

- python 3.6 or greater
- requests==2.23.0
- tqdm==4.48.0
