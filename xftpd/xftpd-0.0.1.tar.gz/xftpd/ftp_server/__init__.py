import os,\
        sys,\
        time,\
        socket,\
        random,\
        paramiko,\
        threading,\
        traceback
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


########################
# FTP Server Class
# Dir = str()
#   Ex: '/tmp'
# Port = int()
#   Ex: 2121
#
class FtpServer(object):
    # Create Random Username and Password
    def __init__(self,Dir='/tmp',Port=2121):
        self.Dir = Dir
        self.Port = Port
        # Random user/pass
        self.user = Random_String()
        self.Pass = Random_String()
        # Create Dummy Authorizer, with the random user/pass
        self.authorizer = DummyAuthorizer()
        self.authorizer.add_user(self.user, self.Pass, self.Dir, perm='elradfmw')
        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer
        # Instantiate the FTP Server
        self.SRV = ThreadedFTPServer(('0.0.0.0',self.Port), self.handler)
        # Get Local Server Address
        try:
            TEST = socket.socket()
            TEST.connect(("8.8.8.8", 80))
            self.Addr = TEST.getsockname()[0]
            TEST.close()
        except:
            print(traceback.format_exc())


    def _run_server(self):
        self.SRV.serve_forever()

    def start(self):
        # Kick off the serve_forever within a thread
        self.srv = threading.Thread(target=self._run_server)
        self.srv.deamon = True
        self.srv.start()

    def stop(self):
        # Close all connections immediately
        # This will print a Threading Exception to STDOUT, but will not throw a true exception
        self.SRV.close_all()


