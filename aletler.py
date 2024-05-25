import pyautogui
import cv2
import keyboard
import time
import numpy as np
import pygetwindow as gw
import json
import requests

dia_kazma_durum = False
dia_kurek_durum = False
dia_balta_durum = False
savas_baltasi_durum = False
titanyum_balta_durum = False
titanyum_kurek_durum = False
titanyum_kazma_durum = False

elmaskazmavarmi = None
kazmavarmi = None

lvlotuzsagalt = [1112 , 494]
lvlbesagalt = [1114, 416]
basilacakitem = [830 , 466]
lapiskordi = [871 , 465]
ekransolalt = [156 ,935]

kitapxy1 = [810, 448]
kitapxy2 = [848, 489]
lapisxy1 = [850, 449]
lapisxy2 = [890, 488]



def resimkontrol(resimyol):
    active_window = gw.getWindowsWithTitle(gw.getActiveWindowTitle())[0]
    x, y, width, height = active_window.left, active_window.top, active_window.width, active_window.height
    screenshot = np.array(pyautogui.screenshot(region=(x, y, width, height)))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    template = cv2.imread(resimyol)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)

    if loc[0].size > 0:
        return True
    else:
        return False

def elmaskazmakoy():
        template = cv2.imread("images/elmaskazma.png")
        h, w, _ = template.shape
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        threshold = 0.999
        lokasyon = np.where(result >= threshold)

        if len(lokasyon[0]) > 0:
            print("Elmas kazma bulundu!")
            top_left = (lokasyon[1][0], lokasyon[0][0])
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            
            pyautogui.keyDown("shift")
            
            pyautogui.leftClick()
            pyautogui.keyUp("shift")

def basilmiselmaskazmaal():
        try:
                pyautogui.moveTo(basilacakitem)
                pyautogui.keyDown("shift")
                pyautogui.leftClick()
                pyautogui.keyUp("shift")
        except pyautogui.ImageNotFoundException:
              print("basilmis elmas kazma bulunamadı")

def elmasKurekKoy():
        template = cv2.imread("images/elmaskurek.png")
        h, w, _ = template.shape
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        threshold = 0.999
        lokasyon = np.where(result >= threshold)

        if len(lokasyon[0]) > 0:
            print("Elmas kurek bulundu!")
            top_left = (lokasyon[1][0], lokasyon[0][0])
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            
            pyautogui.keyDown("shift")
            
            pyautogui.leftClick()
            pyautogui.keyUp("shift")  

def otuzlevelgit():
    global lvlkontrol
    try:
        lvlkontrol = pyautogui.locateOnScreen("images/level30renkli.png")
    except pyautogui.ImageNotFoundException:
        lvlkontrol = False
        pass

    if lvlkontrol:
        pyautogui.moveTo(lvlotuzsagalt)
    else:
        try:
            lvlkontrol2 = pyautogui.locateOnScreen("images/level30renksiz.png")
            if lvlkontrol2:
                pyautogui.moveTo(lvlotuzsagalt)
        except pyautogui.ImageNotFoundException:
            return print("bug oluştu!")

def beslevelkitapbas():
    global levelbesvarmi
    try:
        sagust = pyautogui.locateOnScreen("images/level5renkli.png")
        levelbesvarmi = True
    except pyautogui.ImageNotFoundException:
        sagust = None

    if sagust is None:
        while sagust is None:
            try:
                sagust = pyautogui.locateOnScreen("images/level5renkli.png")
                if sagust:
                    break
            except pyautogui.ImageNotFoundException:
                pass
    if levelbesvarmi == True:
        pyautogui.moveTo(lvlbesagalt)
        pyautogui.leftClick()

            
    pyautogui.moveTo(basilacakitem)
    
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    

def otuzlvlbekle():
    pyautogui.moveTo(ekransolalt)

    try:
        solaltparlak = pyautogui.locateOnScreen("images/level30renkli.png")
    except pyautogui.ImageNotFoundException:
        solaltparlak = None

    while solaltparlak is None:
        try:
            solaltparlak = pyautogui.locateOnScreen("images/level30renkli.png")
            if solaltparlak:
                break
        except pyautogui.ImageNotFoundException:
            pass

    if solaltparlak:
        pyautogui.moveTo(lvlotuzsagalt)

def kitapkoy():
    try:
        book = pyautogui.locateOnScreen("images/kitap.png",confidence=0.999)
        if book is not None:
            pyautogui.moveTo(book)
            
            shiftsolclick()
    except pyautogui.ImageNotFoundException:
        print("kitap bulunamadı")

def lapiskoy():
    try:
        image_path = "images/lapis.png"
        location = pyautogui.locateOnScreen(image_path, confidence=0.99)

        if eger_lapis_range_in_icindeyse_es_gec(location, (lapisxy1), (lapisxy2)):
            print("lapis belirlenen koordinatlar içersinde bulundu es geçiliyor...")
        else:
            if location is not None:
                print(f"Lapis ekranda bulundu!")
                pyautogui.moveTo(location)
                
                pyautogui.keyDown("shift")
                pyautogui.leftClick()
                pyautogui.keyUp("shift")
            else:
                print("Lapis bulunamadı.")
    except pyautogui.ImageNotFoundException:
        print(f"Lapis ekranda bulunamadı")


def servetbas():
    try:
        kirkontrol = resimkontrol("images/servet3.png")
        return kirkontrol
    except Exception as e:
        return False
def webhook_mesaj_gonder(item_ismi, resim_url, aciklama):
    # Kullanım örneği:
    item_ismi = item_ismi
    resim_url = resim_url
    aciklama = aciklama
    try:
        with open("webhook_settings.json", "r") as json_file:
            data = json.load(json_file)
            webhook_value = data.get("webhook", "")

            # Webhook'a embedli mesaj gönder
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


def shiftsolclick():
    pyautogui.keyDown("shift")
    pyautogui.leftClick()
    pyautogui.keyUp("shift")

def lapisyenile():
    pyautogui.moveTo(lapiskordi)
    
    pyautogui.doubleClick()
    
    pyautogui.leftClick()
    


def eger_lapis_range_in_icindeyse_es_gec(location, koordinat1, koordinat2):
    x_within_range = koordinat1[0] <= location[0] <= koordinat2[0] or koordinat2[0] <= location[0] <= koordinat1[0]
    y_within_range = koordinat1[1] <= location[1] <= koordinat2[1] or koordinat2[1] <= location[1] <= koordinat1[1]
    return x_within_range and y_within_range

def main():
    global dia_kazma_durum
    global dia_kurek_durum
    global dia_balta_durum
    global savas_baltasi_durum
    global titanyum_balta_durum
    global titanyum_kurek_durum
    global titanyum_kazma_durum
    global elmaskazmavarmi
    sayi = 0
    global kazmavarmi
    elmas_kazma_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183062523512111165/basilmiselmaskazma.png?ex=6586f7d5&is=657482d5&hm=a758053fd383447701d0e3b623c78937d8d5acbaced3b68f7bd2703bed385a92&"
    keyboard.wait("enter")
    lapiskoy()
    print(f"{dia_kurek_durum}")
    while True:
        lapisyenile()
        if dia_kazma_durum:
            kazmavarmi = elmaskazmakoy()
            
            if kazmavarmi == False:
                elmaskazmavarmi = False
            else:
                otuzlevelgit()
                
                kontrol = servetbas()
                if kontrol:
                    
                    otuzlvlbekle()
                    pyautogui.leftClick()
                    
                    basilmiselmaskazmaal()
                    sayi += 1
                    webhook_mesaj_gonder(item_ismi="Elmas kazma",resim_url=elmas_kazma_resim_url,aciklama=f"Elmas kazma işlemi başarı ile gerçekleştirildi. \n Başarı ile basılmış item sayısı : {sayi}")      
                else:
                    pyautogui.moveTo(basilacakitem)
                    shiftsolclick()
        if dia_kurek_durum:
            kurekvarmi = elmasKurekKoy()
            
            if kurekvarmi == False:
                elmaskurekvarmi = False
            else:
                otuzlevelgit()
                
                kontrol = servetbas()
                if kontrol:
                    
                    otuzlvlbekle()
                    pyautogui.leftClick()
                    
                    basilmiselmaskazmaal()
                    sayi += 1
                    webhook_mesaj_gonder(item_ismi="Elmas kurek",resim_url=elmas_kazma_resim_url,aciklama=f"Elmas kurek işlemi başarı ile gerçekleştirildi. \n Başarı ile basılmış item sayısı : {sayi}")      
                else:
                    pyautogui.moveTo(basilacakitem)
                    shiftsolclick()
            kitapkoy()
            
            beslevelkitapbas()
            if elmaskazmavarmi == False and elmaskurekvarmi == False:
                pyautogui.moveTo(lapiskordi)
                
                shiftsolclick()
                break
