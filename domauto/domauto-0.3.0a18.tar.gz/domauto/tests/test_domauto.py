import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from unittest import TestCase

#from domauto.crawler import crawler
#from domauto.scp_plotter import scp_plotter
#from domauto.status_plotter import status_plotter

__author__ = "Jordan Seneca"
__credits__ = []
__license__ = "MIT"
__maintainer__ = "..."
__email__ = "jseneca@km3net.de"

class TestClasses( TestCase ):

    def test_null( self ):
        
        assert 1

    #def test_crawler( self ):

    #    OUTDOMS = 'DOMINFO_DIC_TEST.pickle'
    #    OUTRUNS = 'RUNINFO_DIC_TEST.pickle'
    
    #    mycrawler = crawler()
    #    assert 1
    #assert 0 == mycrawler.crawl( 'ORCA',
    #                            OUTRUNS,
    #                           OUTDOMS )
    
    #def test_scp_plotter( self ):
    
    #    myscp_plotter = scp_plotter()
    #    assert 1
    
    #def test_status_plotter( self ):
    
    #   mystatus_plotter = status_plotter()
    #   assert 1
    
