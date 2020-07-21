import cv2
import numpy as np

def copyimage(img):
    imgResult = img.copy()
    return imgResult

def obtaincolor(img, myColors, myCrgb,imgResult):
    Inc = 0
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newCoordinates = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHsv, lower, upper)
        x, y = getcontours(mask)
        cv2.circle(imgResult, (x,y),10,myCrgb[Inc],cv2.FILLED)
        if x != 0 and y != 0:
            newCoordinates.append([x, y, Inc])
        Inc+=1
       
    return newCoordinates
def getcontours(img):

    _,contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>450:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def draw(myCoordinates, myColorValues,imgResult):
    for point in myCoordinates:
        cv2.circle(imgResult, (point[0], point[1]), 40, myColorValues[point[2]], cv2.FILLED)
