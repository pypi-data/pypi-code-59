import random
from urllib.request import urlopen

USCrimeList = urlopen("https://raw.githubusercontent.com/Ocramoi/USCrimes/master/CRIMES.txt")\
              .read().decode('utf-8').split("\n")
total = len(USCrimeList)


def randomCrime():
    return USCrimeList[random.randint(0, total - 1)]


def searchCrime(keyword):
    search_list = []
    search_total = 0

    for crime in USCrimeList:
        if keyword.lower() in crime.lower():
            search_list.append(crime)
            search_total += 1

    if total > 0:
        return search_list[random.randint(0, search_total - 1)]

    return 1
