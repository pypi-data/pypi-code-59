# ##### BEGIN GPL LICENSE BLOCK #####
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


import logging
import marshal
import subprocess
import sys
import threading
import time

import zmq

from .constants import STATE_ACTIVE, STATE_INITIAL
from .exception import ServiceNetworkError
from .utils import current_milli_time


"""
 A simple service management API with two components:
   * Service Manager (ROUTER)
   * Service (DEALER)

 The goal is to manage Subprocess and Thread services by using zmq to 
 communicate between the service manager and service.
"""

SERVICE_TIMEOUT = 2000
SERVICE_HEARTBEAT = 2000

class ServiceManager():
    """
        Handle Services management.
    """
    def __init__(
            self,
            python_path=sys.executable,
            ipc_port=5590):
        self._services = {}
        self._context = zmq.Context()
        self._state = STATE_INITIAL
        self._python = python_path

    def start(self, ipc_port):
        """
            Start the service manager.

            :param ipc_port: inter-service communication port 
            :type ipc_port: integer
        """
        # Bind a ROUTER socket to listen services
        self._ipc_port = ipc_port
        self._com_services = self._context.socket(zmq.ROUTER)
        self._com_services.setsockopt(zmq.IDENTITY, b'SERVICE_MANAGER')

        try:
            self._com_services.bind(f"tcp://*:{ipc_port}")
        except zmq.ZMQError:
            self._context.destroy()
            raise ServiceNetworkError(f"Can't launch service manager, an instance is already running on the same IPC ports.")

        self._com_services.linger = 0
        
        self._services_poller = zmq.Poller()
        self._services_poller.register(self._com_services, zmq.POLLIN)

        self._state = STATE_ACTIVE
        logging.debug('Service manager launched')

    def launch_service_as_subprocess(self, name, script_path, *args):
        """
            launch a service as subprocess

            :param name: service name
            :type name: str
            :param script_path: python script path
            :type script_path: str 
        """
        service_instance = subprocess.Popen([
            self._python,
            script_path,
            *args])

        self._services[name] = {
            'instance': service_instance,
            'state': STATE_INITIAL,
            'type': 'subprocess'
        }

    def launch_service(self, service, **kwargs):
        """
            launch a service

            :param service: service implementation
            :type service: Service 
        """

        service_instance = service(ipc_port=self._ipc_port, **kwargs)

        self._services[service_instance.name] = {
            'instance': service_instance,
            'state': STATE_INITIAL,
            'type': 'thread'
        }

    def stop_service(self, service_name, blocking = True):
        """
            Stop the given service

            :param service_name: Stoped service name
            :type service_name: str
        """
        assert(service_name in self._services.keys())

        service = self._services.get(service_name)

        if service:
            self._com_services.send(service_name.encode(), zmq.SNDMORE)
            self._com_services.send_multipart([b'STOP', b'-'])

            # Waiting the service to end by itself
            # TODO: timeout
            while blocking and service['state'] != STATE_INITIAL:
                self.handle_services_com(timeout=1)
        else:
            logging.error(f"Service {service_name} not found")

    def stop_all_services(self):
        """
            Stop all services
        """
        for service in self._services:
            self.stop_service(service, blocking=False)

        while len([s for s in self._services.values() if s['state'] == STATE_ACTIVE]) > 0:
            self.handle_services_com(timeout=1)
        
    def handle_services_com(self, timeout=1):
        """
            Retrieve services communications frames.

            :param timeout: Timeout delay for services message reception (milliseconds) 
            :type timeout: integer
        """
        # Services communication triage
        items = dict(self._services_poller.poll(timeout))
        service_frame = None

        if items:
            service_frame = self._com_services.recv_multipart(0)

            sender = service_frame.pop(0).decode()
            destination = service_frame.pop(0).decode()
            state = marshal.loads(service_frame.pop(0))

            if destination == "MANAGER":
                address = state.pop(0)
                if 'STATE' in address:
                    if sender not in self._services:
                        self._services[sender] = {}
                    self._services[sender]['state'] = state.pop(0)
                if 'HEARTBEAT' in address:
                    self._com_services.send(sender.encode(), zmq.SNDMORE)
                    self._com_services.send_multipart([
                        b'HEARTBEAT',
                        marshal.dumps(state)])

                return None
            else:
                return state

    def stop(self):
        """Stop service manager, close imternal communication sockets
        """
        assert([s['state'] == STATE_INITIAL for s in self._services.values()])

        self._com_services.close()
        logging.debug("Service manager stopped.")

        self._services.clear()


class Service(threading.Thread):
    """A basic looping routine.
    """
    def __init__(
            self,
            ipc_port=None,
            name="DefaultServiceName",
            context=zmq.Context()):
        assert(ipc_port)

        threading.Thread.__init__(self)

        self._name = name
        self._service_state = STATE_INITIAL
         
        self._loop_interval = 0 # TODO: remove this
        self._ipc_port = ipc_port
        self._context = context

        self._ipc_com = self._context.socket(zmq.DEALER)
        self._ipc_com.setsockopt(zmq.IDENTITY, self._name.encode())
        self._ipc_com.connect(f"tcp://localhost:{self._ipc_port}")
        self._ipc_com.linger = 0

        self._poller = zmq.Poller()
        self._poller.register(self._ipc_com, zmq.POLLIN)

        self._stop_flag = threading.Event()
        self.notify_manager(['STATE', self._service_state])

    def notify_manager(self, state):
        """
            Send a state to the Service Manager

            :param state: state 
            :type state: any marshalable python object
        """
        self._ipc_com.send_multipart([b'MANAGER', marshal.dumps(state)])

    def notify(self, state):
        """
            Send a state to the entity which run the service manager

            :param state: state 
            :type state: any marshalable python object
        """
        self._ipc_com.send_multipart([b'PARENT', marshal.dumps(state)])

    def run(self):
        """
            Main service loop. 
            It handle service IO communication on each iteration.
        """
        self._service_state = STATE_ACTIVE
        self.notify_manager(['STATE', self._service_state])

        self.send_heartbeat()
        last_heartbeat = current_milli_time()
        last_response = 0
        ping = 0
        timer_main = 0
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(f'D:/{self._name}.log')
        self.logger.addHandler(fh)
        while not self._stop_flag.wait(self._loop_interval):
            sockets = dict(self._poller.poll(1))
            current_time = current_milli_time()

            if self._ipc_com in sockets:
                msg = self._ipc_com.recv_multipart()
                header = msg.pop(0)
                if header == b'STOP':
                    self._stop_flag.set()
                    break
                if header == b'HEARTBEAT':
                    last_response = current_time

            # Check timeout
            if ping > SERVICE_TIMEOUT:
                self._stop_flag.set()
                self.logger.info("STOP")

            # Heartbeat
            if current_time-last_heartbeat > SERVICE_HEARTBEAT:
                # Evaluate ping
                ping = abs(last_response - \
                    (last_heartbeat+(self._loop_interval*1000)+timer_main))

                self.send_heartbeat()
                last_heartbeat = current_time

            # Run implementation tasks
            timer_main_start = current_milli_time()
            self.main(sockets)
            timer_main=current_milli_time()-timer_main_start

        self.stop()
        self._service_state = STATE_INITIAL
        self.notify_manager(['STATE', self._service_state])     
        self._ipc_com.close()


    def send_heartbeat(self):
        """ Notify the service manager that we are alive
        """
        self.notify_manager(['HEARTBEAT'])

    def main(self, sockets):
        """
            Service main code. Called with `_loop_interval` frequency.

            :param sockets: incoming sockets
            :type sockets: dict of zmq.Socket
        """
        raise NotImplementedError

    def stop(self):
        """
            Handle service stop. 
            Clean the room form here.
        """
        raise NotImplementedError

    @property
    def context(self):
        """ Service zmq context access
        """
        return self._context

    @property
    def poller(self):
        """ Service zmq poller access
        """
        return self._poller

    @property
    def name(self):
        """ Service name context access
        """
        return self._name
