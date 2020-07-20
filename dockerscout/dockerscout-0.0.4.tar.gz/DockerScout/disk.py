import os
import subprocess


def docker_lib_path():
    """
    Get the path to the docker lib folder
    :return:
    """
    output = subprocess.check_output(["docker", "info", "--format={{.DockerRootDir}}"]).decode()
    return output


def docker_disk_free():
    """
    Return the amount of space free on docker's main fs in MB
    :return:
    """
    folder = docker_lib_path().strip()
    if os.path.exists(folder):
        if os.path.islink(folder):
            folder = os.readlink(folder)

        statvfs = os.statvfs(folder)
        return int((statvfs.f_frsize * statvfs.f_bavail) / 1024 / 1024)
    return -1

