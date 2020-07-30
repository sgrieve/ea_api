## River Chess Open Data

### Environment Agency Rainfall

Currently downloading:

- Chesham: 2852TH-level-stage-i-15_min-mASD
- Rickmansworth: 2859TH-level-downstage-i-15_min-mASD
- Rickmansworth: 2859TH-level-stage-i-15_min-mASD
- Unnamed: 278744TP-rainfall-tipping_bucket_raingauge-t-15_min-mm

Can scrape historic data for each of these sites going back to approx mid 2019, but cannot find historic data going back further than that.

Kate has emailed me some data for 2859TH that goes back to 2000.

### Environment Agency Boreholes

Cannot get recent borehole data from the Ashley Green Borehole(SP90_64): https://environment.data.gov.uk/flood-monitoring/id/stations/SP90_64.html But we can pull some data for the past year from the historic API. This can be done with `rainfall-archive.py`

We can see the data for Ashley Green as well as other boreholes in operation in the UK in this HESS paper: https://www.hydrol-earth-syst-sci.net/23/3233/2019/hess-23-3233-2019.pdf

Kate has emailed data for Ashley Green and some other boreholes running back to 1987. These are daily data rather than the 15 min or 1 hr resolution we can get (sporadically) from the current APIs.

### Environment Agency Fish and Ecology

At this page I can download Fish and Ecology data that is tagged to the Chess: https://environment.data.gov.uk/ecology-fish/

- We have data for `Scotsbridge Mill` which has an ID of `10437` and is tagged as having the Chess as a parent site.
- These sites have extensive data on Fish abundance - need to consider what is relevant
- Data spans 1987 to 2019 across a range of sites
- `Scotsbridge Mill` spans 2017-2019
- Each measurement is geotagged with an Easting and Northing

No obvious API so will likely be a 1 off processing job for the historic data rather than a live update.

- Paul can advise on this

### Environment Agency Water Quality

Not sure if these data are of interest: https://environment.data.gov.uk/water-quality/view/doc/reference

Found data for a Chess associated sample point with data going back to 2000: https://environment.data.gov.uk/water-quality/view/sampling-point/TH-PCNR0013

Can grab this via the water quality API if we can identify all of the relevant sample stations.

- Kate to outline water quality narrative

Determinands to collect: 0076, 0077, 0085, 0117, 9901, 9924

See the IGS in the MS Teams file section to see the names of all of the sample locations.

### Riverfly

Seems to be data going back at least a decade for the River Chess. No API that I can see, but data is rarely updated? Can download all of the data to excel format from here: https://www.riverflies.org/open-data

- Need to identify what data we want to process out and how to include it in the story map

- Alan helps with narrative


### Earthwatch fresh water blitz

- Investigate this
- Source of Nitrate data


## Challenges/Questions

- What is the timeframe for the data we need?
- What is the temporal resolution we need?
- What preprocessing do we need to do for each dataset?
- How do we format the data for inclusion in the story map?
- Can the EA give us bulk data download for earlier than 2019?
  - Hydrology API may have longer term records? https://environment.data.gov.uk/hydrology/doc/reference
