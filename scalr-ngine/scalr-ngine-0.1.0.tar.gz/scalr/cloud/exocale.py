import os
import base64

from scalr.cloud import ScalrBase
from scalr.log import log

from cs import CloudStack


class ExoscaleScalr(ScalrBase):

    def __init__(self):
        super().__init__()
        self.cs = CloudStack(
            endpoint='https://api.exoscale.ch/v1',
            key=os.getenv('EXOSCALE_API_KEY'),
            secret=os.getenv('EXOSCALE_API_SECRET'),
        )

    def get_current(self) -> list:
        if self.current_servers is None:
            res = self.cs.listVirtualMachines(
                tags={
                    'scalr': self.name,
                },
                fetch_list=true,
            )
            self.current_servers = res.get('virtualmachine') or []
        return self.current_servers

    def ensure_running(self):
        for server in self.get_current():
            log.info(f"server {server['name']} status {server['state']}")
            if server['state'] in  ['stopping', 'stopped']:
                if not self.dry_run:
                    self.cs.startVirtualMachine(id=server['id'])
                    log.info(f"Server {server['name']} started")
                else:
                    log.info(f"Dry run server {server['name']} started")

    def _get_service_offering(self, name):
        res = self.cs.listServiceOfferings(name=name)
        if not res:
            raise Exception(f"Error: service offering not found: {name}")
        return res['serviceoffering'][0]

    def _get_zone(self, name):
        res = self.cs.listZones(name=name)
        if not res:
            raise Exception(f"Error: Zone not found: {name}")
        return res['zone'][0]

    def _get_template(self, name):
        res = self.cs.listTemplate(name=name)
        if not res:
            raise Exception(f"Error: Template not found: {name}")
        return res['template'][0]

    def scale_up(self, diff: int):
        log.info(f"scaling up {diff}")

        while diff > 0:
            lc = self.launch_config.copy()

            tags = lc.get('tags', {})
            tags.update({'scalr': self.name})

            params = {
                'name': self.get_unique_name(),
                'tags': tags,
                'serviceofferingid': self._get_service_offering(name=lc['service_offering']).get('id'),
                'affinitygroupnames': lc[.get('affinity_groups'),
                'securitygroupnames': lc.get('security_groups'),
                'templateid':  self._get_template(name=lc['templateid']).get('id'),
                'zoneid':  self._get_zone(name=lc['zone']).get('id'),
                'userdata':  base64.b64encode(lc['user_data'])
            }

            if not self.dry_run:
                server = self.cs.deployVirtualMachine(**params)
                log.info(f"Creating server name={name}")
            else:
                log.info(f"Dry run creating server name={name}")
            diff -= 1

    def scale_down(self, diff: int):
        log.info(f"scaling down {diff}")
        while diff > 0:
            server = self.get_selected_server()
            if not self.dry_run:
                self.cs.destroyVirtualMachine(id=server['id'])
                log.info(f"Deleting server id={server['id']}")
            else:
                log.info(f"Dry run deleting server id={server['id']}")
            diff -= 1
