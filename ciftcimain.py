import pyautogui as p
import time
import keyboard
import coz
import sys
sys.setrecursionlimit(2147483646)

kabakkordi = [888, 379]
tamorta = [960, 629]
karpuz_koordinat = [816, 379]
mc_ara_elemani = -1  # Başlangıç değeri sıfır olarak ayarlandı
mc_ara_listesi = []

def onayara():
    try:
        onay_koordinat = p.locateOnScreen("images/onay.png", confidence=0.89)
        if onay_koordinat:
            coz.start()
            time.sleep(0.1)
            p.rightClick()
            p.rightClick()
            return True
    except p.ImageNotFoundException:
        print("Hata: Onay resmi bulunamadı.")
        return False

def yavas_yaz(text, delay=0.7):
    keyboard.write(text, delay=delay)


def mc_ara():
    global mc_ara_elemani
    global mc_ara_listesi
    try:
            mc_ara_elemani += 1
            mc_ara_listesi = list(p.locateAllOnScreen("images/mc.png", confidence=0.9))
            print(len(mc_ara_listesi))
            if mc_ara_listesi:
                if mc_ara_elemani >= len(mc_ara_listesi):
                    mc_ara_elemani = 0
                p.keyDown("t")
                p.keyUp("t")
                p.moveTo(mc_ara_listesi[mc_ara_elemani])
                time.sleep(0.2)
                p.leftClick()
                time.sleep(0.2)
                p.moveTo(tamorta)
                p.leftClick()
                p.keyDown("escape")
                time.sleep(0.2)
                p.keyUp("escape")
                time.sleep(0.2)
                p.rightClick()
                time.sleep(0.2)
                p.rightClick()
                p.rightClick()
                karpuzsat()
                kontrol = onayara()
                if kontrol:
                    p.rightClick()
                    p.rightClick()
                    p.moveTo(tamorta)
                    karpuzsat()
                basla()
    except p.ImageNotFoundException:
            print("Minecraft açık değil")
            mc_ara()
        

def basla():
    global mc_ara_elemani
    global mc_ara_listesi
    while True:
        time.sleep(0.4)
        kabakara = p.locateOnScreen("images/kabak.png", confidence=0.9)
        try:
            if kabakara:
                    time.sleep(0.3)
                    onayara()
                    p.rightClick()
                    p.rightClick()
                    p.moveTo(kabakkordi)
                    time.sleep(0.2)
                    p.keyDown("shift")
                    time.sleep(0.2)
                    p.leftClick()
                    time.sleep(0.2)
                    p.keyUp("shift")
                    time.sleep(0.1)
                    p.keyDown("escape")
                    time.sleep(0.2)
                    p.keyUp("escape")
                    p.keyDown("1")
                    time.sleep(0.2)
                    p.keyUp("1")
                    p.keyDown("t")
                    time.sleep(0.2)
                    p.keyUp("t")
                    keyboard.write("/sat hepsi", delay=0.18)
                    time.sleep(0.1)
                    p.keyDown("enter")
                    p.keyUp("enter")
                    p.rightClick()
        except p.ImageNotFoundException:
                mc_ara()


def karpuzsat():
    p.rightClick()
    p.rightClick()
    p.moveTo(tamorta)
    time.sleep(0.5)
    karpuzara = p.locateOnScreen("images/karpuz.png",confidence=0.9)
    if karpuzara:
            p.moveTo(karpuz_koordinat)
            p.keyDown("shift")
            time.sleep(0.2)
            p.rightClick()
            p.keyUp("shift")
            onayaramak = onayara()
            if onayaramak:
                p.rightClick()
                p.rightClick()
                time.sleep(0.2)
                time.sleep(0.2)
                p.moveTo(karpuz_koordinat)
                p.keyDown("shift")
                time.sleep(0.2)
                p.rightClick()
                p.keyUp("shift")    
                p.moveTo(tamorta)            
                basla()
            else:
                p.rightClick()
                p.moveTo(tamorta)
                basla()
                
def main():
        keyboard.wait("f8")
        mc_ara()

