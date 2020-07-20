import subprocess

from pydantic import BaseModel

BLKID_COMMAND = "/sbin/blkid"


class Disk(BaseModel):
    name: str
    label: str
    type: str
    partuuid: str
    uuid: str


class BlkidException(Exception):
    def __init__(self, description, stdout, stderr):
        self.description = description
        self.stdout = stdout
        self.stderr = stderr


def blkid():
    def find_by_token(line: str, token: str):
        parts = line.split('"')
        for i, part in enumerate(parts):
            if part.endswith(f"{token}="):
                return parts[i + 1]
        return ""

    proc = subprocess.run([BLKID_COMMAND], capture_output=True)
    disks = []

    if proc.returncode == 0:
        stdout = proc.stdout.decode("utf-8", "strict")
        for line in stdout.splitlines():
            name = line.split(":")[0]
            label = find_by_token(line, "LABEL")
            type = find_by_token(line, "TYPE")
            partuuid = find_by_token(line, "PARTUUID")
            uuid = find_by_token(line, "UUID")
            disk = Disk(name=name, label=label, type=type, partuuid=partuuid, uuid=uuid)
            disks.append(disk)
    else:
        raise BlkidException(
            f"Invalid call to blkid: {BLKID_COMMAND}.", proc.stdout, proc.stderr
        )

    return disks
