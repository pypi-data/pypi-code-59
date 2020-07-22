#!/usr/bin/python
# Generate user config for Raptor
# Modified on 20200721
# jianwenzhou {at} aliyun.com


import os
import json
from getpass import getpass

def main():
    print(">>>  Welcome to raptor user info configuration  <<<")
    otp_info = {}
    
    output_direction = input("Enter file in which to save the key (./raptor.json):")
    otp_info['ip'] = input("Enter host ip address :")
    otp_info['user'] = input("Username :")
    otp_info['passwd'] = getpass("Password :")
    otp_info['otp_key'] = getpass("TOTP hash key :")
    
    with open(output_direction, 'w') as f:
        json.dump(otp_info,f, indent=4)        
        
    print("\nUsage : ")
    print("    from raptor import logger ")
    print('    ssh = logger("raptor.json") ')

if __name__ == '__main__':
    main()