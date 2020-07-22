import os


def auth_user():
    '''user identifying.'''
    global users
    #refer  configure of home
    home = os.path.expanduser('~')
    if os.path.isfile(os.path.join(home, '.talert','config')):
        with open(os.path.join(home, '.talert','config')) as f:
            chat_id = f.readline().rstrip()
    else:
        chat_id = input("Please let me know your chat_id : ")
        os.makedirs(os.path.join(home, '.talert'), exist_ok = True)  # make configure folder
        with open(os.path.join(home, '.talert','config'),'w') as f:   # save user chat_id
            f.write(chat_id)



    return None, chat_id

def set_id(chat_id):
    chat_id = input("Please let me know your chat_id : ")
    os.makedirs(os.path.join(home, '.talert'), exist_ok = True)  # make configure folder
    with open(os.path.join(home, '.talert','config'),'w') as f:   # save user chat_id
        f.write(chat_id)
