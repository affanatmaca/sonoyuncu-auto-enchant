import cv2
import keyboard
import time
import numpy as np
import pyautogui as p
import sys
sys.setrecursionlimit(2147483646)

kod1x = [974,406]
kod1y = [986,422]

kod2x = [985,408]
kod2y = [997,424]

kod3x = [991,408]
kod3y = [1004,424]

kod4x = [1001,407]
kod4y = [1014,423]

yerler = [
    [915,504],#1
    [958,505],#2
    [1002,504],#3
    [913,550],#4
    [956,549],#5
    [1002,550],#6
    [914,592],#7
    [957,593],#8
    [1002,593],#9
    [954,629],#10
]
onay = [1001,637]


kabakx = [591, 202]
kabaky = [628, 240]

def ekrandaara(resim_yol, x1, y1, confidence):
    try:
        left, top, width, height = x1[0], x1[1], y1[0] - x1[0], y1[1] - x1[1]
        koordinatlar = p.locateOnScreen(resim_yol, region=(left, top, width, height), confidence=confidence)
        return koordinatlar is not None
    except Exception as e:
        return False

def kodara(kodx, kody, yol):
    try:
        for i in range(10):
            resim_yolu = f"images/{i}.png"
            varmi = ekrandaara(resim_yolu, kodx, kody, get_confidence(yol))
            if varmi:
                return i
    except p.ImageNotFoundException:
        print("kod ekranda bulunamadi")

def get_confidence(yol):
    if yol == 1:
        return 0.95
    elif yol == 2:
        return 0.95
    elif yol == 3:
        return 0.95
    elif yol == 4:
        return 0.95
    else:
        return 0.95

def gitvetıkla(kordi):
    p.rightClick()
    p.moveTo(kordi)
    time.sleep(0.1)
    p.leftClick()
    time.sleep(0.1)

def start():
    yer1_numara = kodara(kod1x, kod1y, 1)
    if yer1_numara is not None:
        yer1 = yerler[yer1_numara - 1]
        gitvetıkla(yer1)
    
    yer2_numara = kodara(kod2x, kod2y, 2)
    if yer2_numara is not None:
        yer2 = yerler[yer2_numara - 1]
        gitvetıkla(yer2)
    
    yer3_numara = kodara(kod3x, kod3y, 3)
    if yer3_numara is not None:
        yer3 = yerler[yer3_numara - 1]
        gitvetıkla(yer3)
    
    yer4_numara = kodara(kod4x, kod4y, 4 )
    if yer4_numara is not None:
        yer4 = yerler[yer4_numara - 1]
        gitvetıkla(yer4)

    print(yer1_numara, yer2_numara, yer3_numara, yer4_numara)
    gitvetıkla(onay)
    time.sleep(0.5)



