from colorama import Style, Fore
import json as JSON

def iMonkeUrl():
    return "http://imonke.gastrodon.io/"

def raise_warning(args):
    message = Fore.YELLOW + "Warning: " + args + Style.RESET_ALL
    print(message)
    return

def headers(bearer=None, basic=None):
    header = {}
    if basic:
        header["Authorization"] = "Basic " + basic
    if bearer:
        header["Authorization"] = "Bearer " + bearer
    return header

def json():
    # Returns a json object
    return JSON