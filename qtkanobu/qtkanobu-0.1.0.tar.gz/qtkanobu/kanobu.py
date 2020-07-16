def main():

    import random

    while True:

        bot = random.randint(0, 2)

        massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]

        i = 0
        for key in massive[player]:
            object = locale["objects"][bot]
            object = object if locale["lang"]["case"] is False else object.lower()

            if bot == i:

                print(message + " " + locale["bot"]["have"] + a + " " + object)

            i += 1
