# -*- coding: utf-8 -*-
#
# Source: https://github.com/infra-helpers/induction-monitoring/blob/master/python/datamonitor/datamonitor/DataMonitor.py
#
# Authors: Denis Arnaud, Michal Mendrygal
#

import elasticsearch, bz2
from itertools import (takewhile, repeat)

class DataMonitor():
    """
    Helper class with a few utility methods supporting collecting KPIs
    (Key Performance Indicators) from data files and monitoring those KPI
    on tools like Elasticsearch (ES) service.
    Technically, the KPIs collected from data are meta-data.
    """
    
    def __init__(self):
        self.es_host = 'localhost'
        self.es_port = 9200
        self.es_scheme = 'http'
        self.es_user = None
        self.es_pass = None
        self.es_auth = None
        self.es_url = None
        self.es_conn = None

    def __str__(self):
        """
        Description of the DataMonitor instance
        """
        desc = f"DataMonitor - ES URL: {self.es_url}"
        return desc

    
    def es_connect(self, conn=dict()):
        """
        Create and store a connection to an Elasticsearch (ES) service
        """
        if 'host' in conn:
            self.es_host = conn['host']

        if 'port' in conn:
            self.es_port = conn['port']

        if 'scheme' in conn:
            self.es_scheme = conn['scheme']

        if 'user' in conn:
            self.es_user = conn['user']

        if 'passwd' in conn:
            self.es_pass = conn['passwd']

        self.es_auth = f"{self.es_user}@" if self.es_user else ""

        self.es_url = f"{self.es_scheme}://{self.es_auth}{self.es_host}:{self.es_port}"

        if self.es_user:
            self.es_conn = elasticsearch.Elasticsearch(hosts=[self.es_host],
                                                       scheme=self.es_scheme,
                                                       port=self.es_port,
                                                       http_auth=(self.es_user,
                                                                  self.es_pass))
        else:
            self.es_conn = elasticsearch.Elasticsearch(hosts=[self.es_host],
                                                       scheme=self.es_scheme,
                                                       port=self.es_port)

        return self.es_conn
    
    def es_info(self):
        """
        Get the ES cluster information
        """
        es_info = self.es_conn.info()

        # Debug
        print(f"Details for the ES cluster ({self.es_url}): {es_info}")

        #
        return es_info

    def es_send(self, index=None, payload=dict()):
        """
        Send a JSON payload to an Elasticsearch (ES) service
        """
        doc_id = None
        
        if not index:
            raise Exception("An Elasticsearch (ES) index should be specified")

        doc_creation_details = self.es_conn.index(index=index, doc_type='_doc',
                                                  body=payload)
        if '_id' in doc_creation_details:
            doc_id = doc_creation_details['_id']
        
        # Debug
        print(f"Sent to ES ({self.es_url}/{index}; assigned doc ID: {doc_id}; doc creation structure: {doc_creation_details}): {payload}")

        #
        return doc_id

    def es_get(self, index=None, docid=None):
        """
        Get a JSON payload from an Elasticsearch (ES) service
        """
        if not index:
            raise Exception("An Elasticsearch (ES) index should be specified")

        if not docid:
            raise Exception("An Elasticsearch (ES) document ID should be specified")

        doc_str = self.es_conn.get(index=index, id=docid)

        # Debug
        print(f"Got from ES ({self.es_url}/{index} for ID={docid}): {doc_str}")

        #
        return doc_str
  
    def calculate_nb_of_rows_in_file(filepath):
        """
        Count the number of lines in a text file.
        Inspired from https://stackoverflow.com/a/27518377/798053
        """
        
        bufgen = None
        with bz2.open (filepath, 'rb') as f:
            bufgen = takewhile(lambda x: x,
                               (f.read(1024*1024) for _ in repeat(None)))
            return sum (buf.count(b'\n') for buf in bufgen)
