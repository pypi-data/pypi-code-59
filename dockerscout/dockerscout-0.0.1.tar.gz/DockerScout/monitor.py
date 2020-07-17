"""
Monitor currently running docker containers so we can keep track of images to keep
"""
import sys
import argparse
import logging
import platform
import subprocess
import time
from threading import Thread
from . import memory, config, utils
from .disk import docker_disk_free


logging.root.setLevel(logging.INFO)
logging.root.name = "docker.scout.monitor"


def get_all_images():
    """
    Get a all images
    :return:
    """
    output = subprocess.check_output(["docker", "image", "ls", "-q", "-a", "--no-trunc", "--format={{.ID}}"]).decode()
    all_images = []
    for line in output.split("\n"):
        all_images.append(line.strip())

    return all_images


def clean(image):
    """
    Remove an image
    :param image:
    :return:
    """
    if image:
        logging.info("removing image {}".format(image))
        try:
            subprocess.check_call(["docker", "image", "rm", image])
            memory.forget(image)
            return True
        except Exception as err:
            logging.error("error in clean {}".format(err))
    return False


def resolve_image(image):
    """
    Get the local ID of an image
    :param image:
    :return:
    """
    try:
        output = subprocess.check_output(["docker", "image", "inspect", "--format", '{{.ID}}', image]).decode()
        return output.strip()
    except Exception as err:
        logging.error("error in resolve_image {}".format(err))
        return None


class ImageScanner(Thread):
    """
    Thread to scan for newly started images and clean up when the disk gets low on space
    """

    def __init__(self, touch, minfree):
        super(ImageScanner, self).__init__()
        self.touch = touch
        self.minfree = minfree

    def clean(self):
        """
        If disk space is below the limit, clean the oldest image
        :return:
        """
        space = docker_disk_free()
        if space < self.minfree:
            # only try to delete images not seen running in the last 2 mins
            only_delete_before = time.time() - 120

            logging.info("We are low on space ({}mb < {}mb)".format(space, self.minfree))
            # prune all stopped containers
            logging.info("Pruning stopped containers..")
            subprocess.call(["docker", "container", "prune", "-f"])

            # now clean images until we are above the limit or there are no more images
            current_images = get_all_images()
            history = memory.read_images()
            for image in current_images:
                if image not in history:
                    # we've not seen it run, destroy it
                    logging.info("Cleaning image {} (unseen)".format(image))
                    clean(image)
                if docker_disk_free() > self.minfree:
                    break

            # sort the images by last seen, and delete the oldest first and stop
            # when we delete at least one image
            least_used_first = sorted(history.items(), key=lambda x: x[1])
            for image, lastseen in least_used_first:
                if docker_disk_free() > self.minfree:

                    break
                if lastseen > only_delete_before:
                    break
                logging.info("Cleaning image {} (least used)".format(image))
                clean(image)

            logging.info("Cleaning done. {}Mb free".format(docker_disk_free()))

    def run(self):
        """
        Use 'docker monitor' to watch for containers being started and report the image used
        :return:
        """
        while True:
            logging.info("Starting docker events monitor")
            proc = subprocess.Popen(
                ["docker", "events",
                 "--filter", "Type=container",
                 "--format", "{{.Action}} {{.Actor.Attributes.image}}"],
                stderr=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stdin=subprocess.DEVNULL)

            while proc.poll() is None:
                line = proc.stdout.readline()
                if not line:
                    break
                try:
                    image = line.decode().strip()
                    action, image = image.split(" ", 1)
                    if action != "create":
                        continue
                    logging.debug("{} {}".format(action, image))

                    imageid = resolve_image(image)
                    logging.info("noticed image start {}".format(imageid))
                    if self.touch:
                        self.touch(imageid)

                    self.clean()
                except Exception as err:
                    logging.error("error touching image {}".format(err))

            proc.wait()


SYSTEMD_SERVICE = """
[Unit]
Description=Docker Scout Image Cleaner
After=multi-user.target
After=docker.service

[Service]
Type=simple
Environment=DOCKERSCOUT_DIR=/etc/docker-scout
ExecStart={cmdline}
StandardInput=tty-force
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=DockerScout

[Install]
WantedBy=multi-user.target

"""


def do_install(configfile):
    """
    Install as a system service
    :param configfile:
    :return:
    """

    cmdline = "{} -m DockerScout --config /etc/docker-scout.yml".format(sys.executable)

    if platform.system() == "Linux":
        with open("/etc/systemd/system/dockerscout.service", "w") as service:
            service.write(SYSTEMD_SERVICE.format(cmdline=cmdline))
        subprocess.check_call(["systemctl", "daemon-reload"])
        subprocess.check_call(["systemctl", "restart", "dockerscout"])

    elif platform.system() == "Windows":
        pass
    else:
        raise NotImplemented("Service install not supported on {}".format(platform.system()))


def run():
    """
    Monitor running images
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str,
                        metavar="CONFIG",
                        default=config.config_path(),
                        help="Specify a config file")
    parser.add_argument("--install", default=False,
                        action="store_true",
                        help="Install as a system service")

    opts = parser.parse_args()
    settings = config.read_config(opts.config)

    if opts.install:
        do_install(opts.config)
    else:
        logging.info("aiming for {} mb disk free".format(settings.min_disk()))
        mindisk = utils.space_suffix(str(settings.min_disk()))

        scanner = ImageScanner(memory.notice, mindisk)
        scanner.setDaemon(True)
        scanner.start()
        scanner.join()

