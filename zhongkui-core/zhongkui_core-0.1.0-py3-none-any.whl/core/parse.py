import logging
import json
from subprocess import Popen, PIPE, TimeoutExpired
from pathlib import Path
from typing import Dict

from .exception import ZhongkuiParseError

log = logging.getLogger(__name__)


def exiftool(target: Path) -> Dict[str, str]:
    '''exiftool scan target
    Args:
        target: A Path to target file
    Raise:
        ZhongkuiParseError
    Return:
        A dict result
    '''
    # ? http://owl.phy.queensu.ca/~phil/exiftool/exiftool_pod.html#Input-output-text-formatting
    # -charset [[TYPE=]CHARSET]        Specify encoding for special characters
    # -j[[+]=JSONFILE] (-json)         Export/import tags in JSON format
    args = ('exiftool', '-charset', 'utf-8', '-json', target)
    proc = Popen(args, stdout=PIPE)
    try:
        stdout, stderr = proc.communicate(timeout=15)
    except TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()

    if stderr:
        log.error("exiftool stderr: {}".format(stderr))

    try:
        stdout = stdout.decode('utf-8', errors='ignore')
        results = json.loads(stdout)[0]
    except Exception as e:
        log.error("exiftool json load error: {}".format(e))
        raise ZhongkuiParseError("exiftool json loads error: {}".format(e))

    ignores = [
        'SourceFile', 'ExifToolVersion', 'FileName', 'Directory',
        'FilePermissions', 'ImageFileCharacteristics'
    ]

    nulls = ('', '(none)')

    # filter results
    for k, v in results.items():
        if v in nulls:
            ignores.append(k)

    for key in ignores:
        results.pop(key, [])
        
    return results