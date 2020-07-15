#!/usr/bin/env python3

"""
DomAuto.

Usage:
     domauto.py crawl         [ -d | --detector <detector> ] [ -F | --force ] [ -t | --threshold <threshold> ]
     domauto.py plot-status   [ -f | --doms_file <doms_file> ] [ -r | --runs_file <runs_file> ] [ -o | -output <output> ] [ -d | --detector <detector> ] [ -F | --force ] [ -t | --threshold <threshold> ]
     domauto.py plot-scp      [ -d | --detector <detector> ] [ -F | --force ] [ -t | --threshold <threshold> ] [ -r | --runs_file <runs_file> ]
     domauto.py webpage       [ -d | --detector <detector> ] [ -F | --force ] [ -t | --threshold <threshold> ]


-f --doms_file        Pickle dom info file
-r --runs_file        Pickle run info file
-d --detector         Detector code, ORCA, or ARCA
-F --force            Force recreate
-t --threshold        Set threshold
-h --help             Display this screen
"""        

import platform
print(platform.python_version())
    
import docopt, os
import pickle
from domauto import crawler
from domauto import status_plotter
from domauto import scp_plotter

def main():

    args = docopt.docopt( __doc__ )
    print( "args: ", args )

    OUTDOMS = args['<doms_file>'] if args['<doms_file>'] else 'files/DOMINFO_DIC_{0}.pickle'.format( args['<detector>'] )
    OUTRUNS = args['<runs_file>'] if args['<runs_file>'] else 'files/RUN_DIC_{0}.pickle'.format(     args['<detector>'] )


    #################    
    if args['crawl']:

        if args['--force']:
            clean_files( args['<detector>'] )
        elif os.path.isfile( OUTRUNS ) and os.path.isfile( OUTDOMS ):
            print( "Files for {0} already exist, exiting.".format( args['<detector>'] ) )
            exit()

        mycrawler = crawler()
        if args['<threshold>']:
            mycrawler.crawl( args['<detector>'],
                             OUTRUNS,
                             OUTDOMS,
                             death_threshold   = args['<threshold>'],
                             coma_threshold    = args['<threshold>'],
                             passout_threshold = args['<threshold>'] )
        else:
            mycrawler.crawl( args['<detector>'],
                             OUTRUNS,
                             OUTDOMS )
        mycrawler.pront()




    ###################
    if args['webpage']:
        if args['--force']:
            web_maker.clean()


        self.OUTDIR = "{0}/RUN{1}".format( self.PLOTS_DIR + "/" + self.detector, MAXRUN ) 
        make_plot_dirs( self.OUTDIR )


        if len( glob.glob( self.OUTDIR + "/*{0}*".format( PARAM_NAME) ) ) >= 5 and not args['--force']:
            print( "Directory exist and has been filled. Aborting." )
            raise ValueError


        DET_DIR = PLOTS_DIR + "/" + run.det_id 
        outfile = open( DET_DIR + "/runs_notes.md", 'a')
        for note in run.notes:
            outfile.write("RUN{0}:".format( run.n ) + note + "\n" )
        outfile.close()
        OUTDIR = "{0}/RUN{1}".format( DET_DIR, run.n ) 
        make_plot_dirs( OUTDIR )
        run.dump_notes( OUTDIR )







    #######################
    if args['plot-status']:

        if not os.path.isfile( OUTRUNS ):
            print( "{0} not found, exiting.".format( OUTRUNS ) )
            exit()

        if not os.path.isfile( OUTDOMS ):
            print( "{0} not found, exiting.".format( OUTDOMS ) )
            exit()

        myplotter = status_plotter( args['<detector>'],
                                       OUTDOMS,
                                       OUTRUNS )

        myplotter.plot(args['<output>'], args['--force'])




    ####################

    """
    if args['plot-scp']:

        if REWRITE or len( glob.glob( OUTDIR + "/*{0}*".format( PARAM_NAME ) ) ) < 5:
            for par_file in glob.glob( OUTDIR + "/*{0}*".format( PARAM_NAME ) ):
                os.remove( par_file )
        else:
            print( "Directory exist and has been filled. Exiting." )
            exit()

        PLOTS_DIR = './plots'
        if not os.path.isdir( PLOTS_DIR ):
            print("Plots directory not found.")
            raise ValueError

        MINRUN = args['runs'][0]
        MAXRUN = args['runs'][-1]

        #
        #
        #
        #
        #
    """


    ##########################
    if args['plot-scp']:

        if not os.path.isfile( OUTDOMS ):
            print( "{0} not found, exiting.".format( OUTDOMS ) )
            exit()

        PLOTS_DIR = './plots'
        if not os.path.isdir( PLOTS_DIR ):
            print("Plots directory not found.")
            raise ValueError

        RUN_DIC = pickle.load( open( OUTRUNS, 'rb' ) )

        RUN_LIST = []
        RUN_LIST.extend( RUN_DIC['deathruns'].items() )
        RUN_LIST.extend( RUN_DIC['comaruns'].items() )

        #RUN_APPENDIX = [ ( dacl.Run( det_id = MAN_RUN_LIST[0], n = int(run_n) ), [(-1, -1)] ) for run_n in MAN_RUN_LIST[1:] ] if MAN_RUN_LIST else []
        #RUN_LIST.extend( RUN_APPENDIX )

        myplotter = scp_plotter()
        myplotter.batch_plot( RUN_LIST,
                              OUTDIR = PLOTS_DIR,
                              SCP_LIST = 'SHORT',
                              RUN_RANGE = [5, 2],
                              REWRITE   = args['--force'])

if __name__ == '__main__':
    main()
