import logging

import requests
import pandas as pd


def get_json(url, headers={}):
    response = requests.get(url, headers=headers)
    logging.info(f'{response.url}.. {response.status_code}')
    
    jo = {}
    if response.status_code==200:
        jo = response.json()
        
    return jo


def metadata(symbol):
    url = f'https://api.nasdaq.com/api/company/{symbol}/company-profile'
    jo = get_json(url)

    metadata = pd.Series([], name=symbol)
    if ('data' in jo) and (jo['data'] is not None):
        metadata = pd.DataFrame(jo['data']).loc['value'].rename(symbol)
    
    return metadata


if False:
    pd.concat([metadata(s) for s in ['AMZN', 'GOOGL', 'AAAU']], axis=1).T