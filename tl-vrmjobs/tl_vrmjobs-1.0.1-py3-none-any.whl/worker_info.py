class WorkerInfo(object):
    """
    Define structure of the information of a worker host that
    will be exchanged via probe_ack packet
    """
    def __init__(self, ip_addr:str, port: int, hostname: str, exporter_info: {}):
        self.ip_addr = ip_addr
        self.port = port
        self.hostname = hostname
        self.exporter_info = exporter_info

    def __str__(self):
        return "{}[{}:{}] - exporters: {}".format(self.hostname,
                                                  self.ip_addr,
                                                  self.port,
                                                  self.exporter_info)

    def __repr__(self):
        return "{}({}[{}:{}] - exporters: {})".format(self.__class__.__name__,
                                                      self.hostname,
                                                      self.ip_addr,
                                                      self.port,
                                                      self.exporter_info)