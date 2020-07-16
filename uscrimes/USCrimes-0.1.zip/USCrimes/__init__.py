import USCrimes.core

print("The list of atrocities commited by the US used in this library can be found in "
      "'https://github.com/dessalines/essays/blob/master/us_atrocities.md'\n")


def randomCrime():
    return USCrimes.core.randomCrime()


def searchCrime(keyword):
    return USCrimes.core.searchCrime(keyword)
