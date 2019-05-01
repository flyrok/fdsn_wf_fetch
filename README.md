## fdsn_wf_fetch##

Pull waveforms from IRIS FDSN server (default server) and save them as
sac or miniseed format.

Event info can be passed on the command line to fill out sac headers.


## Install ##

Clone source package

**git clone ...  **  

Install in editable mode  

**pip install -e .**  

Install to system python  

**pip install .**  

Or install from github

**pip install git+https://github.com/flyrok/fdsn_wf_fetch#egg=fdsn_wf_fetch**

## Python Dependencies ##

python>=3.6 
argparse  
obspy

## Usage ##

to see help:  
**fdsn_wf_fetch.py --help**    

To see version:  
**fdsn_wf_fetch.py --version**    

To requestion BH channels for station:  
**fdsn_wf_fetch.py -b 2019001T00:00 -e 2019100T00:00 --lon -71.0 --lat 41.0 --radmin 1 --radmax 50 -r -c "BH*" -o test.csv**    


