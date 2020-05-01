### Gauges being processed

Chesham: 2852TH-level-stage-i-15_min-mASD
Rickmansworth: 2859TH-level-downstage-i-15_min-mASD
Rickmansworth: 2859TH-level-stage-i-15_min-mASD
Unnamed: 278744TP-rainfall-tipping_bucket_raingauge-t-15_min-mm


### Notes

- Only run `rainfall-archive.py` if there is no existing csv and json file to update.
- `update-data.py` should be run once per day, ideally in the middle of the night to capture complete daily telemetry
- The code backs up the json data daily, but does no content testing to ensure the backup is valid

### Requirements

- python 3.6 or greater
- requests==2.23.0
