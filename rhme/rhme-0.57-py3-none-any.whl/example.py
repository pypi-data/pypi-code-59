from rhme.api import *
from rhme.config import Configuration
from rhme.helpers.exceptions import *
import base64
import numpy as np
import cv2
import sys

configs = Configuration()

class Example:

    def __init__(self):

        expression = ""
        hme_recognizer = HME_Recognizer()
        if sys.argv[1]:
            images = [configs.package_path + '/images/' + sys.argv[1]]
        else:
            images = [configs.package_path + '/images/validacao/21.png']

        for image in images:

            try:
                hme_recognizer.load_image(image, data_type='path')
                expression, img = hme_recognizer.recognize()

                lex_errors = hme_recognizer.get_lex_errors()
                yacc_errors = hme_recognizer.get_yacc_errors()
                pure_lex_errors = hme_recognizer.get_lex_pure_errors()
                pure_yacc_errors = hme_recognizer.get_yacc_pure_errors()

                print('\n\nLex errors: ', lex_errors)
                print('\n\nYacc errors: ', yacc_errors)
                print('\n\nPure Lex Errors:', pure_lex_errors)
                print('\n\nPure Yacc Errors: ', pure_yacc_errors)

            except (GrammarError, SintaticError, LexicalError) as e:

                print('[example.py] Exception: ', e.data)
                print('[example.py] Exception: ', e.valor)

                if 'latex_string_original' in e.data:
                    print('hmmmm')
                    expression = e.data['latex_string_original']

            print("\nExpressão: ", expression)
Example()
