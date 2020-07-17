import json

from powerfuldeveloper_base.commands import Command


class Docker(Command):

    def _json_format(self, *command):
        command = list(command)
        command.extend(['--format', '{{json .}},'])
        return self._docker(*command)

    def _get_result(self, popen):
        return popen.communicate()

    def _with_json_result(self, *command):

        p = self._json_format(*command)
        """popen instance"""

        r = self._get_result(p)
        """ results """

        rs: str = r[0].decode('utf-8').strip()
        """ result string """

        if rs.endswith(','):
            rs = rs[:len(rs) - 1]

        rs = '[%s]' % rs

        rs = json.loads(rs)

        return rs, p

    def _list_ables(self, what):
        assert self.is_docker_available
        j, _ = self._with_json_result(what)
        return j

    def _docker(self, *command):
        return self.exec('docker', *command)

    @property
    def is_docker_available(self):
        try:
            self._docker()
            return True
        except:
            return False

    def images(self):
        return self._list_ables('images')

    def ps(self):
        return self._list_ables('ps')

    def start(self, container):
        assert self.is_docker_available
        return self._docker('start', container)

    def stop(self, container):
        assert self.is_docker_available
        return self._docker('stop', container)

    def kill(self, container):
        assert self.is_docker_available
        return self._docker('stop', container)

    def rm(self, container):
        assert self.is_docker_available
        return self._docker('rm', container)

    def rmi(self, image_id):
        assert self.is_docker_available
        return self._docker('rmi', image_id)
