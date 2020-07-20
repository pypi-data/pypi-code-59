import argparse, logging


def input_config(message:str, default=''):
    data = input(message + "[%s]: "%default)
    if(data == ''):
        return default
    else:
        return data

def gen_mysql_config():
    config = {}
    try:
        tag_name = input_config('Tag Name', 'mysqldb')
        config['username'] = input_config('Username', 'root')
        config['password'] = input_config('Password', 'a123')
        config['host'] = input_config('Host', '127.0.0.1')
        config['port'] = input_config('Port', '3306')
        config['schema'] = input_config('Schema', 'database-name')
        config['minConnection'] = input_config('Min Connection', '1')
        config['maxConnection'] = input_config('Max Connection', '10')
    except KeyboardInterrupt as e:
        logging.error("\nProcess is killed by user!")
        return

    with open('config.ini', 'w+') as f:
        f.write("[%s]\n"%tag_name)
        for key, value in config.items():
            f.write("%s=%s\n"%(key,value))
