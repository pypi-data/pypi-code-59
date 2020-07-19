from xingyunlib.pygame_set import clear_os
colors = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]


def spark(word):
    import random
    import time
    for i in range(25):
        print("\033[{}m{}".format(random.choice(colors), word))
        time.sleep(0.1)
        clear_os()

#谁会单字闪烁的私信我谢谢
