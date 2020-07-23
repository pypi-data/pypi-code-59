import os
import nltk
import string
import random
import warnings
import wikipedia
import numpy as np
from nltk import word_tokenize
from chatterbot import ChatBot

warnings.filterwarnings("ignore")
from nltk.corpus import stopwords
from nltk.chat.util import Chat, reflections
from validate_email import validate_email
from chatterbot.trainers import ListTrainer
from sklearn.metrics.pairwise import cosine_similarity
from chatterbot.trainers import ChatterBotCorpusTrainer
from sklearn.feature_extraction.text import TfidfVectorizer


#Functions for formal reponses

def greeting(sentence):
        for word in sentence.split():
                if word.lower() in greeting_inputs:
                        return random.choice(greeting_responses)

def thank_u(sentence):
        for word in sentence.split():
                if word.lower() in thank_you:
                        return random.choice(thank_you)

def noo(sentence):
        for word in sentence.split():
                if word.lower() in no:
                        return random.choice(no)
     
def k_s(sentence):
        for word in sentence.split():
                if word.lower() in ok_yes:
                        return random.choice(ok_yes)




def response(user_response):
        robo_response=""
        sent_tokens.append(user_response)
        TfidfVec =TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf=TfidfVec.fit_transform(sent_tokens)
        vals =cosine_similarity(tfidf[-1],tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf=flat[-2]
        if(req_tfidf==0):
                return bot.get_response(user_response) 
        else:
                robo_response = robo_response+sent_tokens[idx]
                return robo_response




# Record Users Data

def get_data ():
        print(botspeech, "Please Fill your details for better Reach  !")                                                #name_of_person is recorded
        name,email,number = True,True,True
        while name:
                print(botspeech, "Name format:  Input Name Middle name Surname")
                name_of_person = input("User:  ")
                if len(name_of_person.split(" ")) >=3:
                        name = False
                    
        while email:
                print(botspeech,"Enter your email address")
                address=input("User:  ")                                                                                                            #email is recorded  
                check=validate_email(address)
                if check==True:
                        email=False
                               
        while number:
                print(botspeech,"Enter your 10- digit Contact Number")
                contact=input("User:  ")                                                                                                            #contact recorded
                if  len(contact)>=10 and len(contact)<=13 and contact.isdigit()==True:
                        number=False
        print(botspeech,"Thank You")
                    


#With this Data we Give data and Take Action according to users preferrence.
        
def give_data():
        thing1= "Donate"
        thing2="Pledge"
        thing3 ="Visit"
        
        print(botspeech, "May I know What you are Looking for ?")
        print("1) "+thing1,"2) " +thing2,"3) "+thing3, sep = '\n')
        option_selected=input("User:  ").lower()
        if   '1' in option_selected.split() or thing1.lower()  in option_selected.split(): print ("Follow this Process to do" +thing1)
        if   '2' in option_selected.split() or thing2.lower()  in option_selected.split(): print ("Follow this Process to"+ thing2)
        if   '3' in option_selected.split() or thing3.lower()  in option_selected.split(): print ("Follow this Process to"+ thing3)

def links():

        print("Just a Remainder, Stay Connected with us and Follow us on:")
        print("Facebook","Instagram","LinkedIn","Youtube",sep = '\n')
