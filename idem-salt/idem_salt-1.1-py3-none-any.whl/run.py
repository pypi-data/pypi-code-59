import os
import shutil

idem_salt_root = os.path.dirname(__file__)
src_modules = os.path.join(idem_salt_root, "_modules")
src_states = os.path.join(idem_salt_root, "_states")

file_root = "/srv/salt/"
dest_modules = os.path.join(file_root, "_modules")
dest_states = os.path.join(file_root, "_states")


def install():
    os.makedirs(dest_modules, exist_ok=True)
    for s in os.listdir(src_modules):
        _, file_name = os.path.split(s)
        src = os.path.abspath(os.path.join(src_modules, s))
        dest = os.path.join(dest_modules, s)
        print(f"Copying module '{file_name}' from {src} to {dest}")
        shutil.copy(src, dest)
    os.makedirs(dest_states, exist_ok=True)
    for s in os.listdir(src_states):
        _, file_name = os.path.split(s)
        src = os.path.abspath(os.path.join(src_states, s))
        dest = os.path.join(dest_states, s)
        print(f"Copying module '{file_name}' from {src} to {dest}")
        shutil.copy(src, dest)
