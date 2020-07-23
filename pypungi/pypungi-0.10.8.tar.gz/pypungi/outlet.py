'''
  abstract visualization class; implements methods all visualization classes should have
  
  class methods are services available to the outlet
'''

class Outlet : 
    def ping(self):
        '''tests if is connected'''
        pass
    
    def plot(self):
        '''main visualization method with model; takes data and "plot" it'''
        pass
    
    def stash(self):
        pass
    
    def getStash(self):
        pass
    
    def download(self):
        pass
    
    def model(self):
        '''main visualization method with plot; takes data transforms it and "plot" it'''
        pass