# -*- coding: utf-8 -*-
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim

import glob, os
import pandas

import time

class Similarity:
    
    def __init__(self):
        pass
    
    def compareImageWithMSE(self, imageA, imageB):
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        
        return err
    
    def compareImageWithSSIM(self, imageA, imageB):
        v_ssim = ssim(imageA, imageB)
        return v_ssim


class AvaluateListOfImages:
    
    def __init__(self):
        pass
    
    def loadImageList(self, pathOrigin):
        listOfImages = glob.glob(pathOrigin + '/*.jpg') + glob.glob(pathOrigin + '/*.png')
        return listOfImages
    
    def constructComparation(self, pathOrigin, fileDestiny, resize = False, scale_percent = 100):
        listOfImages = self.loadImageList(pathOrigin)
        listOfImages.sort()
        
        similarity = Similarity()
        
        listTotal = []
        listForImage = []
        listNameImages = []
        
        for i, image in enumerate(listOfImages):
            listNameImages.append(image.split('/')[-1])
            for j, image2 in enumerate(listOfImages):
                imageA = cv2.imread(image)
                imageB = cv2.imread(image2)
                imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                
                if resize:
                    width = int(imageA.shape[1] * scale_percent / 100)
                    height = int(imageA.shape[0] * scale_percent / 100)
                    
                    # dsize
                    dsize = (width, height)
                    imageA = cv2.resize(imageA, dsize)
                    imageB = cv2.resize(imageB, dsize)
                
                mse = int(similarity.compareImageWithMSE(imageA, imageB))
                ssim = np.around(similarity.compareImageWithSSIM(imageA, imageB), 2)
                #print(f'Imagem: {i} x Imagem: {j} : ({mse},{ssim})')
                listForImage.append((mse, ssim))
            listTotal.append(listForImage)
            listForImage = []
            
        listTotal.insert(0, listNameImages)
        
        df = pandas.DataFrame(listTotal)
        
        listNameImages.insert(0, 'nameFile')
        
        dfFinal = pandas.concat([pandas.DataFrame(listNameImages), df], axis=1)
        dfFinal.to_csv(fileDestiny)
        
        return(dfFinal)
        
    def compareImages(self, imageA, imageB, onlyEqual = True, resize = False, scale_percent = 100):
        similarity = Similarity()
        
        imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                
        if resize:
            width = int(imageA.shape[1] * scale_percent / 100)
            height = int(imageA.shape[0] * scale_percent / 100)
                    
            # dsize
            dsize = (width, height)
            imageA = cv2.resize(imageA, dsize)
            imageB = cv2.resize(imageB, dsize)
            
        mse = int(similarity.compareImageWithMSE(imageA, imageB))
        
        if mse < 100:
            if onlyEqual:
                if mse == 0:
                    similar = True
            else:
                similar = True
        else:
            similar = False
            
        return similar
        
    def listRepetidos(self, pathOrigin, removeSimilar = True, resize = False, scale_percent = 100):
        listOfImages = self.loadImageList(pathOrigin)
        listOfImages.sort()
        
        similarity = Similarity()
        
        listaRestante = listOfImages[:]
        listToRemove = []
        for i, image in enumerate(listOfImages):
            imageA = cv2.imread(image)
            
            imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

            if resize:
                        width = int(imageA.shape[1] * scale_percent / 100)
                        height = int(imageA.shape[0] * scale_percent / 100)
                        
                        # dsize
                        dsize = (width, height)
                        imageA = cv2.resize(imageA, dsize)
            
            for image2 in listOfImages[i:]:
                nameImage = image.split('/')[-1]
                nameImage2 = image2.split('/')[-1]
                if image != image2:
                    imageB = cv2.imread(image2)
                    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                    
                    if resize:
                        dsize = (width, height)
                        imageB = cv2.resize(imageB, dsize)
                    
                    mse = int(similarity.compareImageWithMSE(imageA, imageB))
                        
                    if mse < 70:
                        if mse == 0:
                            #print(f'Imagem: {nameImage2} igual a {nameImage} com mse = {mse}')
                            listToRemove.append(image2)
                        else:
                            if removeSimilar:
                                #print(f'Imagem: {nameImage2} semelhante a {nameImage}')
                                listToRemove.append(image2)
                                
        for elementToRemove in listToRemove:
            try:
                listaRestante.remove(elementToRemove)
            except:
                print(f'O elemento {elementToRemove} parece que já foi removido.')
                
                
        return listaRestante, listToRemove
        

    def removerRepetidos(self, listToRemove):
        for imageToRemove in listToRemove:
            try:
                os.remove(imageToRemove)
            except:
                print(f'O elemento {imageToRemove} parece que já foi removido.')
    
    def checkBlacklImage(self, image):
        similarity = Similarity()
        
        imageA = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imageB = np.zeros([int(imageA.shape[1]), int(imageA.shape[0]), 1])

        width = int(imageA.shape[1] * 50 / 100)
        height = int(imageA.shape[0] * 50 / 100)
        
        dsize = (width, height)
        imageA = cv2.resize(imageA, dsize)
        imageB = cv2.resize(imageB, dsize)
 
        mse = int(similarity.compareImageWithMSE(imageA, imageB))
        
        remove = False
        
        if mse < 500:
            remove = True
        
        return remove, mse
        
            
    def removeBlack(self, imageA):
        pass
        
    def listBlackImages(self, pathOrigin, resize = False, scale_percent = 100):
        listOfImages = self.loadImageList(pathOrigin)
        listOfImages.sort()
        
        listaRestante = listOfImages[:]
        listOfBlacks = []
        for i, image in enumerate(listOfImages):
            imageA = cv2.imread(image)
            
            remove, mse = self.checkBlacklImage(imageA)
            
            print(f'A imagem {image} tem mse de {mse} para imagem preta')
            
            if remove:
                listOfBlacks.append(image)
                           
        for elementToRemove in listOfBlacks:
            try:
                listaRestante.remove(elementToRemove)
            except:
                print(f'O elemento {elementToRemove} parece que já foi removido.')
                
                
        return listaRestante, listOfBlacks
                
