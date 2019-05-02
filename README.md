## fdsn_wf_fetch ##

Pull seismic data from IRIS FDSN server (default server) and save it as
sac or miniseed.

Event info can be passed on the command line to fill out sac headers.

### Purpose/Scope ###

This script is useful for pulling single event, multi-channel data
from IRIS and saving as SAC. If event info is given on the
command line, then it will be written to the SAC headers.

## Install ##

Clone source package
`git clone ...`  

Install with pip after download 
`pip install .`  

Or install directly from github
`pip install git+https://github.com/flyrok/fdsn_wf_fetch#egg=fdsn_wf_fetch`  

## Python Dependencies ##

python>=3.6   
obspy  

## Usage ##

to see help:  
`fdsn_wf_fetch.py --help`    

To see version:  
`fdsn_wf_fetch.py --version`    

To grab 60 seconds of BH channel data for station HRV, remove response
and save as SAC files:  
`fdsn_wf_fetch.py -t 2019001T00:00 -b 0 -e 60 -n UI -s HRV -c "BH?" -r`    


