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


greeting_inputs =    ("hello","hi","greetings","greeting","sup","Wsup","what's up","hey","heya","hey","hi there","heloo","heelo")
greeting_responses  =   ["Hey","Hello","Hi there","How may I help you ?","Wsup, Hope you are doing well !","What's up","How may I help you ?"] 
wrong_responses =   ["Hmm Hmm, Tell me more!!","OK Can You Specify more ?","I don't Understand", "Tell me more ","OK, I see !!" ]
thank_you  =    [ "thank u", "thank you","thanx","thanks","thank","thnx","tnx" ]
ok_yes    =   [ "ok","k","kk","kkk","ook","okk","yes","sss","s","ss"]
referring  =    [" Is it right ?"," Is this what you want to know !!"," R8t ?","Is this what you are referring  ?"]
no =   ["no","noo","nah","nooo"]
ok_yes_resp=[" How Can I help you ?","Anything I can help you with ?","How can I serve You ?","Need Help in Anything ?"]


class Jigbot():
        def __init__(self, txt_file, name="Jiganesh"):
                self.name = name
                self.botspeech = name + ":  "
                self.txt_file = txt_file


        def get_data(self):
                print(self.botspeech, "Please Fill your details for better Reach  !")
                bname, bemail, bnumber = True, True, True

                while bname:
                        print(self.botspeech, "Name format:  Input Name Middle name Surname")
                        name_of_person = input("User:  ")  # name_recorded
                        if len(name_of_person.split(" ")) >= 3:
                                bname = False

                while bemail:
                        print(self.botspeech, "Enter your email address")
                        address = input("User:  ")  # email is recorded
                        check = validate_email(address)
                        if check == True:
                                bemail = False

                while bnumber:
                        print(self.botspeech, "Enter your 10- digit Contact Number")
                        contact = input("User:  ")  # contact recorded
                        if len(contact) >= 10 and len(contact) <= 13 and contact.isdigit() == True:
                                bnumber = False
                print(self.botspeech, "Thank You")

                return name_of_person, address, contact

