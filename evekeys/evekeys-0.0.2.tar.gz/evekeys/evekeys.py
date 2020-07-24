# -*- coding: utf-8 -*-
#!/usr/bin/python

# evekeys for Python 3
# by Chris Lindgren <chris.a.lindgren@gmail.com>
# Distributed under the BSD 3-clause license.
# See LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause for details.

# WHAT IS IT?
# A set of functions that uses scikit-learn to conduct a TF-IDF analysis to isolate keywords 
# from an event-based document. It answers the following questions:

    # 1. What keywords represent a particular period of content?
    # 2. What keywords represent a particular group of content from a particular period?

# It assumes you have:
    # imported your corpus as a pandas DataFrame,
    # included metadata information, such as a list of dates and list of groups to reorganize your corpus, and
    # pre-processed your documents.

# It functions only with Python 3.x and is not backwards-compatible.

# Warning: evekeys performs little to no custom error-handling, so make sure your inputs are formatted properly. If you have questions, please let me know via email.
import pandas as pd
import ast
import re
from tqdm import tqdm_notebook as tqdm
from sklearn.feature_extraction.text import CountVectorizer

def list_contains_string(lst, string):
   for v in lst:
      if string in v:
         return True
   return False

def get_stop_words(stop_file_path):
    """load stop words from file"""
    
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return frozenset(stop_set)

def period_writer(**kwargs):
    p_dict = {}
    for p in range( kwargs['p_range'][0], kwargs['p_range'][1]+1 ):
        period_df_sample = kwargs['corpus'][kwargs['corpus'][kwargs['date_col']].isin(kwargs['date_list'][str(p)])]
        
        p_dict.update({
            str(p): {'period_only': period_df_sample}
        })
        
    return p_dict

def period_group_writer(**kwargs):
    for p in range( kwargs['p_range'][0], kwargs['p_range'][1]+1 ):        
        ps = kwargs['corpus'][str(p)]['period_only']
        
        for g in kwargs['group_lists']:
            group_content = []
            for row in ps.to_dict('records'):
                # CHECK GROUP
                h = row[kwargs['group_col']]
                #check if list is string
                if isinstance(h, str):
                    h = ast.literal_eval(h)
                    if type(h) == list and len(h) > 0:
                        # Go through list of group search factors
                        for ht_check in h:
                            for ht in g[0]:
                                #If match found, append content to list
                                if ht == ht_check:
                                    group_content.append(row)
                #check if list is list
                if isinstance(h, list):
                    if len(h) > 0:
                        # Go through list of group search factors
                        for ht_check in h:
                            for ht in g[0]:
                                #If match found, append content to list
                                if ht == ht_check:
                                    group_content.append(row)

            g_df = pd.DataFrame(group_content)
            group_name = g[1]
            kwargs['corpus'][str(p)].update({
                group_name: { 'corpus': g_df }
            })
    return kwargs['corpus']

def group_only_writer(**kwargs):
    s = kwargs['corpus']
    
    #Create dict for storing grouped content
    group_dict = {}
    for group in kwargs['group_lists']:
        group_dict.update({
            group[1]:[]
        })
    
    # Parse corpus and based on grouping filter, 
    # assign to respective group in group_dict
    for row in tqdm(s.to_dict('records')):
        # Check content for group filter
        h = row[kwargs['group_col']]
        
        # Check if list is string
        if isinstance(h, str):
            h = ast.literal_eval(h)
            if type(h) == list and len(h) > 0:
                # Go through list of group search factors
                for group_check in h:
                    # Parse all group lists
                    for group in kwargs['group_lists']:
                        # Check each filtering item in List
                        for g in group[0]:
                            #If match found, append content to list
                            #with shared group name from tuple
                            if g == group_check:
                                group_dict[group[1]].append(row)
        # Check if list is list
        elif isinstance(h, list):
            if len(h) > 0:
                # Go through list of group search factors
                for group_check in h:
                    # Parse all group lists
                    for group in kwargs['group_lists']:
                        # Check each filtering item in List
                        for g in group[0]:
                            #If match found, append content to list
                            #with shared group name from tuple
                            if g == group_check:
                                group_dict[group[1]].append(row)

        
    # Assign each corpus as dataframes
    final_group_dict = {}
    for group in group_dict:
        g_df = pd.DataFrame(group_dict[group])
        final_group_dict.update({
            group: { 'corpus': g_df }
        })
    
    return final_group_dict

class vectorObj:
    '''an object class that stores each event's/group's documents, count vector, word count vector, and keywords'''
    def __init__(self, docs=None, cv=None, word_count_vector=None, keywords=None,):
        self.docs = docs
        self.cv = cv
        self.word_count_vector = word_count_vector
        self.keywords = keywords

def word_count_vectorizer(**kwargs):
    # If periodicly organized
    if kwargs['org_type'] == 'periodic':
        for p in kwargs['corpus']:
            for group in kwargs['corpus'][p]:
                group_check = list_contains_string(kwargs['group_list'], group)
                if group_check == True:
                    vo = vectorObj()

                    docs = kwargs['corpus'][p][group]['corpus']['tweet'].tolist()
                    vo.docs = docs

                    #create a vocabulary of words, 
                    #ignore words that appear in X% of documents, 
                    #eliminate stop words
                    cv = CountVectorizer(max_df=kwargs['max_df'], stop_words=kwargs['stopwords'])
                    vo.cv = cv

                    word_count_vector = cv.fit_transform(docs)
                    vo.word_count_vector = word_count_vector

                    kwargs['corpus'][p][group].update({ 'object':vo })

    if kwargs['org_type'] == 'groups_only':
        for group in kwargs['corpus']:
                group_check = list_contains_string(kwargs['group_names'], group)
                if group_check == True:
                    vo = vectorObj()

                    docs = kwargs['corpus'][group]['corpus']['tweet'].tolist()
                    vo.docs = docs

                    #create a vocabulary of words
                    cv = CountVectorizer(
                        max_df=kwargs['max_df'], #ignore words that appear in X% of documents
                        stop_words=kwargs['stopwords'] #eliminate stop words
                    )
                    vo.cv = cv

                    word_count_vector = cv.fit_transform(docs)
                    vo.word_count_vector = word_count_vector

                    kwargs['corpus'][group].update({ 'object':vo })

    return kwargs['corpus']
