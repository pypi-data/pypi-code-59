#!/usr/bin/python
# Raptor, reeve time-based one time password ahead rapidly
# Modified on 20200721
# jianwenzhou {at} aliyun.com

import json
import pyotp
import paramiko
from getpass import getpass


def my_handler(title, instructions, prompt_list):
    if prompt_list == [('Password: ', False)]:
        return [logger.otp_info["passwd"]]
    
    if prompt_list == [('Verification code: ', False)]:
        gtoken = logger.otp_info["otp_key"]
        totp= pyotp.TOTP(gtoken)
        return [str(totp.now())]
    
    return ([getpass(prompt) for (prompt, echo) in prompt_list])
    

def logger(config_file):
    with open(config_file) as f:
        logger.otp_info = json.load(f)
        
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())        
    
    try:
        ssh.connect(logger.otp_info["ip"], username=logger.otp_info["user"])
    except paramiko.ssh_exception.SSHException:
        pass
       
    ssh.get_transport().auth_interactive(username=logger.otp_info["user"], handler=my_handler)
    return ssh

if __name__ == '__main__':
    ssh_test = logger("cngb.json")
    stdin,stdout, stderr= ssh_test.exec_command("ls /")
    print(stdout.readlines())
    ssh_test.close