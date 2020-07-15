import shutil
import os

from git import Repo

from tokko_cli.conf import Settings

__all__ = [
    "clone_monorepo",
]


def clone_monorepo(user: str, access_token: str):
    print("Cloning Monorepo", end="\t...\t")
    settings = Settings(current_user=user)
    try:
        if os.listdir(settings.sources.monorepo_path):
            shutil.rmtree(settings.sources.monorepo_path)
            os.makedirs(settings.sources.monorepo_path, 0o777)
        Repo.clone_from(settings.sources.remote, settings.sources.monorepo_path)
        print("OK")
    except Exception as clone_error:
        raise IOError(f"Monorepo clone fails. {clone_error}") from clone_error
