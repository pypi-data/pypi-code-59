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
import os
import subprocess
import sys
import threading
import time
import uuid
from pathlib import Path

import zmq

from .constants import (
    ADDED, COMMITED, FETCHED, MODIFIED, RP_COMMON, RP_STRICT, STATE_ACTIVE,
    STATE_INITIAL, STATE_QUITTING, STATE_SYNCING, STATE_LAUNCHING_SERVICES, UP)
from .data import (
    RepDeleteCommand, RepDisconnectCommand, ReplicatedCommand,
    ReplicatedDatablock, RepRightCommand, RepUpdateClientsState,
    RepUpdateUserMetadata)
from .network import ClientNetService
from .observer import Observer
from .service import ServiceManager
from .worker import TaskExecutor
from .utils import current_milli_time


class Orchestrator(threading.Thread):
    """Orchestrator

    Main thread in charge to coordinate each services such as
    - Network
    - TaskExecutor
    - Observers (soon remove in flavor of event driven)
    """

    def __init__(
            self,
            replication_graph=None,
            q_tasks=None,
            q_net_output=None,
            session=None,  # TODO: Remove !!!!!
            factory=None,
            python_path=sys.executable):
        threading.Thread.__init__(self)

        self.name = "Orchestrator"

        self._exit_event = threading.Event()
        self._python = python_path  # used by subprocess popen
        self._rep_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        self._ttl_script = os.path.join(self._rep_dir, 'ttl.py')
        self._server_script = os.path.join(self._rep_dir, 'server.py')

        self._context = zmq.Context()
        self._com_services = None  # inter-process communication socket
        self._connection_timeout = 3000
        self._graph = replication_graph
        self._factory = factory
        self._q_tasks = q_tasks
        self._q_net_output = q_net_output

        self._session = session
        self._online_users = {}
        self._is_host = False
        self._state = {
            'STATE': STATE_INITIAL,
            'CURRENT': -1,
            'TOTAL': -1
        }

        self._services = []
        self._server_process = None
        self._service_manager = ServiceManager(python_path=self._python)

    def connect(
            self,
            id="Default",
            address="127.0.0.1",
            port=5560,
            ipc_port=5565,
            timeout=1000,
            password=None):

        self._port = port
        self._ipc_port = ipc_port
        self._address = address
        self._connection_timeout = timeout
        self._service_manager.start(ipc_port)
        self.start()

        self._state['STATE'] = STATE_LAUNCHING_SERVICES

        # Background tasks executor service
        self._service_manager.launch_service(
            TaskExecutor,
            graph=self._graph,
            push_queue=self._q_net_output,
            tasks=self._q_tasks
        )

        # Network IO service
        self._service_manager.launch_service(
            ClientNetService,
            store_reference=self._graph,
            factory=self._factory,
            items_to_push=self._q_net_output,
            tasks=self._q_tasks,
            id=id,
            address=address,
            port=port,
            password=password
        )

        ids = self._service_manager._services['NetworkIO']['instance']._uuid_str
        self._service_manager.launch_service_as_subprocess(
                            'TTL',
                            self._ttl_script,
                            '-p', str(self._port),
                            '-d', self._address,
                            '-i', str(ids),
                            '-t', str(self._connection_timeout),
                            '-tp', str(self._ipc_port),
                        )

    def host(
            self,
            id="Default",
            port=5560,
            ipc_port=5560,
            timeout=1000,
            password="admin"):

        self._is_host = True

        # Launch the server
        self._server_process = subprocess.Popen([
            self._python,
            self._server_script,
            '-p', str(port),
            '-t', str(timeout),
            '-pwd', str(password),
            '--attached',]
        )

        # Launch the client
        self.connect(
            id=id,
            address="127.0.0.1",
            port=port,
            ipc_port=ipc_port,
            password=password)

    def disconnect(self):
        if self.state['STATE'] == STATE_ACTIVE:
            deco_request = RepDisconnectCommand(
                owner='client'
            )

            self._q_net_output.put(deco_request)
        else:
            self.stop()

    #TODO: move this into the future repositoy class
    def init_repository(self):
        self._service_manager._services['NetworkIO']['instance'].request_server_repository_init()

    def run(self):
        starting_time = current_milli_time()  # used for timeout

        while not self._exit_event.wait(.005):
            incoming_services_msg = self._service_manager.handle_services_com()

            if incoming_services_msg is not None:
                address = incoming_services_msg.pop(0)
                if 'EVENT' in address:
                    if 'LOBBY' in address:
                        
                        if self._is_host:
                            self.init_repository()

                    if 'CONNECTED' in address:
                        # Preload the graph before apply it on client side.
                        # It avoid to deal with circular dependencies.
                        for node in self._graph.list_ordered():
                            node_ref = self._graph.get(node)
                            if node_ref.state == FETCHED:
                                node_ref.resolve()

                        self._state = {
                            'STATE': STATE_ACTIVE,
                            'CURRENT': -1,
                            'TOTAL': -1
                        }

                        # NOTE: This will be remove with the Event-Driven
                        # system
                        for stype, implementation, timer, auto in self._factory.supported_types:
                            if timer > 0:
                                self._service_manager.launch_service(Observer,
                                                                     store_reference=self._graph,
                                                                     watched_type=implementation,
                                                                     timeout=timer,
                                                                     automatic=auto,
                                                                     session_instance=self._session)
      
                    if 'FAILURE' in address:
                        logging.error(
                            "Failed to connect, authentification refused.")
                        self.stop()
                    if 'DISCONNECT' in address:
                        state = incoming_services_msg.pop(0)
                        logging.info(
                            f"Quitting session. [ {state['reason']} ]")
                        self.stop()
                    if 'CONNECTION_REFUSED' in address:
                        logging.error("Connection refused by server")
                        self.stop()
                    if 'CONNECTION_FAILED' in address:
                        logging.error("Connection failed, server not found")
                        self.stop()
                elif 'STATE' in address:
                    state = incoming_services_msg.pop(0)

                    if 'CLIENTS' in address:
                        self._online_users = state
                    if 'CONNECTION' in address:
                        self._state = state

            if self._state['STATE'] == STATE_LAUNCHING_SERVICES and \
                    current_milli_time() - starting_time > self._connection_timeout:
                logging.error("Service launching error. Quitting")
                self.stop()

        self._service_manager.stop()
        self._state['STATE'] = STATE_INITIAL

    @property
    def state(self):
        return self._state

    @property
    def services_state(self):
        return {k: v['state'] for k, v in self._service_manager._services.items()}

    @property
    def online_users(self):
        return self._online_users

    def stop(self):
        self._state['STATE'] = STATE_QUITTING

        # Stop the server
        if self._is_host:
            self._server_process.kill()

        self._service_manager.stop_all_services()
        time.sleep(1)
        self._exit_event.set()

        # Cleanup  vars
        self._online_users.clear()
        self._graph.clear()

        with self._q_net_output.mutex:
            self._q_net_output.queue.clear()

        with self._q_tasks.mutex:
            self._q_tasks.queue.clear()

        self._is_host = False

        if not self.is_alive():
            self._service_manager._services.clear()
            self._state['STATE'] = STATE_INITIAL
