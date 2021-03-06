## fdsn_wf_fetch ##

ObsPy wrapper script to pull seismic data from IRIS FDSN server (default server), remove
response,  and save it as SAC or Miniseed.

Event info can be passed on the command line to fill out sac headers.

### Purpose/Scope ###

This script is useful for pulling single event, single station, multi-channel data
from IRIS, saving as SAC, and populating the SAC headers. 
If event info is given on the command line, then it will be written to the SAC headers, 
otherwise only the SAC station and channel fields are populated.

Current implementation is to only to request one station at a time. This will likely change.

An intended use is to loop through the output of 
`fdsn_station_info.py` (https://github.com/flyrok/fdsn_station_info)
and pass the Net,Station,Chan,Loc info to `fdsn_wf_fetch.py`.

## Install ##

Clone source package  
`git clone http://github.com/flyrok/fdsn_wf_fetch`  

Install with pip after download  
`pip install .`  

Or install directly from github  
`pip install git+https://github.com/flyrok/fdsn_wf_fetch#egg=fdsn_wf_fetch`  

Or just put the executable on your PATH and call directly  
`./fdsn_wf_fetch.py`

## Python Dependencies ##

python>=3.6  (script uses f-strings)  
obspy (https://github.com/obspy/obspy/wiki)
-- without this, nothing will work


## Usage ##

To see help:  
`fdsn_wf_fetch.py --help`    

To see version:  
`fdsn_wf_fetch.py --version`    

To grab 60 seconds of BH channel data for station HRV, remove response
and save as SAC files (a default pre-filter is applied):  
`fdsn_wf_fetch.py -t 2019001T00:00 -b 0 -e 60 -n IU -s HRV -c "BH?" -r`    

To grab 60 seconds of BH channel data for station HRV, remove response,  
but DON'T apply pre-filter, and save as SAC files:  
`fdsn_wf_fetch.py -t 2019001T00:00 -b 0 -e 60 -n IU -s HRV -c "BH?" -r --nofilt`    

To grab 60 seconds of BH channel data for station HRV, remove response,  
apply a user defined pre-filter, and save as SAC files:  
`fdsn_wf_fetch.py -t 2019001T00:00 -b 0 -e 60 -n IU -s HRV -c "BH?" -r --filter 0.002  0.003 36 38`    




