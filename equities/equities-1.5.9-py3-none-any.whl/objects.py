import os 
import sys 
import shutil, errno


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# storage objects
from equities.lib.storage.Connections import LocalStorage
from equities.lib.storage.Connections import Resolver
#from equities.lib.sotrage.Connections import GcpStorage

# Scripts 
from equities.scripts.pull import PullScript
from equities.scripts import test as TestScript

class Universe(object):
    '''
        A Universe should be thought of as a set of Companies.
        The universe object gives us the ability to download,
        access and purge our data. 
    '''

    def __init__(self,path='default_path'):

        self.connect_storage(path) # Attempt to Connect to local storage.

        msg_success = " > 🌟 ( universe instantiated )  - local storage connected! "
        msg_empty   = " > 🗑️ ( universe instantiated )  - local storage is empty"
        msg_fail    = """ > 💣 !! Error !! Invalid storage path, local storage not 
                          connected\n\t ---- QUITTING... """
        
        # Prints status message 
        if len(self) > 0: print(msg_success) # Non-empty Universe
        else:
            if path != 'default_path':
                print(msg_fail); quit() # Invalid Path 
            else: print(msg_empty) # Empty Universe

    def __getitem__(self,id):
        return Company(\
            cik = str(id),\
            storage = self.storage)

    def __len__(self):
        return len(self.ciks)

    def connect_storage(self,path):
        try: 
            self.storage = LocalStorage(path=path)
            self.storage_path = self.storage.DATADIR
            self.ciks = self.storage.ciks
        except:
            self.storage = None 
            self.storage_path = None
            self.ciks = []
            pass 

    def properties(self):
        return self.storage.get('properties')

    def manifest(self):
        return self.storage.get('manifest')

    def build(self,quarters=[],ciks=[]):
        print(">>> BUILDING SEC UNIVERSE")
        PullScript().execute(quarters = [q.lower() for q in quarters],
                             ciks     = ciks)
        self.connect_storage(path=self.storage_path) # reconnects to storage
        print(">>> build - complete")

    def purge(self):
        print(">>> PURGING SEC UNIVERSE")
        PullScript().purge()
        print(">>> purge - complete")

    def serialize(self):
        print(">>> SERIALIZING SEC UNIVERSE")
        print(" > 📦 ( zipping your universe )")
        uni = {}
        for cik in self.ciks:
            stmt = {}
            try: stmt['income']=self.__getitem__(cik).income()
            except: stmt['income']=None; pass
            try: stmt['balance']=self.__getitem__(cik).income()
            except: stmt['balance']=None; pass
            try: stmt['cash']=self.__getitem__(cik).cash()
            except: stmt['cash']=None; pass
            uni[cik]=stmt
        print(">>> serialize - complete")
        return uni
        
    def export(self,export_path):
        print(">>> EXPORTING SEC UNIVERSE")
        print(" > 🚢 ( exporting of your universe in csv fmt %s)"%(str(export_path)))
        try:
            shutil.copytree(os.path.join(self.storage_path,'clean'), os.path.join(export_path,'data'))
        except OSError as exc: # python >2.5
            if exc.errno == errno.ENOTDIR:
                shutil.copy(os.path.join(self.storage_path,'clean'), os.path.join(export_path,'data'))
            else: raise
        print(">>> export - complete")

    @staticmethod
    def test():
        print(">>> RUNNING TEST SCRIPT")
        TestScript.execute()
        print(">>> test - complete")

class Company(object):

    def __init__(self,cik,storage,collapse=False):
        self.collapse = collapse
        self.cik      = cik
        self.storage  = storage
            
    def _header_series(self):
        return self.storage.get(item = 'properties')[int(self.cik)]

    def _try_get_sheet(self,item):
        try:
            result = self.storage.get(item = item,
                                      cik  = self.cik,
                                      collapse = self.collapse)
        except Exception as e:
            print(e)
            result = None
        return  result

    def name(self):
        return self._header_series()['name']

    def sic(self):
        return int(self._header_series()['sic'])

    def division(self):
        try: return self.storage.resolver.resolve(\
                int(self.sic),'SIC','Division')
        except: return 'N/A';

    def industry(self):
        try:  return self.storage.resolver.resolve(\
                int(self.sic),'SIC','Industry Group')
        except: return 'N/A';

    def income(self):
        return self._try_get_sheet(\
            item = 'income')

    def balance(self):
        return self._try_get_sheet(\
            item = 'balance')

    def cash(self):
        return self._try_get_sheet(\
            item = 'cash')

    def equity(self):
        return self._try_get_sheet(\
            item = 'equity')

    def undefined(self):
        return self._try_get_sheet(\
            item = 'undefined')  
        