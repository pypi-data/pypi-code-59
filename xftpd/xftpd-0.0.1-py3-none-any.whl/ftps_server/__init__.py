import os,\
        sys,\
        time,\
        socket,\
        random,\
        paramiko,\
        threading,\
        traceback
from Crypto.PublicKey import RSA
from sftpserver.stub_sftp import StubSFTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler #, TLS_FTPHandler ##Apparently the TLS module doesn't exist in Python3
from pyftpdlib.servers import ThreadedFTPServer





########################
# Random Password Generator
# Returns 14 character string
#
def Random_String(num=14):
    Random_Str = ''
    while len(Random_Str) < num:
        char = 'abcdefghijklmnopqrstuvwxyz'
        CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        NUM = '1234567890'

        Random_Str += random.choice(char)
        Random_Str += random.choice(NUM)
        Random_Str += random.choice(CHAR)

    return Random_Str

#########################
## Random PKI Generator
## Returns dictionary with
## private and public filenames
##
#def Random_PKI():
#    return {'priv':PRIV,'pub':PUB}
#
#########################
## TLS FTP Server Class
## FTPS... NOT SFTP
## Dir = str()
##   Ex: '/tmp'
## Port = int()
##   Ex: 2121
## cert = str()
## key = str()
#class TlsFtpServer(object):
#    # Create Random Username and Password
#    def __init__(self,Dir='/tmp',Port=2121,cert='cert.pem',key=None):
#        self.Dir = Dir
#        self.Port = Port
#        self.cert = cert
#        self.key = key
#        self.user = Random_String()
#        self.Pass = Random_String()
#        self.authorizer = DummyAuthorizer()
#        self.authorizer.add_user(self.user, self.Pass, self.Dir, perm='elradfmw')
#        self.handler = TLS_FTPHandler
#        self.handler.certfile = self.cert
#        self.handler.keyfile = self.key
#        self.handler.authorizer = self.authorizer
#
#        self.SRV = ThreadedFTPServer(('0.0.0.0',self.Port), self.handler)
#
#    def _run_server(self):
#        self.SRV.serve_forever()
#
#    def start(self):
#        self.srv = threading.Thread(target=self._run_server)
#        self.srv.deamon = True
#        self.srv.start()
#
#    def stop(self):
#        self.SRV.close_all()
#




