import requests


def request_basement():
    resp = requests.get("https://www.jeremyberman.org").json()
    print("resp", resp["Hello"])


print("THANKS BEING DONNEE")
