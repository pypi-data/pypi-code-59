'''malnet config'''
import os
import toml
import logging
from pathlib import Path

DBPATH = Path(__file__).parent.joinpath('data')

PRUD_CFG = DBPATH.joinpath('prud.conf')
DEV_CFG = DBPATH.joinpath('dev.conf')

log = logging.getLogger(__file__)


class Config:
    @classmethod
    def apply(self, cfg_path: os.PathLike):
        """apply cfg to prud.conf
        Args:
            cfg: prud config dict
        """
        cfg = toml.load(cfg_path)
        with open(PRUD_CFG, "w") as f:
            toml.dump(cfg, f)

    @classmethod
    def make(self, fpath: Path = None):
        """make example config
        """
        if fpath is None:
            cfg_path = Path(os.getcwd()).joinpath('malnet.conf')
        else:
            cfg_path = fpath

        default_cfg = toml.load(DEV_CFG)
        with open(cfg_path, "w") as f:
            toml.dump(default_cfg, f)

    @classmethod
    def get(self, item=None, cfg=PRUD_CFG):
        if not Path(cfg).exists():
            cfg = DEV_CFG
        cfg = toml.load(cfg)

        if item is None:
            return cfg
        else:
            return cfg.get(item)