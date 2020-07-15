import os
import logging
import shutil
import zipfile
from typing import Generator, Tuple
from pathlib import Path

from malnet.core import MalnetCriticalError

from .utils import md52Bucket, md52Object

log = logging.getLogger(__name__)


class MalnetFS(object):
    """malnet FS

    Args:
        root_path: (pathLike): fs path
    """
    def __init__(self, root_path):
        if not Path(root_path).exists():
            raise ValueError("root_path is not exists")

        self.root_path = root_path

    def getOrCreatePath(self, file_md5, root_path=None) -> Tuple:
        """get or create target in MalnetFS
        
        Args:
            file_md5 (str): target file md5
            root_path (pathLike, optional): [description]. Defaults to None.
        
        Raises:
            ValueError: invalid root_path
        
        Returns:
            Tuple (is_create<bool>, PathLike)
        """
        if root_path is not None:
            if not Path(root_path).exists():
                raise ValueError("root_path is not exists")
        else:
            root_path = self.root_path

        archive_dir = Path(root_path).joinpath(md52Bucket(file_md5))
        archive_path = Path(root_path).joinpath(md52Object(file_md5))
        if archive_path.exists():
            return (False, archive_path)

        if not archive_dir.exists():
            try:
                os.makedirs(str(archive_dir), mode=0o755)
            except OSError as e:
                log.error(f"makedirs {archive_dir} error: {e}")
                raise

        return (True, archive_path)

    def upload(self, origin_path, file_md5) -> Tuple:
        is_create, dest_path = self.getOrCreatePath(file_md5)

        success = False
        if not is_create:
            success = True
            return (success, dest_path)

        try:
            shutil.copy(origin_path, dest_path)
            success = True
        except BaseException as e:
            log.error(f"MalnetFS upload {origin_path} faced error: {e}")
            return (success, dest_path)

        return (success, dest_path)

    def delete(self, file_md5, path=None):
        is_create, dest_path = self.getOrCreatePath(file_md5)

        success = False
        if is_create:
            success = True
            return success

        try:
            os.remove(dest_path)
            success = True
        except BaseException as e:
            log.error(f"MalnetFS delete {dest_path} error {e}")
            return success

        return success


class CollectFS(object):
    @classmethod
    def walk(self, collect_path) -> Generator:
        '''collect sample from collect_path, by defalut
        `root_path/domain/package/*`

        Return
            Generator of Tuple value (<domain>, <package>, [<sample_path_list>])
        '''

        for root, dirs, files in os.walk(collect_path):
            if len(files) != 0:
                pkg_path = Path(root)
                package = pkg_path.name
                domain = pkg_path.parent.name
                sample = [pkg_path.joinpath(i) for i in files]
                yield (domain, package, sample)

    @classmethod
    def delete(self, fpath) -> bool:
        '''
        Raise MalnetCriticalError
        Return True
        '''
        try:
            os.remove(fpath)
        except BaseException as e:
            raise MalnetCriticalError(f"CollectFS delete {fpath} error {e}")

        return True

    @classmethod
    def unzip(self, src, dest, password=None):
        f = zipfile.ZipFile(src)
        f.extractall(path=dest, pwd=bytes(password, 'utf-8'))
