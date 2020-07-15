import os, ROOT
import km3pipe as kp
import numpy as np
import matplotlib.dates as md
from domauto import da_classlib as dac

def make_plot_dirs( OUT_DIR ):
    print( OUT_DIR)
    RUN_DIR = OUT_DIR.split("/")[-1]
    DET_DIR = OUT_DIR[ :-len( RUN_DIR ) ] if RUN_DIR else OUT_DIR
    print(DET_DIR)
    if not os.path.isdir( DET_DIR ):
        os.mkdir( DET_DIR )
        print("Created directory {0}".format( DET_DIR ) )

    if len(OUT_DIR.split("/")[-1]) and not os.path.isdir( OUT_DIR ):
        os.mkdir( OUT_DIR )
        print("Created directory {0}".format( OUT_DIR ) )



def getruns( doms_dic ) :
    "sorted list of all runs with at least 1 live dom"
    
    r = set()
    for ( du, floor ), dominf in doms_dic.items() :
        r.update( dominf.live_runs )
        
    return sorted( r, key = lambda obj: obj.get_index() )



def get_detectors( detector_string,
                   sds ):

    if detector_string and detector_string[1:] == 'RCA':
        print("entered")
        #Get all xRCA detectors
        detectors = [ OID_to_DETID( det_name, sds ) for det_name in sds.detectors().OID.values if detector_string in det_name ]
    elif detector_string and detector_string[1:] != 'RCA':
        if detector_string not in sds.detectors().OID.values:
            #Return converted to DETID
            try:
                detector_string = OID_to_DETID( detector_string, sds )
            except:
                print( "ERROR: detector {0} not recognized...".format( detector_string ) )
                raise ValueError
        #Return DETID
        detectors = [ detector_string ]
    else:
        #Get all detectors
        detectors = [ OID_to_DETID( det_name, sds ) for det_name in sds.detectors().OID.values if 'RCA' in det_name ]
        
    return detectors
                
def process_jra_file( filename, det_id, runs_dic, doms_dic) :

    try:
        run = dac.Run( det_id, int( filename.split("_")[-2] ) )
        print( "processing {0}, run = {1}".format( filename, run.n ) )

        f = ROOT.TFile( filename)
        hrs = f.Get("Detector/h_rate_summary")
    except ValueError:
        print( "BAD FILE: {0}, ABORTING.".format( filename ) )
        return

    if not hrs:
        print( "NO h_rate_summary IN {0}, ABORTING.".format( filename ) )
        run.add_note(" h_rate_summary not found in {0}".format( filename ) )
        runs_dic['badruns'].append( run )
        return
    elif hrs.GetNbinsY() < 18:
        print( "BAD HISTOGRAM IN {0}, ABORTING.".format( filename ) )
        run.add_note(" bad h_rate_summary in {0}".format( filename ) )
        runs_dic['badruns'].append( run )
        return
    else:
        runs_dic['goodruns'].append( run )
        
    for xbin in range (1, hrs.GetNbinsX() + 1 ) :
        for ybin in range (1, hrs.GetNbinsY() + 1 ) :
            du    = int( hrs.GetXaxis().GetBinCenter( xbin) + 1e-10 )
            floor = int( hrs.GetYaxis().GetBinCenter( ybin) + 1e-10 )
            rate  = hrs.GetBinContent( xbin, ybin )
            
            if (du,floor) not in doms_dic :
                doms_dic[ (du,floor) ] = dac.DomInfo( du, floor )
                
            if rate == 0 : doms_dic[ (du,floor) ].dead_runs.append( run )
            if rate >  0 : doms_dic[ (du,floor) ].live_runs.append( run )

def pront( doms_dic ):

    for r in getruns( doms_dic ) :
        
        s = r.string()

        for (du,floor) in sorted(doms_dic.keys()) :

            if floor == 1 : s+= " | "
            s += '+' if r in doms_dic[(du,floor)].live_runs else '.'

        print( s )


def get_DU_dic( clb_map, det_id, verbose = False ):
    DU_dic = {}
    for DU in range( 200 ):
        for DOM in range( 20 ):
            dom = db_manager.doms.via_omkey( (DU, DOM), det_id )
            if dom == None: continue
            if verbose: print( dom )
            keys = dom.__str__().split("-")
            try:
                DU_dic[keys[0]].append( keys[1] )
            except KeyError:
                DU_dic[keys[0]] = [keys[1]]
    return DU_dic

def get_n_DU_DOM( DU_dic ):
    n_DU = len( DU_dic )
    n_DOM = 0
    for DU in DU_dic:
        if len(DU_dic[DU]) > n_DOM:
            n_DOM = len(DU_dic[DU])
    return (n_DU, n_DOM)

def get_unit( sc_param_name, sds = kp.db.StreamDS() ):
    #very slow for some reason...
    params = sds.allparams().MAPNAME[ sds.allparams().loc[:, 'MAPNAME'] == sc_param_name ]
    return sds.allparams().UNIT_NAME[  params.index[0] ]

def get_description( sc_param_name, sds = kp.db.StreamDS() ):
    #very slow for some reason...
    params = sds.allparams().MAPNAME[ sds.allparams().loc[:, 'MAPNAME'] == sc_param_name ]
    return sds.allparams().DESCRIPTION[  params.index[0] ]

def get_meaning( sc_param_name, sds = kp.db.StreamDS() ):
    return get_description( sc_param_name, sds = kp.db.StreamDS() )



def get_DOM_datagroup( scp_dataframe,
                       clb,
                       mpl_dates = True,
                       verbose = False):
    
    scp_datagroup = scp_dataframe.loc[ scp_dataframe.loc[:, 'SOURCE_NAME'] == clb.upi, :].copy()
    if not scp_datagroup.size:
        if verbose: print(" - DOM {0} empty! Skipping...".format( clb.floor ), end='')
        raise ValueError
    
    #Warning is due to the following line.
    if mpl_dates: #convert ms to s, then to matplotlib date number
        scp_datagroup.loc[:, 'UNIXTIME'] = md.epoch2num( scp_datagroup.loc[ :, 'UNIXTIME'] / 1000. )
        
    return scp_datagroup

def get_DU_datagroup( scp_dataframe,
                      DUs,
                      det_oid,
                      mpl_dates = True,
                      verbose = False):

    DU_clbs = get_DU_clbs( get_DU_omkeys( DUs, kp.db.CLBMap(det_oid).omkeys, ignore_base = True) )
    scp_datagroup = scp_dataframe.loc[ scp_dataframe.loc[:, 'SOURCE_NAME'].isin( DU_clbs ), : ].copy()
    #Warning is due to the following line.
    if mpl_dates: #convert ms to s, then to matplotlib date number
        scp_datagroup.loc[:, 'UNIXTIME'] = md.epoch2num( scp_datagroup.loc[ :, 'UNIXTIME'] / 1000.)#convert ms to s, then to matplotlib date number

    return scp_datagroup

def get_DOMID_from_CLB( CLB_UPI, clbm):
    for (DOM_ID, clb) in clbm.dom_ids.items():
        if clb == CLB_UPI:
            return DOM_ID
        
def get_omkey_from_CLB( CLB_UPI, clbm):
    for (omkey, clb) in clbm.omkeys.items():
        if clb.upi in CLB_UPI:
            return omkey

def get_DUs( omkeys ):
    DUs = []
    for omkey in omkeys:
        if omkey[0] not in DUs:
            DUs.append(omkey[0])
    return DUs

def get_live_DUs( scp_dataframe, clbm):
    return set( [ get_omkey_from_CLB( upi, clbm )[0] for upi in scp_dataframe.loc[:, 'SOURCE_NAME'].unique() ] )

def get_DU_omkeys( DUs, omkeys, ignore_base = True):
    omkeys_out = {}
    for (omkey, clb) in omkeys.items():
        if omkey[0] in DUs:
            if ignore_base == False or omkey[1] != 0:
                omkeys_out[omkey] = clb
    return omkeys_out

def get_DU_clbs( DU_omkeys ):
    return np.array([(lambda oc: oc[1].upi)(oc) for oc in sorted(DU_omkeys.items())])                         

def get_DU_clbs_floor( DU_omkeys ): 
    return np.array([(lambda oc: oc[1].upi + " ({0})".format(oc[1].floor))(oc) for oc in sorted( DU_omkeys.items())])

def DETID_to_OID( detid, sds = None):
    experiment, detid_n = detid.split("_")
    serial_n = int( detid_n )
    if not sds:
        sds = kp.db.StreamDS()
    dets = sds.detectors()
    return dets.loc[ dets.SERIALNUMBER == serial_n, 'OID' ].values[0]

def OID_to_DETID( oid, sds = None):
    if not sds:
        sds = kp.db.StreamDS()
    dets = sds.detectors()
    return "KM3NeT_{:08d}".format( dets.loc[ dets.OID == oid, 'SERIALNUMBER' ].values[0] )
