'''
    icmplib
    ~~~~~~~

        https://github.com/ValentinBELYN/icmplib

    :copyright: Copyright 2017-2020 Valentin BELYN.
    :license: GNU LGPLv3, see the LICENSE for details.

    ~~~~~~~

    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public License
    as published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this program.  If not, see
    <https://www.gnu.org/licenses/>.
'''


class ICMPLibError(Exception):
    '''
    Exception class for the icmplib package.

    '''
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message

    @property
    def message(self):
        return self._message


class ICMPSocketError(ICMPLibError):
    '''
    Base class for ICMP sockets exceptions.

    '''


class SocketPermissionError(ICMPSocketError):
    '''
    Raised when the permissions are insufficient to create a socket.

    '''
    def __init__(self):
        message = 'Root privileges are required to create the socket'
        super().__init__(message)


class SocketBroadcastError(ICMPSocketError):
    '''
    Raised when a broadcast address is used and the corresponding
    option is not enabled on the socket.

    '''
    def __init__(self):
        message = 'Broadcast is not allowed: ' \
                  'please use broadcast method (setter) to allow it'
        super().__init__(message)


class TimeoutExceeded(ICMPSocketError):
    '''
    Raised when a timeout occurs on a socket.

    '''
    def __init__(self, timeout):
        message = f'The timeout has been reached ({timeout}s)'
        super().__init__(message)


class ICMPError(ICMPLibError):
    '''
    Base class for ICMP error messages.

    '''
    def __init__(self, message, reply):
        super().__init__(message)
        self._reply = reply

    @property
    def reply(self):
        return self._reply


class DestinationUnreachable(ICMPError):
    '''
    Base class for ICMP Destination Unreachable messages.

    Destination Unreachable message is generated by the host or its
    inbound gateway to inform the client that the destination is
    unreachable for some reason.

    '''
    _CODES = {}

    def __init__(self, reply):
        if reply.code in self._CODES:
            message = self._CODES[reply.code]

        else:
            message = f'Destination unreachable, bad code: {reply.code}'

        super().__init__(message, reply)


class ICMPv4DestinationUnreachable(DestinationUnreachable):
    _CODES = {
        0:  'Destination network unreachable',
        1:  'Destination host unreachable',
        2:  'Destination protocol unreachable',
        3:  'Destination port unreachable',
        4:  'Fragmentation needed and DF set',
        5:  'Source route failed',
        6:  'Destination network unknown',
        7:  'Destination host unknown',
        8:  'Source host isolated',
        9:  'Destination network prohibed',
        10: 'Destination host prohibed',
        11: 'Destination network unreachable for ToS',
        12: 'Destination host unreachable for ToS',
        13: 'Packet filtered',
        14: 'Precedence violation',
        15: 'Precedence cutoff'
    }


class ICMPv6DestinationUnreachable(DestinationUnreachable):
    _CODES = {
        0:  'No route to destination',
        1:  'Communication with destination administratively prohibited',
        2:  'Beyond scope of source address',
        3:  'Address unreachable',
        4:  'Port unreachable',
        5:  'Source address failed ingress/egress policy',
        6:  'Reject route to destination'
    }


class TimeExceeded(ICMPError):
    '''
    Base class for ICMP Time Exceeded messages.

    Time Exceeded message is generated by a gateway to inform the
    source of a discarded datagram due to the time to live field
    reaching zero. A Time Exceeded message may also be sent by a host
    if it fails to reassemble a fragmented datagram within its time
    limit.

    '''
    _CODES = {}

    def __init__(self, reply):
        if reply.code in self._CODES:
            message = self._CODES[reply.code]

        else:
            message = f'Time exceeded, bad code: {reply.code}'

        super().__init__(message, reply)


class ICMPv4TimeExceeded(TimeExceeded):
    _CODES = {
        0:  'Time to live exceeded',
        1:  'Fragment reassembly time exceeded'
    }


class ICMPv6TimeExceeded(TimeExceeded):
    _CODES = {
        0:  'Hop limit exceeded',
        1:  'Fragment reassembly time exceeded'
    }
