# -*- coding: utf-8 -*-
import cv2
import glob


class RemoveBlurImages:
    
    def __init__(self, pathOrigin = '', threshold = 100):
        self.threshold = threshold
        if pathOrigin != '':
            self.listRemaining, self.listOfBlurring = self.filterPathOfImages(pathOrigin)
            
    def setThreshold(self, threshold):
        self.threshold = threshold
    
    def checkBlurring(self, imageToAnalise):
        image = cv2.imread(imageToAnalise)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        if fm < self.threshold:
            blurr = True
        else:
            blurr = False
        
        return blurr
        
    
    def filterPathOfImages(self, pathOrigin):
        listOfImages = glob.glob(pathOrigin + '/*.jpg') + glob.glob(pathOrigin + '/*.png')
        listOfImages.sort()
        
        listOfBlurring = []
        for image in listOfImages:
            blurr = self.checkBlurring(image)
            if blurr:
                listOfBlurring.append(image)
        
        listRemaining = listOfImages[:]
        for elementToRemove in listOfBlurring:
            try:
                listRemaining.remove(elementToRemove)
            except:
                print(f'O elemento {elementToRemove} parece que já foi removido.')
                
        return listRemaining, listOfBlurring
    

if __name__ == '__main__':
    
    removeBlur = RemoveBlurImages('/media/alancaio/Elements/DataBase/PythonProjectMachineLearning/Filtragem/Blurring', 100)
    print(f' Imagens restantes: {len(removeBlur.listRemaining)} Imagem embaçadas: {len(removeBlur.listOfBlurring)}')