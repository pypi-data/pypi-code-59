import glob, os, pickle 
from fs.sshfs import SSHFS
from fs.osfs import OSFS

from .iolib    import *
from .classlib import *
from .clean_files import *

import km3pipe

#Produces run_dic, a dictionary of all bad runs, and interesting runs (such as death runs)
#dominfo_dic, a dictionary of all doms, containing information on their status over runs

import platform
import getpass
print(platform.python_version())

class crawler:
    
    def  __init__(self,
                  JRA_DIR = "/sps/km3net/repo/data/raw/quality/root/",
                  verbose = 0):

        self.verbose = verbose
        self.JRA_DIR = JRA_DIR

        if os.path.isdir( self.JRA_DIR ):
            self.my_fs = OSFS( self.JRA_DIR )
        else:
            self.my_fs = SSHFS( host = "cca.in2p3.fr",
                                user = input( "Lyon username: " ),
                                passwd = getpass.getpass(),
                                timeout = 60)
        
        self.run_dic = {}
        self.dominfo_dic = {}    # key will be a (line,floor) tupledominfo_dic = {}

        if verbose >= 2: print( "Fetching database streams...", end='' )
        self.sds = km3pipe.db.StreamDS()
        if verbose >= 2: print( " done." )

        if verbose >= 2: print( "Made crawler." )
        

    def crawl( self,
               detector,
               OUTRUNS,
               OUTDOMS,
               death_threshold   = 10,  #minimum amount of dead runs to be counted as "dead"
               coma_threshold    = 30,   #minimum amount of dead runs to be counted as "coma"
               passout_threshold = 1 ): #minimum amount of dead runs to be counted as "passout"

        files = {}
            
        for dir_detector in sorted( self.my_fs.listdir( '.' ) ):
            if( detector in DETID_to_OID( dir_detector, self.sds ) ) or ( dir_detector in detector ):
                if self.verbose >= 2: print(" found detector directory: {0}".format(dir_detector))
                files[dir_detector] = []
                for f in self.my_fs.glob( "{}/*/KM3NeT*root".format( dir_detector ) ):
                    files[dir_detector].append( f.path )
                self.run_dic['goodruns']  = [] #list of good JRA runs
                self.run_dic['badruns']   = [] #list of bad JRA runs
                self.run_dic['comaruns']  = {} #dictionary of key: run, value: list of omkeys of comadoms
                self.run_dic['deathruns'] = {} #dictionary of key: run, value: list of omkeys of deathdoms


        if not len( files.items() ):
            if self.verbose >= 1: print("ERROR: no files found.")
            raise ValueError

        # read the jra files
        for det, fdic in files.items():
            print( "detector {0}, total {1} files".format( det, len( fdic ) ) )
            for i, jrafile in enumerate( fdic ):
                if self.verbose >= 2: print( "detector {} file {} of {}".format( det, i, len(fdic) ) )
                process_jra_file( self.JRA_DIR + jrafile, det,
                                  self.run_dic,
                                  self.dominfo_dic,
                                  self.verbose )

        R = getruns( self.dominfo_dic )[-passout_threshold]
        print( "\nThe following were once alive, but are dead in the last {0} runs; i.e since at least run {1}:".format( passout_threshold, R.string() ) )




        #Categorize runs
        for dom_info in sorted( self.dominfo_dic.values(), key = lambda obj: obj.index ):

            dom_info.init_status_runs( death_threshold = death_threshold,
                                       passout_threshold = passout_threshold )
            if dom_info.is_empty():
                print( "DU{0}DOM{1}, empty".format(dom_info.du, dom_info.floor) )
                continue
            if not len( dom_info.live_runs ) :
                print( "DU{0}DOM{1}, always dead".format(dom_info.du, dom_info.floor) )
                continue
            try:
                if last_run( dom_info.live_runs ).index < R.index :
                    death_run = dom_info.get_death_run( death_threshold )
                    print( "DU{0}DOM{1}, dead since {2}".format(dom_info.du, dom_info.floor, death_run.string() ) )
                    death_run.add_note( "DU{0}DOM{1} death".format( dom_info.du, dom_info.floor ) )
                    if death_run in self.run_dic['deathruns']:
                        self.run_dic['deathruns'][death_run].append( (dom_info.du, dom_info.floor) )
                    else:
                        self.run_dic['deathruns'][death_run] = [ (dom_info.du, dom_info.floor) ]

            except AttributeError as ae:
                print( "ERROR: {0}".format( ae ) )

            #Define coma as a very long passout
            coma_runs = dom_info.get_passout_runs( coma_threshold )
            for coma_run in coma_runs:
                if coma_run in self.run_dic['comaruns']:
                    self.run_dic['comaruns'][coma_run].append( (dom_info.du, dom_info.floor) )
                else:
                    self.run_dic['comaruns'][coma_run] = [ (dom_info.du, dom_info.floor) ]
                    
        outfile_runs = open( OUTRUNS, 'wb')
        outfile_doms = open( OUTDOMS, 'wb')
        pickle.dump( self.run_dic, outfile_runs )
        pickle.dump( self.dominfo_dic, outfile_doms )
        outfile_runs.close()
        outfile_doms.close()

        return 0
        
    def pront_dominfo( dominfo_dic ):
        pront( dominfo_dic )

    def pront( self ):
        print( "runs with bad jra files : ", [ obj.string() for obj in self.run_dic['badruns'  ] ] )
        print( "runs with coma : ",          [ obj.string() for obj in self.run_dic['comaruns' ] ] )
        print( "runs with deaths : ",        [ obj.string() for obj in self.run_dic['deathruns'] ] )
        print( "dead  in all runs : ", sorted( [ d for d in self.dominfo_dic if not len( self.dominfo_dic[d].live_runs ) ] ) )
        print( "alive in all runs : ", sorted( [ d for d in self.dominfo_dic if self.dominfo_dic[d].alive_in_runs( getruns( self.dominfo_dic ) ) ]) )
