# -*- coding: utf-8 -*-
"""
ekca_client.sshinit - the command-line client for EKCA service
"""

#---------------------------------------------------------------------------
# Imports
#---------------------------------------------------------------------------

# from Python's standard library
import sys
import os
import re
import getpass
import subprocess
import uuid
import json
import time

# from PyNaCl package
import nacl.utils
import nacl.encoding
import nacl.public

# external modules
if sys.platform == 'win32':
    import win32com.client
else:
    import ptyprocess

# internal imports from own package
from .cmd import SSH_ADD_WAIT
from .cfg import read_config, check_ca_certs
from .req import EKCAUserCertRequest

# List of directories with volatile storage backend or
# at least restricted to personal use.
# The first directory found is used for storing temporary files
if sys.platform == 'win32':
    TMPFS_LOCATIONS = []
else:
    TMPFS_LOCATIONS = [os.path.join('/run/user', str(os.getuid()))]
TMPFS_LOCATIONS.extend([
    '/tmp',
    os.environ.get('TMP', os.environ.get('TEMP', os.path.expanduser('~'))),
])


def remove_file(path):
    """
    overwrite file before removing it
    """
    old_size = os.stat(path).st_size
    with open(path, 'ab') as fileobj:
        fileobj.seek(0)
        fileobj.write(os.urandom(old_size))
    os.remove(path)
    print('Removed file', path)


def remove_temp_files(ssh_init_path, ssh_key_filename, ssh_cert_filename):
    """
    Remove temporary cert/key files
    """
    if sys.platform != 'win32':
        # on non-Windows systems the temporary files are not needed
        # => remove them immediately
        remove_file(ssh_key_filename)
        remove_file(ssh_cert_filename)
    # clean up stale files older than a day from former runs (especially needed on Windows)
    current_time = time.time()
    with os.scandir(ssh_init_path) as stale_files:
        for dir_entry in stale_files:
            if dir_entry.stat().st_mtime <= current_time - 86400:
                remove_file(os.path.join(ssh_init_path, dir_entry.name))
    # end of remove_temp_files()


def prepare_ssh_init_path():
    """
    search for temporary storage directory and create extra directory within
    """
    for ssh_init_tmpfs in TMPFS_LOCATIONS:
        if os.path.isdir(ssh_init_tmpfs):
            break
    ssh_init_path = os.path.join(ssh_init_tmpfs, '.ekca-ssh-init')
    if not os.path.exists(ssh_init_path):
        os.mkdir(ssh_init_path, mode=0o700)
    else:
        os.chmod(ssh_init_path, 0o700)
    return ssh_init_path


def ask_password_and_otp(cfg, user_name):
    """
    interactively get the user's password and OTP
    """
    # User input could be interrupted by Ctrl+C
    # => wrap it in try-except for exit without traceback
    try:
        # ask user for non-empty password
        while True:
            password = getpass.getpass('Password for user %r' % (user_name))
            if password:
                break
            sys.stdout.write('Empty password, please repeat...\n')
        # ask user for non-empty OTP
        while True:
            otp_value = getpass.getpass('OTP for user %r' % (user_name))
            if otp_value and re.fullmatch(cfg['otp_regex'], otp_value, flags=0):
                break
            if not otp_value:
                sys.stdout.write('Empty OTP, please repeat...\n')
            else:
                sys.stdout.write(
                    'Malformed OTP did not match %r, please repeat...\n' % (cfg['otp_regex'])
                )
    except KeyboardInterrupt:
        print('\nAborted by user -> exiting...')
        sys.exit(0)

    return password, otp_value
    # end of ask_password_and_otp()


def ssh_add(cfg, ssh_cert_filename, ssh_key_filename, passphrase, validity):
    """
    Invoke ssh-add command to load user cert and private key into ssh-agent.
    """

    # display the received cert
    subprocess.check_call([cfg['ssh_keygen'], '-L', '-f', ssh_cert_filename])
    # remove all existing keys from SSH key agent
    subprocess.check_call([cfg['ssh_add'], '-D'])

    # now add the private key and cert to ssh-agent
    # sending password to interactive password prompt
    ssh_add_cmd = [cfg['ssh_add']]
    if sys.platform != 'win32':
        ssh_add_cmd.extend(['-t', validity])
    ssh_add_cmd.append(ssh_key_filename)
    print('Adding new key with following command:', repr(ssh_add_cmd))

    if sys.platform == 'win32':
        # on Windows we use WSH
        proc = win32com.client.Dispatch('WScript.Shell')
        proc.run(' '.join(ssh_add_cmd))
        proc.AppActivate('ssh-add to agent')
        time.sleep(SSH_ADD_WAIT)
        proc.SendKeys(passphrase.decode('ascii')+'{ENTER}')
    else:
        # on Mac OS X or Linux we use PTY
        proc = ptyprocess.PtyProcess.spawn(ssh_add_cmd)
        pw_prompt = proc.read(3000)
        print('-->', pw_prompt.decode('ascii'))
        proc.waitnoecho()
        print('--> echo disabled')
        print('<-- send decrypted passphrase')
        proc.write(passphrase+proc.crlf)
        # we MUST consume CLI output here on Mac OS X
        _ = proc.read(3000)
        proc.sendeof()
        time.sleep(SSH_ADD_WAIT)
        proc.close()

    # this only lists loaded key and cert as final check
    try:
        subprocess.check_call([cfg['ssh_add'], '-l'])
    except subprocess.CalledProcessError:
        pass
    else:
        print('Successfully added key and cert to SSH key agent.')

    # end of ssh_add()


def sshinit():
    """
    the main CLI function
    """

    # read the configuration file
    cfg = read_config()
    check_ca_certs(cfg)

    if sys.platform == 'win32':
        # TODO: How to check whether ssh-agent service is running?
        pass
    elif 'SSH_AUTH_SOCK' not in os.environ:
        print('No SSH key agent found!')
        sys.exit(1)

    try:
        user_name = sys.argv[1]
    except IndexError:
        user_name = getpass.getuser()

    # make sure a local directory is present to store the temporary key and cert
    ssh_init_path = prepare_ssh_init_path()

    # interactively ask user for password and OTP
    password, otp_value = ask_password_and_otp(cfg, user_name)

    # generate a key identifier
    req_id = str(uuid.uuid4())

    # generate temporary enrollment key pair
    enroll_key = nacl.public.PrivateKey.generate()

    # send the request to EKCA service and parse the response
    err = None
    print('Sending signing request...')
    try:
        resp = EKCAUserCertRequest(
            cfg['baseurl'],
            cfg['sshca_name'],
            username=user_name,
            password=password,
            reqid=req_id,
            otp=otp_value,
            epubkey=enroll_key.public_key.encode(
                encoder=nacl.encoding.URLSafeBase64Encoder
            ).decode('ascii'),
        ).req(cafile=cfg['ca_certs'])
        resp_body = resp.read().decode('utf-8')
        resp_data = json.loads(resp_body)
        resp_msg = resp_data.get('message', '')
        if resp.status != 200:
            print('{0}: {1}'.format(resp.status, resp_msg))
            sys.exit(1)
        if req_id != resp_data['reqid']:
            print('Expected request ID {0} but received {1}'.format(req_id, resp_data['reqid']))
            sys.exit(1)
    except Exception as err:
        print('Exception: ', str(err))
        sys.exit(1)

    # the full pathname where to store private key (also prefix for cert filename)
    ssh_key_filename = os.path.join(ssh_init_path, req_id)
    ssh_cert_filename = ssh_key_filename + '-cert.pub'
    # store passphrase-proteced private key
    with open(ssh_key_filename, mode='wt', encoding='utf-8') as fileobj:
        fileobj.write(resp_data['key'])
    os.chmod(ssh_key_filename, mode=0o600)
    # store SSH cert
    with open(ssh_cert_filename, mode='wt', encoding='utf-8') as fileobj:
        fileobj.write(resp_data['cert'])
    os.chmod(ssh_cert_filename, mode=0o600)

    # decrypt passphrase
    unseal_box = nacl.public.SealedBox(enroll_key)
    passphrase = unseal_box.decrypt(
        resp_data['passphrase'],
        nacl.encoding.URLSafeBase64Encoder,
    )

    try:
        ssh_add(cfg, ssh_cert_filename, ssh_key_filename, passphrase, resp_data['validity'])
    finally:
        remove_temp_files(ssh_init_path, ssh_key_filename, ssh_cert_filename)

    # end of sshinit()


if __name__ == '__main__':
    sshinit()
