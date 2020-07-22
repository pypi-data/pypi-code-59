from threading import Lock
import logging
import docker

class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class DockerWrapper(metaclass=SingletonMeta):
    """
    Wrapper class for Docker SDKs
    """
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.docker_client = None
        self.dcli = None
        self.containers = []
        try:
            self.logger.info("Create DockerWrapper with default configuration (localhost)")
            self.docker_client = docker.from_env()
            self.dcli = self.docker_client.api
        except Exception as e:
            self.logger.error(e)

    def _check_cli(self):
        if not self.dcli:
            raise TypeError("Failed to initialize dcli api.")

    def create_container(self, name:str, image:str, command:str, **kwargs) -> {}:
        self._check_cli()
        """
        Create a Docker container based on input parameters
        :param name: desired name of the container
        :param image: chosen docker image for container
        :param command: command used for container
        :param kwargs: additional keyword arguments used to set up container
        :return: a dictionary contains status,message
        """
        container_id = None  # Id of this container
        container_info = None  # Information of this container
        # default configuration resource limits
        # default configuration resource limits
        defaults = {
            'cpu_quota': -1,
            'cpu_period': None,
            'cpu_shares': None,
            'cpuset_cpus': None,
            'mem_limit': None,
            'memswap_limit': None,
            'environment': {},
            'volumes': [],  # use ["/home/user1/:/mnt/vol2:rw"]
            'tmpfs': [],  # use ["/home/vol1/:size=3G,uid=1000"]
            'network_mode': None,
            'publish_all_ports': True,
            'port_bindings': {},
            'ports': [],
            'dns': [],
            'ipc_mode': None,
            'devices': [],
            'cap_add': [],
            'sysctls': {}
        }
        defaults.update(kwargs)

        # keep resource in a dict for easy update during container lifetime
        container_resources = dict(
            cpu_quota=defaults['cpu_quota'],
            cpu_period=defaults['cpu_period'],
            cpu_shares=defaults['cpu_shares'],
            cpuset_cpus=defaults['cpuset_cpus'],
            mem_limit=defaults['mem_limit'],
            memswap_limit=defaults['memswap_limit']
        )

        # set up default command for container
        container_command = command if command is not None else "/bin/sh"

        try:
            self.logger.info("Prepare to create container {}".format(name))

            # create host_config for container
            container_host_config = self.dcli.create_host_config(
                network_mode=defaults['network_mode'],
                binds=defaults['volumes'],
                tmpfs=defaults['tmpfs'],
                publish_all_ports=defaults['publish_all_ports'],
                port_bindings=defaults['port_bindings'],
                mem_limit=container_resources.get('mem_limit'),
                cpuset_cpus=container_resources.get('cpuset_cpus'),
                dns=defaults['dns'],
                ipc_mode=defaults['ipc_mode'],
                devices=defaults['devices'],
                cap_add=defaults['cap_add'],
                sysctls=defaults['sysctls']
            )

            # create new docker container
            container = self.dcli.create_container(
                name=name,
                image=image,
                command=container_command,
                entrypoint=list(),
                stdin_open=True,
                tty=True,
                environment=defaults['environment'],
                host_config=container_host_config,
                ports=defaults['ports'],
                volumes=[self._extract_volume_mount_name(path) for path in defaults['volumes'] if
                         self._extract_volume_mount_name(path) is not None],
                hostname=name
            )

            # start container
            self.dcli.start(container)
            self.logger.debug("Starting container {}".format(name))
            # fetch information about new container
            container_info = self.dcli.inspect_container(container)
            container_id = container_info.get("Id")

            # add to list of containers
            self.containers.append({'name': name,
                                    'id': container_id,
                                    'info': container_info})

            self.logger.info("Inspect container {} [{}]: {}".format(name,
                                                                    container_id,
                                                                    container_info))

            return {'status': True,
                    'msg': "Create container {} successfully. Id: {}".format(name, container_id),
                    'info': container_info}
        except Exception as e:
            self.logger.error("Exception raised! {}".format(str(e)))
            return {'status': False, 'msg': str(e)}

    @staticmethod
    def _extract_volume_mount_name(volume_path: str):
        """ Helper to extract mount names from volume specification paths"""
        parts = volume_path.split(":")
        if len(parts) < 3:
            return None
        return parts[1]