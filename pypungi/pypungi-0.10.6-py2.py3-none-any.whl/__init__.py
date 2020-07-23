'''Helper tool'''

__version__ = "0.10.6"

from .main import link

if __name__ == '__main__':
    import pypungi
    
    pp = pypungi.link()
    pp.stash('hi')
    pp.getStash()
    