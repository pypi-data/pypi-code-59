import asyncio
import hmac
import json
import logging
import uuid

from base64 import b64encode
from time import time

from pyee import AsyncIOEventEmitter
from slugify import slugify

from werkzeug.security import generate_password_hash, check_password_hash

from camus import app
from camus.util import MTimer, time_ms


_chat_manager = None


def get_chat_manager():
    global _chat_manager
    if _chat_manager is None:
        _chat_manager = ChatManager()
    return _chat_manager


def generate_turn_creds(key, client_id):
    expiration = int(time()) + 6 * 60 * 60  # creds expire after 6 hrs
    username = '{}:{}'.format(expiration, client_id)
    token = hmac.new(key.encode(), msg=username.encode(), digestmod='SHA1')
    password = b64encode(token.digest()).decode()

    return username, password


class ChatException(Exception):
    pass


class ChatRoom(AsyncIOEventEmitter):
    def __init__(self, name, password=None, guest_limit=None, admin_list=None, is_public=False):
        super().__init__()

        logging.info('Create ChatRoom {}'.format(id))
        self.name = name
        self.id = slugify(name)
        self.clients = {}
        self.password_hash = None if password is None else generate_password_hash(password)
        self.guest_limit = guest_limit
        self.admin_list = admin_list if admin_list is not None else []
        self.is_public = is_public
        self._last_active = time_ms()

        async def check_expire():
            now = time_ms() / 1000
            last_active = self.last_active / 1000

            if now - last_active > self._reap_timeout:
                logging.info('Room %s is expiring', self.id)
                self.emit('expire')
            else:
                new_timeout = last_active + self._reap_timeout - now
                self._timer = MTimer(new_timeout, check_expire)

        self._reap_timeout = 3600
        self._timer = MTimer(self._reap_timeout, check_expire)


    @property
    def last_active(self):
        last_seen = [client.last_seen for client in self.clients.values()]
        self._last_active = max([self._last_active, *last_seen])
        return self._last_active

    @property
    def active_ago(self):
        return int((time_ms() - self.last_active) / 60000)

    @property
    def info(self):
        clients = [{'id': client.id, 'username': client.username}
                   for client in self.get_clients()]

        return {'room_id': self.id, 'clients': clients}

    def authenticate(self, password=None):
        if password is None:
            return self.password_hash is None

        return check_password_hash(self.password_hash, password)

    def is_full(self):
        return self.guest_limit is not None and len(self.clients) == self.guest_limit

    def add_client(self, client):
        if self.is_full():
            raise ChatException('Guest limit already reached')

        self.clients[client.id] = client
        client.room = self

    def remove_client(self, client):
        logging.info('Removing client {} from room {}'.format(client.id, self.id))
        self._last_active = max(self._last_active, client.last_seen)
        client.room = None
        self.clients.pop(client.id, None)
        logging.info('{} clients remaining in room {}'.format(len(self.clients), self.id))

    def get_clients(self):
        return self.clients.values()

    def broadcast(self, message):
        logging.info('Broadcasting to room {}: {}'.format(self.id, message.json()))
        for client in self.get_clients():
            message.receiver = client.id
            client.send(message.json())

    async def shutdown(self):
        if self._timer is not None:
            self._timer.cancel()
            self._timer = None

        for client in self.clients.values():
            self.remove_client(client)
            await client.shutdown()


class ChatClient(AsyncIOEventEmitter):
    def __init__(self, id, username=None, room=None, is_admin=False):
        super().__init__()

        logging.info('Create client {}'.format(id))
        self.id = id
        self.username = username if username is not None else 'Major Tom'
        self.room = room
        self.is_admin = is_admin
        self.inbox = asyncio.Queue()
        self.outbox = asyncio.Queue()
        self._inbox_task = asyncio.create_task(
            self._process_inbox()
        )

        # Used by ChatManager for reaping
        # TODO: there is probably a cleaner solution
        self.last_seen = time_ms()
        self.timer = None

    async def _process_inbox(self):
        while True:
            message = await self.inbox.get()
            self.last_seen = time_ms()
            self.emit('message', message)

    def send(self, data):
        try:
            logging.info('ChatClient.send({})'.format(data))
            self.outbox.put_nowait(data)
        except Exception as e:
            logging.info('Couldn\'t send message to client {}: {}'
                         .format(self.id, e))

    def ping(self):
        message = ChatMessage()
        message.sender = 'ground control'
        message.receiver = self.id
        message.type = 'ping'
        message.data = time_ms()
        self.send(message.json())

    async def shutdown(self):
        message = ChatMessage()
        message.sender = 'ground control'
        message.receiver = self.id
        message.type = 'bye'
        message.data = time_ms()
        self.send(message.json())

        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        if self._inbox_task is not None:
            self._inbox_task.cancel()
            self._inbox_task = None

        logging.info('Finished shutting down client {}'.format(self.id))

class ChatMessage:
    def __init__(self, message=None):
        if isinstance(message, str):
            _json = json.loads(message)
        elif message is None:
            _json = {}
        else:
            _json = message

        # TODO: verify the sender against the client connection
        self.sender = _json.get('sender')
        self.receiver = _json.get('receiver')
        self.type = _json.get('type')
        self.data = _json.get('data')

    def json(self):
        return json.dumps(self.__dict__)


class ChatManager:
    def __init__(self):
        logging.info('Create ChatManager')
        self.rooms = {}
        self._message_address = "ground control"
        self._reap_timeout = 60

    @property
    def clients(self):
        return {client.id: client for room in self.rooms.values()
                for client in room.clients.values()}

    async def _handle_message(self, message, client):
        chat_message = self._parse_message(message, client)

        if chat_message.receiver == self._message_address:
            await self._handle_local_message(chat_message, client)
            return

        if chat_message.receiver == 'room':
            self._handle_room_message(chat_message, client)
            return

        if chat_message.receiver not in self.clients:
            logging.info('Message recipient does not exist for message: {}'.format(chat_message.json()))
            # TODO: reply with error
            return

        to_client = self.clients[chat_message.receiver]
        to_client.send(chat_message.json())
        logging.info('Sending message to client {}'.format(to_client.id))

    async def _handle_local_message(self, message, client):
        reply = ChatMessage()
        reply.sender = self._message_address
        reply.receiver = client.id

        if message.type == 'ping':
            reply.type = 'pong'
            reply.data = message.data
        elif message.type == 'pong':
            logging.info('Got pong {} from client {}'.format(message.data, message.sender))
            return
        elif message.type == 'profile':
            username = message.data.get('username')
            if username:
                client.username = username
            logging.info('Set username for client {}: {}'.format(client.id, username))
            self.broadcast_room_info(client.room)
            return
        elif message.type == 'get-room-info':
            reply.type = 'room-info'
            reply.data = client.room.info
        elif message.type == 'get-ice-servers':
            reply.type = 'ice-servers'
            reply.data = self.get_ice_servers(client.id)
        elif message.type == 'greeting':
            logging.info('Greeting received from client {}: {}'.format(message.sender, message.data))
            return
        elif message.type == 'bye':
            await self.remove_client(client)
            return
        else:
            reply.type = 'error'
            reply.data = 'Unknown message type: {}'.format(message.type)

        logging.info('Sending response: {}'.format(reply.json()))
        client.send(reply.json())

    def _handle_room_message(self, message, client):
        logging.info('Room message from {}: {}'.format(client.username, message))
        room = client.room
        for c in room.clients.values():
            c.send(message.json())

    def _parse_message(self, message, client):
        chat_message = ChatMessage(message)
        if chat_message.sender is None:
            chat_message.sender = client.id
        return chat_message

    def broadcast_room_info(self, room):
        message = ChatMessage()
        message.sender = self._message_address
        message.type = 'room-info'
        message.data = room.info
        room.broadcast(message)

    def add_room(self, room):
        self.rooms[room.id] = room

    async def remove_client(self, client):
        room = client.room
        if room:
            room.remove_client(client)
            self.broadcast_room_info(room)

        await client.shutdown()

    async def _reap(self, client):
        # Ping client and allow time for a response
        # If a message is received in the meantime, this task is cancelled by the timer
        logging.info('Ping client {} pending reaping'.format(client.id))
        client.ping()

        await asyncio.sleep(self._reap_timeout)
        await self.remove_client(client)

    def get_room(self, room_id):
        return self.rooms.get(room_id)

    def get_public_rooms(self):
        return sorted([room for room in self.rooms.values() if room.is_public],
                      key=lambda room: room.active_ago)

    def create_room(self, name, **kwargs):
        room_id = slugify(name)
        if room_id in self.rooms:
            raise ChatException('Room {} already exists'.format(room_id))

        room = ChatRoom(name, **kwargs)
        self.add_room(room)

        @room.on('expire')
        async def on_expire():
            await self.remove_room(room)

        return room

    async def remove_room(self, room):
        logging.info('Removing room %s', room.id)
        self.rooms.pop(room.id, None)
        await room.shutdown()

    def create_client(self, client_id=None):
        logging.info('create_client()')

        if client_id is None:
            client_id = uuid.uuid4().hex

        if client_id in self.clients:
            raise ChatException('Client {} already exists'.format(client_id))

        client = ChatClient(client_id)
        client.timer = MTimer(self._reap_timeout, self._reap, client=client)

        logging.info('Sending greeting to client {}'.format(client.id))
        greeting = ChatMessage()
        greeting.sender = self._message_address
        greeting.receiver = client.id
        greeting.type = 'greeting'
        greeting.data = 'This is Ground Control to Major Tom: You\'ve really made the grade. Now it\'s time to leave the capsule if you dare.'
        client.send(greeting.json())

        @client.on("message")
        async def on_message(message):
            logging.info('Received message: {}'.format(message))

            # Reap this client if we haven't seen it for too long
            if client.timer is not None:
                client.timer.cancel()
            client.timer = MTimer(self._reap_timeout, self._reap, client=client)

            await self._handle_message(message, client)

        return client

    def get_ice_servers(self, client_id):
        stun_host = app.config['STUN_HOST']
        stun_port = app.config['STUN_PORT']
        stun_url = 'stun:{}:{}'.format(stun_host, stun_port)
        servers = [{'urls': [stun_url]}]

        turn_host = app.config['TURN_HOST']
        turn_port = app.config['TURN_PORT']
        turn_key = app.config['TURN_STATIC_AUTH_SECRET']

        if turn_host and turn_port and turn_key:
            turn_url = 'turn:{}:{}'.format(turn_host, turn_port)
            username, password = generate_turn_creds(turn_key, client_id)
            servers.append({'urls': [turn_url], 'username': username, 'credential': password})

        return servers
