import os

from unittest import TestCase

import domauto

class TestCrawler( TestCase ):

    def test_output( self ):


        OUTDOMS = 'DOMINFO_DIC_TEST.pickle'
        OUTRUNS = 'RUN_DIC_TEST.pickle'
    
        mycrawler = domauto.crawler()
        mycrawler.crawl( None,
                         OUTRUNS,
                         OUTDOMS )
        self.assertTrue( os.path.isfile( OUTRUNS ) )
