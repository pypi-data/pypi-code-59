#!/usr/bin/env python3

"""
A workspace switcher for Sway and i3.
See https://www.mankier.com/1/swaymsg#get_workspaces and https://www.mankier.com/5/sway#workspace
"""

import subprocess
import json

get_workspaces_result = subprocess.run(['swaymsg', '--raw', '-t', 'get_workspaces'],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

if get_workspaces_result.stderr:
    raise IOError(get_workspaces_result.stderr.decode('utf-8'))

get_workspaces_json = json.loads(get_workspaces_result.stdout.decode('utf-8'))

workspaces = {wp['num']: wp['name'] for wp in get_workspaces_json}

sway_result = subprocess.run(['sway', 'workspace', workspaces[2]],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

if sway_result.stderr:
    raise IOError(sway_result.stderr.decode('utf-8'))

sway_result_json = json.loads(sway_result.stdout.decode('utf-8'))

if not sway_result_json[0]['success']:
    raise IOError('The command did not return success True.' + sway_result.stderr.decode())
