#!/usr/bin/env python

import logging
logging.basicConfig(level=logging.DEBUG)

# import dateutil.parser
#
# from cbapi.psc.threathunter import CbThreatHunterAPI
# from cbapi.psc.threathunter import Watchlist, Report, Feed
#
# cb = CbThreatHunterAPI(profile="eap01")
#
# watchlist=[wl for wl in cb.select(Watchlist) if wl.name == "ATT&CK >8"][0]
#
# if watchlist.classifier:
#     feed=cb.select(Feed, watchlist.classifier['value'])
#     reports=feed.reports
# else:
#     reports=watchlist.reports
#     print("Length of 'report_ids': {}".format(len(watchlist.report_ids)))
#
# print("Length of 'reports': {}".format(len(reports)))
#
# for report in reports:
#     print(report.id)
#
#
# print(watchlist.report_ids)

# import requests
#
# cb_api_id = "ZTTLWSBQWY"
# cb_api_key = "NRTJWZ5M895UIQTCDTHDN4TK"
#
# data = {
# "name": "test",
# "notify_on_finish": False,
# "sql": "SELECT name, path, source FROM autoexec;"
# }
#
# print ( data )
#
# headers = {
# 'X-Auth-Token': '{0}/{1}'.format(cb_api_key ,cb_api_id),
# 'Content-Type': 'application/json'
# }
#
# print ( headers )
#
# r = requests.post('https://defense-test03.cbdtest.io/livequery/v1/orgs/252TYM96/runs', json=data, headers=headers)
#
# print ( r.text )
#
# print(r.status_code)
#
# print ( r.json() )

from cbapi.psc.threathunter import CbThreatHunterAPI, Process

cbth = CbThreatHunterAPI(profile="eap01")
proc_search = cbth.select(Process).where('process_name:services.exe').sort_by('childproc_count')

procs = proc_search[0:300]

for proc in procs:
    print(proc.childproc_count)
