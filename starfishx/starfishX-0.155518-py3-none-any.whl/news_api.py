import os
import pandas as pd
import datetime

from enum import Enum
class NewsTypeMatch(Enum):
 any = "any"
 all = "all"


def news_api(keyword,contentLen=100,contentShort=True,typeMatch=NewsTypeMatch.any):
 '''
 keyword : (list) คำที่ต้องการค้นหาในข่าว
 typeMatch : (str) มีสอง type คือ any คือคำใดคำหนึ่ง และ all คือต้อง match ทั้ง list
 '''   
 #ดึงข้อมูลใน Directory
 arr = os.listdir("news")
 #keyword = symbol

 dateDS = []
 content = []
 for filename in arr:
  file = "news/"+filename
  date = filename.replace("news-","").replace(".txt","")[:-3]
  
  with open(file) as f:
   for line in f:
    matching = [s for s in keyword if s in line]
    
    typeMatch.value
    if(typeMatch.value=="any"):
     if(len(matching)>0):
      dateDS.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
      content.append(line)
    
    if(typeMatch.value=="all"):
     if(len(matching)==len(keyword)):
      dateDS.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
      content.append(line)
 ################    
 if(len(content)==0):
    return 0

 dfNews = pd.DataFrame({"Date":dateDS,"content":content})

 #######################
 #ยุบข่าวให้ไม่ยาวเกินไป
 tmp = dfNews["content"].str.split(" ")
 shortContent = []
 for i in tmp:
  s = ""
  for j in i:
   if(len(s)+len(j)<=contentLen):
     s+=j
     #print(j)
  shortContent.append(s.replace("\n","")) 

 pd.set_option('display.max_colwidth', -1)
 if(contentShort):
     dfNews["contentShort"] = shortContent
     return dfNews[["Date","contentShort"]].sort_values(["Date"],ascending=False)
 else:

     return dfNews.sort_values(["Date"],ascending=False)