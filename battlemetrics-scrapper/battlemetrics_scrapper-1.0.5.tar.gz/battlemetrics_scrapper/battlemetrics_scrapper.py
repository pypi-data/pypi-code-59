import requests
import json
import csv
import datetime
import os
from iso3166 import countries
import time
"""
This tool scrap Battle metrics (steam game server statistics)
it return a dictionnary for a given country if used as a module.
alternatively it can be used in standalone and will scrap all iso country and save the result in a csv
and store in a csv the number of server up, down, off and the number of player for each country
@author ARamushi, NMorand
"""
########################################################################################################################
### the goal of this programme is to parse all the server on battle metrics, and for each country
### have the number of player, know how many server are offline and how many still up
### all the data generated all stored in a csv file with country,server_up,server_down, server_dead,pourcentage,players
########################################################################################################################

# https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements
# link to have language

class battlemetrics:
    def get_latest_gameserverstat_country(country_iso_code, saveascsv=None):
        """
        This function scrap Battle metrics server to get the number of server and player in the requested country.
        :param country_iso_code: the iso code of the country you want to get the data from
        :param saveascsv: provide the path the file if you want the data to be saved as CSV
        the CSV contains line like this: each line is a datapoint
            2020-07-09 13:33:50,AT,76,38,93,66.67,116
            1)  value is the date and time in the local format (where the script is ran)
            2)  is the country code (AT = austria) in iso3166
            3)  value is the number of server up
            4)  is the number of server down / off
            5)  is the number of server dead
            6)  is ratio of online server over the online and off server
            7) is the number of player connected to the country's server
        :return:
        it return a dictionnary with the value, here are the key
            countryISO -> the ISO code of the country we scrapped (EX : AT) (string)
            countryname -> the human name of the country (EX : Austria) (string)
            timestamp -> timestamp in YYYY-MM-DD HH:MM:SS format EX : 2015-10-21 19:28:50 (string)
            serverup -> number of server up (EX : 69) (int)
            serverdown -> number of server down (EX : 42) (int)
            serverdead -> number of server dead (EX : 666) (int)
            ratioupdown -> % of server up by the sum of server up and down (EX : 77) (int)
            player -> number of player connected on the country's server (EX : 1337) (int)
        """
        startedat = time.time() # used to monitor the speed at which the data are retrieved
        nbrequest = 0  # we need it because for battle metrics allow only 60 request per minute
        start_time = time.time()
        i = 0 # number of time in a row an error occurend
        stat = {} # hold the statistics that are returned about server of a country
        country = country_iso_code
        while True:
            try:
                # initliatisation of counters
                ServerUP = [] # number of server that are UP
                ServerDOWN = [] # number of server that are down usually temporary
                ServerDEAD = [] # number of server that are dead and will not come back online
                ServerID = []
                playercounter = 0
                # we are allow to make max 60 request on battle metrics every 60 secondes so we need to keep a counter of request
                if nbrequest >= 55:
                    if (time.time() - start_time) < 60:
                        time.sleep(60)
                    start_time = time.time()
                    print()
                    nbrequest = 0
                else:
                    ############# look for server up ################
                    paramsON = (
                        ('filter[status]', 'online'),
                        ('filter[countries][]', country[1]),
                        ('page[size]', '100'),
                    )
                    # send a request with the param
                    responseON = requests.get('https://api.battlemetrics.com/servers', params=paramsON)
                    nbrequest += 1
                    #parse data
                    for data in json.loads(responseON.content)["data"]:
                        ServerUP.append(data["attributes"]["ip"])
                        ServerID.append(data["id"])
                    ServerUP = list(set(ServerUP))
                    print("number of server UP ", len(ServerUP), "in ", country[0])

                    ############# look for server OFF ################
                    paramsOFF = (
                        ('filter[status]', 'offline'),
                        ('filter[countries][]', country[1]),
                        ('page[size]', '100'),
                    )
                    # send a request with the param
                    responseOFF = requests.get('https://api.battlemetrics.com/servers', params=paramsOFF)
                    nbrequest += 1
                    # parse data
                    for data in json.loads(responseOFF.content)["data"]:
                        ServerDOWN.append(data["attributes"]["ip"])
                    ServerDOWN = list(set(ServerDOWN))
                    print("number of server down ", len(ServerDOWN), "in ", country[0])

                    ############# look for server dead ################
                    paramsDEAD = (
                        ('filter[status]', 'dead'),
                        ('filter[countries][]', country[1]),
                        ('page[size]', '100'),
                    )
                    # send a request with the param
                    responseDEAD = requests.get('https://api.battlemetrics.com/servers', params=paramsDEAD)
                    nbrequest += 1
                    # parse data
                    for data in json.loads(responseDEAD.content)["data"]:
                        ServerDEAD.append(data["attributes"]["ip"])
                    ServerDEAD = list(set(ServerDEAD))
                    print("number of server dead ", len(ServerDEAD), "in ", country[0])

                    ############# % of server up ################

                    if len(ServerDOWN) > 0:
                        pourcentage = round(float((len(ServerUP)) / float((len(ServerUP) + len(ServerDOWN)))) * 100, 2)
                    elif len(ServerUP) > 1:
                        pourcentage = 100
                    else:
                        pourcentage = 0

                    print("% of the server up currently : ", pourcentage, "% in", country[0])

                    ############# player on the country's server ################
                    playercounter = 0
                    for data in ServerID:
                        # print("nb de requet ", nbrequest)
                        if nbrequest >= 55:
                            if (time.time() - start_time) < 60:
                                time.sleep(60)
                            start_time = time.time()
                            print()
                            nbrequest = 0
                        else:
                            while True:
                                try:
                                    responseByID = requests.get('https://api.battlemetrics.com/servers/' + data)
                                    # print(responseByID)
                                    # print(json.loads(responseByID.content))
                                    playercounter += int(json.loads(responseByID.content)["data"]["attributes"]["players"])
                                except:
                                    time.sleep(60)
                                    nbrequest = 0
                                break

                        nbrequest += 1
                    print("they are ", playercounter, "players on ", country[0])
                    # print(playercounter)
                    timestamp = str(datetime.datetime.now())[:-7]
                    stat["countryISO"] = country[1]
                    stat["countryname"] = country[0]
                    stat["timestamp"] = timestamp
                    stat["serverup"] = len(ServerUP)
                    stat["serverdown"] = len(ServerDOWN)
                    stat["serverdead"] = len(ServerDEAD)
                    stat["ratioupdown"] = pourcentage
                    stat["player"] = playercounter
                    if saveascsv is not None:
                        csvfile = open(saveascsv, "a", newline="")
                        BMlogs = [[timestamp, country[1], len(ServerUP), len(ServerDOWN), len(ServerDEAD), pourcentage, playercounter]]
                        with csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerows(BMlogs)
                        csvfile.close()
                    i = 0 # reset the crash counter if everything went fine
                    break # leave the while loop once we got what we wanted
            except:
                i = i + 1
                if i < 3:
                    print("an error occured, retrying in 60 secondes")
                    time.sleep(60)
                    nbrequest = 0
                else:
                    print("waiting was not enough, please investigate the issue")
                    break
        print("it took %s seconds" % (time.time() - startedat))
        return stat

    def get_latest_gameserverstat_world():
        """
        This function scrap Battle metrics server to get the number of server and player in every country.
        the CSV contains line like this: each line is a datapoint. the csv are stored in a folder called "scrapResult"
            2020-07-09 13:33:50,AT,76,38,93,66.67,116
            1)  value is the date and time in the local format (where the script is ran)
            2)  is the country code (AT = austria) in iso3166
            3)  value is the number of server up
            4)  is the number of server down / off
            5)  is the number of server dead
            6)  is ratio of online server over the online and off server
            7) is the number of player connected to the country's server
        """
        if not os.path.exists("scrapResult"):
            os.makedirs("scrapResult")
        startedat = time.time()
        nbrequest = 0  # we need it because for battle metrics you can make only 60 every 1 minute (and we make some before)
        start_time = time.time()
        total = len(countries)
        i = 0

        for country in countries:
            i = i + 1
            while True:
                try:
                    # initliatisation of counters
                    ServerUP = []
                    ServerDOWN = []
                    ServerDEAD = []
                    ServerID = []
                    playercounter = 0
                    print("")
                    print("#######################################")
                    # we are allow to make max 60 request on battle metrics every 60 secondes so we need to keep a counter of request
                    if nbrequest >= 55:
                        print()
                        print("ran for %s seconds" % (time.time() - start_time))
                        if (time.time() - start_time) < 60:
                            print("API need a break ;), pausing for " + str(60 ))
                            time.sleep(60)
                        start_time = time.time()
                        print()
                        nbrequest = 0
                    else:
                        print("scrapping", country[0], "(", country[1], ")")
                        ############# look for server up ################
                        paramsON = (
                            ('filter[status]', 'online'),
                            ('filter[countries][]', country[1]),
                            ('page[size]', '100'),
                        )
                        # send a request with the param
                        responseON = requests.get('https://api.battlemetrics.com/servers', params=paramsON)
                        nbrequest += 1
                        #parse data
                        for data in json.loads(responseON.content)["data"]:
                            ServerUP.append(data["attributes"]["ip"])
                            ServerID.append(data["id"])
                        ServerUP = list(set(ServerUP))
                        print("number of server UP ", len(ServerUP), "in ", country[0])

                        ############# look for server OFF ################
                        paramsOFF = (
                            ('filter[status]', 'offline'),
                            ('filter[countries][]', country[1]),
                            ('page[size]', '100'),
                        )
                        # send a request with the param
                        responseOFF = requests.get('https://api.battlemetrics.com/servers', params=paramsOFF)
                        nbrequest += 1
                        # parse data
                        for data in json.loads(responseOFF.content)["data"]:
                            ServerDOWN.append(data["attributes"]["ip"])
                        ServerDOWN = list(set(ServerDOWN))
                        print("number of server down ", len(ServerDOWN), "in ", country[0])

                        ############# look for server dead ################
                        paramsDEAD = (
                            ('filter[status]', 'dead'),
                            ('filter[countries][]', country[1]),
                            ('page[size]', '100'),
                        )
                        # send a request with the param
                        responseDEAD = requests.get('https://api.battlemetrics.com/servers', params=paramsDEAD)
                        nbrequest += 1
                        # parse data
                        for data in json.loads(responseDEAD.content)["data"]:
                            ServerDEAD.append(data["attributes"]["ip"])
                        ServerDEAD = list(set(ServerDEAD))
                        print("number of server dead ", len(ServerDEAD), "in ", country[0])

                        ############# % of server up ################

                        if len(ServerDOWN) > 0:
                            pourcentage = round(float((len(ServerUP)) / float((len(ServerUP) + len(ServerDOWN)))) * 100, 2)
                        elif len(ServerUP) > 1:
                            pourcentage = 100
                        else:
                            pourcentage = 0

                        print("% of the server up currently : ", pourcentage, "% in", country[0])

                        ############# player on the country's server ################
                        playercounter = 0
                        for data in ServerID:
                            # print("nb de requet ", nbrequest)
                            if nbrequest >= 55:
                                print()
                                print("ran for %s seconds" % (time.time() - start_time))
                                if (time.time() - start_time) < 60:
                                    print("API need a break ;), pausing for " + str(60))
                                    time.sleep(60)
                                start_time = time.time()
                                print()
                                nbrequest = 0
                            else:
                                while True:
                                    try:
                                        responseByID = requests.get('https://api.battlemetrics.com/servers/' + data)
                                        # print(responseByID)
                                        # print(json.loads(responseByID.content))
                                        playercounter += int(json.loads(responseByID.content)["data"]["attributes"]["players"])
                                    except:
                                        print("")
                                        print("API need a break ;), pausing for " + str(60))
                                        time.sleep(60)
                                        nbrequest = 0
                                    break

                            nbrequest += 1
                        print("they are ", playercounter, "players on ", country[0])
                        # print(playercounter)

                        filelink = os.path.join("scrapResult", country[0] + ".csv")
                        csvfile = open(filelink, "a", newline="")
                        timestamp = str(datetime.datetime.now())[:-7]
                        # title of cvs, this cod just append to the csv file, the head with title has to be done before
                        BMlogs = [[timestamp, country[1], len(ServerUP), len(ServerDOWN), len(ServerDEAD), pourcentage, playercounter]]
                        with csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerows(BMlogs)
                        csvfile.close()
                    print("%s seconds so far" % (time.time() - startedat))
                    print("reviewed " + str(i) + "out of " + str(total) + " countrys")
                except:
                    print("")
                    print("API need a break ;), pausing for " + str(60))
                    time.sleep(60)
                    nbrequest = 0
                break
        print("it took %s seconds" % (time.time() - startedat))

def main():
    battlemetrics.get_latest_gameserverstat_world() # scrap the number of player in each country and save them in a CSV

if __name__ == "__main__":
    # execute only if run as a script
    main()
