from .collector_info import CollectorInfo
from .vrm_type import VrmType

class ProbeInit(object):
    """
    System packet that will be encapsulated inside an UDP packet
    and broadcast to all worker hosts inside a single network segment
    """
    def __init__(self, packet_id: str, info: 'CollectorInfo', packet_type: 'VrmType'):
        self.id = packet_id
        self.info = info
        self.type = packet_type

    def __str__(self):
        return "[{}] {} - {}".format(str(self.type), id, str(self.info))

    def __repr__(self):
        return "{}({} - {})".format(self.__class__.__name__,
                                    id,
                                    str(self.info))
