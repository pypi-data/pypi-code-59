colors = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]


def spark(word):
    import random
    import time
    import sys
    for i in range(25):
        print("\033[{}m{}".format(random.choice(colors), word))
        time.sleep(0.1)
        sys.stdout.write('\033[2J\033[00H')

#谁会单字闪烁的私信我谢谢
