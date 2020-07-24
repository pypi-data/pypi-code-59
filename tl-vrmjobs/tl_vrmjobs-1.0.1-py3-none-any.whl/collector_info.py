class CollectorInfo(object):
    """
    Define structure of the information of a collector host that
    will be exchanged via probe_init packet
    """
    def __init__(self, ip_addr:str, port: int):
        self.ip_addr = ip_addr
        self.port = port

    def __str__(self):
        return "{}:{}".format(self.ip_addr, self.port)

    def __repr__(self):
        return "{}({}:{})".format(self.__class__.__name__, self.ip_addr, self.port)