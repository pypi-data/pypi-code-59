# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:21:04 2020

@author: Hadrien
"""
from os.path import join,dirname
base_dir=dirname(__file__)

import sqlite3
# sqliteConnection = sqlite3.connect('nameGenderUSSSA.db')
# cursor = sqliteConnection.cursor()

def predict_gender(name,start_year=1880,end_year=2018):
    sqliteConnection = sqlite3.connect(join(base_dir,'nameGenderUSSSA.db'))
    cursor = sqliteConnection.cursor()
    nyears=end_year-start_year+1
    years_male_str=','.join(['male_%i'%y for y in range(start_year,end_year+1)])
    years_all_str=','.join(['all_%i'%y for y in range(start_year,end_year+1)])
    sql_select_query="SELECT %s,%s from nameGenderUSSSA WHERE name='%s';"%(years_male_str,years_all_str,name.lower())
    cursor.execute(sql_select_query)
    rows = cursor.fetchall()
    if len(rows)>0:
        nmale=sum(rows[0][:nyears])
        ntot=sum(rows[0][nyears:])
        return nmale/ntot
        #print("Male probability for name %s: %f"%(name,nmale/ntot))
    else:
        return None