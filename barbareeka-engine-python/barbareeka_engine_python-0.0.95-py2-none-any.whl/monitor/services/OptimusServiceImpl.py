from monitor.clients.BuildsClient import BuildsClient
from monitor.services.OptimusService import OptimusService


class OptimusServiceImpl(OptimusService):
    pass

    def get_latest_id(self):
        return BuildsClient().get_latest_build_id()
