#!/usr/bin/env python
# coding: utf-8

# In[103]:
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
class quora_qa:
    def quora_scrap(self,keyword,PATH): 
        links = []
        final_answers = []
        questions = []
        final_question_answer_pairs_quora_dict = {}
        driver = webdriver.Chrome(executable_path =r'{}chromedriver.exe'.format(PATH))
        #load website to scrape
        driver.get('https://www.quora.com/q/{}/questions'.format(keyword))
        html1=driver.page_source
        #Scroll the webpage
        ScrollNumber=600
        #max scrolls-> it's value depends on count of questions-answers rendering through particular profile page. 
        #Scrapping questions on Coronavirus
        for i in range(1, ScrollNumber):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html=driver.page_source
        html=html.encode()
        soup = BeautifulSoup(html)

        elem = driver.find_elements_by_partial_link_text('Answer')
        for link in elem:
            links.append(link.get_attribute('href'))

        ScrollNumber = 5
        for qa_link in links:
            answers = []
            driver.get(qa_link)

            for i in range(1, ScrollNumber):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html2 = driver.page_source
            html2 = html2.encode()
            soup2 = BeautifulSoup(html2)
            for hit in soup2.findAll(attrs={'class':'q-text puppeteer_test_question_title','style':'box-sizing: border-box; direction: ltr;'}):
                span = hit.contents[0]
                questions.append(span.text)

            for hit in soup2.findAll(attrs={'class':'q-relative spacing_log_answer_content','style':'box-sizing: border-box; direction: ltr; position: relative;'}):
                span = hit.contents[0]
                answer = span.text
                answers.append(answer)
            final_answers.append(answers)

        for keys in questions:
            for values in final_answers:
                final_question_answer_pairs_quora_dict[keys] = values
                final_answers.remove(values)
                break
        print("Extraction Complete")
        return questions,final_answers,final_question_answer_pairs_quora_dict

# Now save questions answers in a csv file
    def save_to_csv(self,filename,questions,final_question_answer_pairs_quora_dict):
        qa_csv = pd.DataFrame({'questions':pd.Series(questions),'answers':pd.Series(list(final_question_answer_pairs_quora_dict.values()))})
        qa_csv.to_csv(filename)
        return "Saved Successfully!"       

