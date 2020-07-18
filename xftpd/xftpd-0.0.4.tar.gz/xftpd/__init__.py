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
from paramiko import ServerInterface,\
                        AUTH_FAILED,\
                        AUTH_SUCCESSFUL,\
                        OPEN_SUCCEEDED
from Crypto.PublicKey import RSA
from sftpserver.stub_sftp import StubSFTPServer


########################
# Random Password Generator
# Returns 14 character string
#
def random_string(num=14):
    Random_Str = ''
    char = 'abcdefghijklmnopqrstuvwxyz'
    CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUM = '1234567890'
    while len(Random_Str) < num:
        Random_Str += random.choice(char)
        Random_Str += random.choice(NUM)
        Random_Str += random.choice(CHAR)
    return Random_Str



########################
# Random RSA Key Generator
# Returns dictionary with
# private and public filenames
#
def random_rsa():
    key = RSA.generate(1024)
    PRIV = ''.join(i for i in [chr(random.randint(97,122)) for i in range(6)])
    f = open(PRIV, "wb")
    f.write(key.exportKey('PEM'))
    f.close()
    pubkey = key.publickey()
    PUB = ''.join(i for i in [chr(random.randint(97,122)) for i in range(6)])
    f = open(PUB, "wb")
    f.write(pubkey.exportKey('OpenSSH'))
    f.close()
    return {'priv':PRIV,'pub':PUB}



########################
# FTP Server Class
# Dir = str()
#   Ex: '/tmp'
# Port = int()
#   Ex: 2121
#
class ftp_server(object):
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
            TEST.connect(('8.8.8.8', 53))
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


########################
# SFTP Server Class
# Dir = str()
#   Ex: '/tmp'
# Port = int()
#   Ex: 22
# level = str()
#   Ex: 'DEBUG'
#
class sftp_server(object):
    def __init__(self,Dir='/tmp',Port=22,level='INFO'):
        self.Dir = Dir
        self.Port = Port
        self.level = level
        # Random user/pass
        self.user = random_string()
        self.Pass = random_string()
        # Get Local Server Address
        try:
            TEST = socket.socket()
            TEST.connect(('8.8.8.8', 53))
            self.Addr = TEST.getsockname()[0]
            TEST.close()
        except:
            print(traceback.format_exc())

    class _stub_server(ServerInterface):
        # SubClass of Paramiko ServerInterface
        # Allowing authentication only for random user/pass
        def __init__(self,user,Pass):
            self.user = user
            self.Pass = Pass

        def check_auth_password(self, username, password):
            # Only randomly generated user/pass is allowed
            if (username == self.user) and (password == self.Pass):
                return AUTH_SUCCESSFUL
            else:
                return AUTH_FAILED

        def check_channel_request(self, kind, chanid):
            return OPEN_SUCCEEDED

        def get_allowed_auths(self, username):
            # List availble auth mechanisms
            return 'password'

    class conn_handler_thd(threading.Thread):
        # Custom Connection Handler Thread for running server
        def __init__(self, conn, SRV, user, Pass, Dir, keyfile):
            threading.Thread.__init__(self)
            self.user = user
            self.Pass = Pass
            self.Dir = Dir
            self.SRV = SRV
            self._conn = conn
            self._keyfile = keyfile

        def run(self):
            self._host_key = paramiko.RSAKey.from_private_key_file(self._keyfile)
            self.transport = paramiko.Transport(self._conn)
            self.transport.add_server_key(self._host_key)

            self.STUB = StubSFTPServer
            self.STUB.ROOT = self.Dir

            self.transport.set_subsystem_handler(
                'sftp', paramiko.SFTPServer, StubSFTPServer)

            self.transport.start_server(server=self.SRV)
            self.channel = self.transport.accept()
            while self.transport.is_active():
                time.sleep(1)

    def _run_server(self):
        # Run Server function that calls Custom Connection Handler Thread
        paramiko_level = getattr(paramiko.common, self.level)
        paramiko.common.logging.basicConfig(level=paramiko_level)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server_socket.bind(('0.0.0.0', self.Port))
        self.server_socket.listen(10)
        self.SRV = self._stub_server(self.user,self.Pass)
        while True:
            self._conn, self.addr = self.server_socket.accept()
            self.srv = self.conn_handler_thd(self._conn, self.SRV, self.user, self.Pass, self.Dir, self._keyfile)
            self.srv.deamon = True
            self.srv.start()

    def start(self):
        # Random RSA key pair
        self._keys = random_rsa()
        self._keyfile = self._keys['priv']

        # Start Thread calling Run Server function
        self.srv = threading.Thread(target=self._run_server)
        self.srv.deamon = True
        self.srv.start()

    def stop(self):
        # Close server socket immediately
        # This will print a Threading Exception to STDOUT, but will not throw a true exception
        self.server_socket.close()
        os.remove(self._keys['priv'])
        os.remove(self._keys['pub'])




#########################
## Random PKI Generator
## Returns dictionary with
## private and public filenames
##
#def random_pki():
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
#class ftps_server(object):
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


#########################
## TFTP Server Class
## Dir = str()
##   Ex: '/tmp'
## Port = int()
##   Ex: 69
##
#class tftp_server(object):
#    # Create Random Username and Password
#    def __init__(self,Dir='/tmp',Port=2121):
#        self.Dir = Dir
#        self.Port = Port
#        # Random user/pass
#        self.user = Random_String()
#        self.Pass = Random_String()
#        # Create Dummy Authorizer, with the random user/pass
#        self.authorizer = DummyAuthorizer()
#        self.authorizer.add_user(self.user, self.Pass, self.Dir, perm='elradfmw')
#        self.handler = FTPHandler
#        self.handler.authorizer = self.authorizer
#        # Instantiate the FTP Server
#        self.SRV = ThreadedFTPServer(('0.0.0.0',self.Port), self.handler)
#        # Get Local Server Address
#        try:
#            TEST = socket.socket()
#            TEST.connect(('8.8.8.8', 53))
#            self.Addr = TEST.getsockname()[0]
#            TEST.close()
#        except:
#            print(traceback.format_exc())
#
#
#    def _run_server(self):
#        self.SRV.serve_forever()
#
#    def start(self):
#        # Kick off the serve_forever within a thread
#        self.srv = threading.Thread(target=self._run_server)
#        self.srv.deamon = True
#        self.srv.start()
#
#    def stop(self):
#        # Close all connections immediately
#        # This will print a Threading Exception to STDOUT, but will not throw a true exception
#        self.SRV.close_all()
#
#



