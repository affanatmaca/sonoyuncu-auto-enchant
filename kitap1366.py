import pyautogui as p
import keyboard
import time

import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import json
import requests
koruma_durum = False

yumruk_durum = False
keskinlik_durum = False
kirilmazlik_durum = False
derin_kosucu_durum = False
sonsuzluk_durum = False
verimlilik_durum = False
servet_durum = False
ganimet_durum = False
savurma_durum = False
ipeksi_durum = False

lapisvarmi = None
kitapvarmi = None

lvlotuzsagalt = [836 , 338]
lvlbesagalt = [836, 260]
basilacakitem = [555 , 314]
lapiskordi = [590 , 314]
ekransolalt = [91 ,657]

kitapxy1 = [531, 293]
kitapxy2 = [571, 333]
lapisxy1 = [571, 293]
lapisxy2 = [613, 334]

def aramayap():
    Durum = None
    if yumruk_durum:
        if Durum == None or Durum == False:
            Durum = yumrukbas()
    if keskinlik_durum:
        if Durum == None or Durum == False:
            Durum = keskinlikbas()
    if kirilmazlik_durum:
        if Durum == None or Durum == False:
            Durum = kirbas()
    if derin_kosucu_durum:
        if Durum == None or Durum == False:
            Durum = derkinkosucubas()
    if sonsuzluk_durum:
        if Durum == None or Durum == False:
            Durum = sonsuzlukbas()
    if verimlilik_durum:
        if Durum == None or Durum == False:
            Durum = verimlilikbas()
    if servet_durum:
        if Durum == None or Durum == False:
            Durum = serverbas()
    if ganimet_durum:
        if Durum == None or Durum == False:
            Durum = ganimetbas()
    if savurma_durum:
        if Durum == None or Durum == False:
            Durum = savurmabas()
    if koruma_durum:
        if Durum == None or Durum == False:
            Durum = koruma4check()
     
    return Durum

def koruma4check():
    try:
        kirkontrol = pyautogui.locateOnScreen("images/koruma4.jpg",confidence=0.9)
        return kirkontrol
    except p.ImageNotFoundException:
        return False

def resimkontrol(resimyol):
    x1 = 907
    y1 = 428
    x2 = 1120
    y2 = 503
    region = (907, 428, 1120, 503)
    location = pyautogui.locateOnScreen(resimyol,confidence=0.9, region=region) 
    if location:
        return True
    else:
        return False

def webhook_mesaj_gonder(item_ismi, resim_url, aciklama):
    item_ismi = item_ismi
    resim_url = resim_url
    aciklama = aciklama
    try:
        with open("webhook_settings.json", "r") as json_file:
            data = json.load(json_file)
            webhook_value = data.get("webhook", "")
            if webhook_value:
                embed = {
                "title": item_ismi,
                "description": aciklama,
                "thumbnail": {"url": resim_url},
                "color": 0x00FF00  # Açık yeşil renk                   
                }


                payload = {
                    "content": "",
                    "embeds": [embed]
                }

                headers = {"Content-Type": "application/json"}

                response = requests.post(webhook_value, data=json.dumps(payload), headers=headers)

                if response.status_code == 204:
                    print("Webhook'a embedli mesaj başarıyla gönderildi.")
                else:
                    print(f"Webhook'a mesaj gönderme başarısız. HTTP status code: {response.status_code}")
    except FileNotFoundError:
        print("webhook_settings.json dosyası bulunamadı.")
    except json.JSONDecodeError:
        print("webhook_settings.json dosyası okunurken hata oluştu.")

def kirbas():
    try:
        kirkontrol = resimkontrol("images/kirilmazlik.png")
        return kirkontrol
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def keskinlikbas():
    try:
        kirkontrol = resimkontrol("images/keskinlik4.png")
        return kirkontrol
    except Exception as e:
        return False

def yumrukbas():
    try:
        kirkontrol =  resimkontrol("images/yumruk2.png")
        return kirkontrol
    except:
        return False

def derkinkosucubas():
    try:
        kirkontrol =  resimkontrol("images/derkinkosucu.png")
        return kirkontrol
    except:
        return False

def sonsuzlukbas():
    try:
        kirkontrol = resimkontrol("images/sonsuzluk.png")
        return kirkontrol
    except Exception as e:
        return False

def verimlilikbas():
    try:
        kirkontrol = resimkontrol("images/verimlilik.png")
        return kirkontrol
    except Exception as e:
        return False

def serverbas():
    try:
        kirkontrol = resimkontrol("images/servet3.png")
        return kirkontrol
    except Exception as e:
        return False

def ganimetbas():
    try:
        kirkontrol = resimkontrol("images/ganimet.png" )
        return kirkontrol
    except Exception as e:
        return False

def savurmabas():
    try:
        kirkontrol = resimkontrol("images/savurma.png")
        return kirkontrol
    except Exception as e:
        return False

def ipeksibas():
    try:
        kirkontrol = resimkontrol("images/savurma.png")
        return kirkontrol
    except Exception as e:
        return False


def eger_lapis_range_in_icindeyse_es_gec(location, koordinat1, koordinat2):
    x_within_range = koordinat1[0] <= location[0] <= koordinat2[0] or koordinat2[0] <= location[0] <= koordinat1[0]
    y_within_range = koordinat1[1] <= location[1] <= koordinat2[1] or koordinat2[1] <= location[1] <= koordinat1[1]
    return x_within_range and y_within_range

def lapisyenile():
    p.moveTo(lapiskordi)
    p.doubleClick()
    p.leftClick()
    
def kitapkoy():
    global kitapvarmi
    try:
        image_path = "images/kitap.png"
        location = pyautogui.locateOnScreen(image_path, confidence=0.99)

        if location is not None:
            print(f"Kitap ekranda bulundu!")

            p.moveTo(location)
            time.sleep(0.25)
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
        else:
            print("Kitap bulunamadı.")
            kitapvarmi = True
    except pyautogui.ImageNotFoundException:
        print(f"Kitap ekranda bulunamadı")
        kitapvarmi = True


def lapiskoy():
    global lapisvarmi
    try:
        image_path = "images/lapis.png"
        location = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if location is not None:
                print(f"Lapis ekranda bulundu!")
                p.moveTo(location)
                time.sleep(0.25)
                p.keyDown("shift")
                p.leftClick()
                p.keyUp("shift")
        else:
                print("Lapis bulunamadı.")
                lapisvarmi = True
    except pyautogui.ImageNotFoundException:
        print(f"Lapis ekranda bulunamadı")
        lapisvarmi = True

def main():
    global lapisvarmi
    global kitapvarmi
    sayi = 0
    keyboard.wait("enter")
    kitapvarmi = False
    while True:
        kitapkoy()
        p.moveTo(lvlotuzsagalt)
        time.sleep(0.25)
        test = aramayap()
        if test:
            p.moveTo(ekransolalt)

            try:
                solaltparlak = p.locateOnScreen("images/level30renkli.png",confidence=0.9)
                if solaltparlak:
                    solaltparlakmi = True
            except p.ImageNotFoundException:
                solaltparlak = None

            while solaltparlak is None:
                try:
                    solaltparlak = p.locateOnScreen("images/level30renkli.png",confidence=0.9)
                    if solaltparlak:
                        solaltparlakmi = True
                        break
                except p.ImageNotFoundException:
                    pass

            p.moveTo(lvlotuzsagalt)
            p.leftClick()
            sayi += 1
            kitap_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183073187341271130/maxresdefault.png?ex=658701c4&is=65748cc4&hm=c99826fde3ca0f8b0596fce1b3860a2a6a0509730f42de9d820376c3dcc36547&"
            webhook_mesaj_gonder(item_ismi="Büyülü kitap",resim_url=kitap_url,aciklama=f"Seçtiğiniz büyülü kitaplardan biri basıldı. \n Başarı ile basılmış item sayısı : {sayi}")
            try:
                p.moveTo(basilacakitem)
                time.sleep(0.25)
                p.keyDown('shift')
                p.leftClick()
                p.keyUp('shift')
            except p.ImageNotFoundException:
                print("basilmis kitap bulunamadi")
        else:
            try:
                sagust = p.locateOnScreen("images/level5renkli.png",confidence=0.9)
            except p.ImageNotFoundException:
                sagust = None
            if sagust is None:
                while sagust is None:
                    try:
                        sagust = p.locateOnScreen("images/level5renkli.png",confidence=0.9)
                        if sagust:
                            break
                    except p.ImageNotFoundException:
                        pass

            p.moveTo(sagust[0] - 9, sagust[1] + 15)
            p.leftClick()
            p.moveTo(basilacakitem)
            time.sleep(0.3)
            p.keyDown('q')
            p.keyUp('q')

            if lapisvarmi or kitapvarmi:
                p.keyDown('escape')
                p.keyUp('escape')
                print("dongu basari ile kirildi")
                break
