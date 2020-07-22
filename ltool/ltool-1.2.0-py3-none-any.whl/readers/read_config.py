"""
@author: P. Paschou
"""
import configparser
import re
import numpy as np

class config():
    """
    Holds all the configurable variables
    
    Fields
    ===
        directories : Dict[str, str]
            Hold the paths of files
        
    """
    
    def __init__(self, path):
        """Reads the config file at the given path"""
        
        parser = configparser.ConfigParser()
        parser.read(path)

#Database       
        self.host = read_var(parser['database']['host'], str)

        self.user = read_var(parser['database']['user'], str)

        self.pswd = read_var(parser['database']['password'], str)
        
        self.port = read_var(parser['database']['port'], int)
        
        self.sock = read_var(parser['database']['socket'], str)
        
        self.dbid = read_var(parser['database']['scc-db-name'], str)

# SCC 
        
        self.inp = read_var(parser['scc']['input-dir'], str)

        self.out = read_var(parser['scc']['output-dir'], str)

        self.log = read_var(parser['scc']['log-dir'], str)

        self.log_lev = read_var(parser['scc']['log-level'], str)
        

# -------- END OF CLASS

def read_dictionary_with_dtype(d, keys, func):
    return {
        key: func(value)
        for key, value in d.items()
        if key in keys
    }

def read_var(var, func):
    #converts the var in a certain type (int, float, etc) unless it is ''
    if var != '':
        var = func(var)
    return(var)

def comma_split(var, func):
    
    if var != '':
        var = re.split(',', var)
    
        var = np.array([item.strip() for item in var], 
                       dtype = func) #trimming the spaces
    else:
        var=[]
    return(var)
