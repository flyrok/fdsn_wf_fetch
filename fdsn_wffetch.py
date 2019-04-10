#!/usr/bin/env python3

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.core import AttribDict
import argparse
from os.path import isdir
from sys import exit

progname='fdsn_wffetch.py';
__version_info__ = ('2019','04','01','0.01')
__version__ = '-'.join(__version_info__)

def remove_resp(stream,debug):
    if debug > 0:
        print("... detrending stream")
    stream.detrend(type='linear');
    if debug > 0:
        print("... removing responses")
    stream.remove_response(output="VEL")
    return(stream)

def write_sac(stream,sac_info,inv,suffix,debug):
    for tr in stream:
        chan_info=inv.get_channel_metadata(tr.id)
        tr.stats.sac=AttribDict()
        tr.stats.sac.stla=chan_info['latitude']
        tr.stats.sac.stlo=chan_info['longitude']
        tr.stats.sac.stel=chan_info['elevation']
        tr.stats.sac.stdp=chan_info['local_depth']
        tr.stats.sac.cmpaz=chan_info['azimuth']
        tr.stats.sac.cmpinc=chan_info['dip']
        khole=float(tr.stats.starttime-sac_info['otime'])
        tr.stats.sac.b=khole
        tr.stats.sac.o=0.0

        #tr.stats.sac.o=float(tr.stats.starttime-sac_info['otime'])
        tr.stats.sac.evlo=sac_info['evlo']
        tr.stats.sac.evla=sac_info['evla']
        tr.stats.sac.evdp=sac_info['evdp']
        tr.stats.sac.evel=sac_info['evel']
        tr.stats.sac.khole=tr.stats.location
        t=tr.stats.starttime.strftime('%Y%j%H%M%S')
        #outfile=sac_info['outdir']+"/"+tr.id+"."+t+suffix
        outfile=sac_info['outdir']+"/"+sac_info['evid']+"."+tr.id+suffix
        if debug > 0:
            print("*** writing files: ",outfile)
        tr.write(filename=outfile,format='SAC')

def write_mseed(stream,suffix,debug):
    for tr in stream:
        t=tr.stats.starttime.strftime('%Y%j%H%M%S')
        outfile=tr.id+"."+t+suffix
        tr.write(filename=outfile,format='MSEED')

def main():
    # Command line parsing
    parser = argparse.ArgumentParser(prog=progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=
            'grab waveform data for a station and output in some format')

    parser.add_argument("-t","--start_time", type=str,
        required=True, help="reference start time in iso-format e.g. 2019001T00:00, set to SAC O")

    parser.add_argument("-b","--begin", type=float,
        required=True, help="number of seconds to start record relative to start_time (e.g. 60)")

    parser.add_argument("-e","--end", type=float,
        required=True, help="number of seconds to end record relative to start_time (e.g. 120)")

    parser.add_argument("-n","--net", type=str,
        required=True, help="net code")

    parser.add_argument("-s","--sta", type=str,
        required=True, help="sta code")

    parser.add_argument("-l","--loc", type=str,default="*",
        required=False, help="loc code, wild cards ok, default: *")

    parser.add_argument("-c","--chan", type=str,default="*",
        required=False, help="chan codes, wild cards ok default: *")

    parser.add_argument("-r","--resp", action="store_true",default=False,
        required=False, help="remove response, default: False")

    parser.add_argument("-m","--mseed", action="store_true",default=False,
        required=False, help="Store in mseed instead of sac: False")

    parser.add_argument("--evlo", type=float,required=False, default=0.0,
        help="event longitude, for sac output")

    parser.add_argument("--evla", type=float,required=False, default=0.0,
        help="event latitude, for sac output")

    parser.add_argument("--evel", type=float,required=False, default=0.0,
        help="event elevation, for sac output")

    parser.add_argument("--evdp", type=float,required=False, default=0.0,
        help="event depth, for sac output")

    parser.add_argument("-o", "--outdir", type=str,required=False, default="./",
        help="output dir for waveforms. must exist or error")

    parser.add_argument( "--evid", type=str,required=False, default="evid",
        help="evid number added to output filename")

    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")

    parser.add_argument('--version', action='version',
                    version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()

    startt= UTCDateTime(args.start_time)-args.begin
    endt= UTCDateTime(args.start_time)+args.end
    net=args.net
    sta=args.sta
    loc=args.loc
    chan=args.chan
    do_resp=args.resp
    do_mseed=args.mseed
    debug=args.verbose
    sac_info={'otime':UTCDateTime(args.start_time),
        'evlo':args.evlo,'evla':args.evla,'evdp':args.evdp,'evel':args.evel,
        'outdir':args.outdir,'evid':args.evid}

    if debug > 0:
        print("begin: ",startt)
        print("end: ",endt)
        print("net: ",net)
        print("sta: ",sta)
        print("loc: ",loc)
        print("chan: ",chan)
        print("do_mseed:",do_mseed)
        print("do_resp: ",do_resp)
        print("outdir: ",args.outdir)
        print("sac_info:",sac_info)

    if not isdir(args.outdir):
        print(args.outdir," doesn't exist, exiting")
        exit(0)

    client = Client(timeout=240,base_url="http://service.iris.edu")
    if debug > 0:
        print("... getting waveform data")
    stream=client.get_waveforms(net,sta,loc,chan,startt,endt,attach_response=do_resp)

    if debug > 0:
        print(stream)

    if do_resp:
        stream=remove_resp(stream,debug)

    if do_mseed == True:
        suffix='m'
        write_mseed(stream,suffix,debug)

    if do_mseed == False :
        inv=client.get_stations(network=net,station=sta,starttime=startt,endtime=endt,level='channel')
        suffix=".sac"
        write_sac(stream,sac_info,inv,suffix,debug)

if __name__ == '__main__':
    main()

