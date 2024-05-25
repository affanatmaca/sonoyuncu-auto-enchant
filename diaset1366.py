import pyautogui as p
import keyboard
import time
import json
import requests

dia_kask_durum = False
dia_cp_durum = False
dia_pant_durum = False
dia_bot_durum = False

tit_kask_durum = False
tit_cp_durum = False
tit_pant_durum = False
tit_bot_durum = False

dia_kazma_durum = False
dia_kurek_durum = False
dia_balta_durum = False
dia_kilic_durum = False
tit_kilic_durum = False
yay_durum = False

##### 

tkafalikvarmi = None
tkilicvarmi = None
tgoguslukvarmi = None
tpantvarmi = None
tayakkabivarmi = None
kaskvarmi = None
goguslukvarmi = None
pantvarmi = None
ayakkabivarmi = None
kilicvarmi = None
yayvarmi = None
levelbesvarmi = None
lvlkontrol = None

diakafalikkontrol = None
diagoguslukvarmi = None
diapantkontrol = None
diaayakkabivarmi = None

lvlotuzsagalt = [836 , 338]
lvlbesagalt = [836, 260]
basilacakitem = [555 , 314]
lapiskordi = [590 , 314]
ekransolalt = [91 ,657]

kitapxy1 = [531, 293]
kitapxy2 = [571, 333]
lapisxy1 = [571, 293]
lapisxy2 = [613, 334]


def shiftsolclick():
    p.keyDown("shift")
    p.leftClick()
    p.keyUp("shift")


def checkboxlogla():
    print(f"tit kask : {tit_kask_durum}")
    print(f"tit cp : {tit_cp_durum}")
    print(f"tit pant : {tit_pant_durum}")
    print(f"tit bot : {tit_bot_durum}")

    print(f"elmas kask : {dia_kask_durum}")
    print(f"elmas cp : {dia_cp_durum}")
    print(f"elmas pant : {dia_pant_durum}")
    print(f"elmas bot : {dia_bot_durum}")

    print(f"elmas kilic : {dia_kilic_durum}")
    print(f"yay  : {yay_durum}")

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

def dia_kilic_koy():
    keyboard.wait("enter")
    try:
        kaskbul = p.locateOnScreen("images/kilic.png" , confidence=0.992)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False




def t_kilic_koy():
    try:
        kaskbul = p.locateOnScreen("images/titkilic.png" , confidence=0.999)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False
    
############################

def yay_koy():
    try:
        kaskbul = p.locateOnScreen("images/yay.png" , confidence=0.999)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False

def yay_al():
    try:
        kaskbul = p.locateOnScreen("images/yay.png" , confidence=0.999)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False


################

def t_kask_koy():
    try:
        kaskbul = p.locateOnScreen("images/tkask.png")
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False




################

################

def t_gogusluk_koy():
    try:
        kaskbul = p.locateOnScreen("images/tgogusluk.png")
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False


################

def t_pant_koy():
    try:
        kaskbul = p.locateOnScreen("images/tpant.png")
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False



################

def t_ayakkabi_koy():
    try:
        kaskbul = p.locateOnScreen("images/tayakkabi.png")
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False


def basilmis_t_ayakkabi_al():
    try:
        kaskbul = p.locateOnScreen("images/basilmistbot.png" ,confidence=0.9)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False

################

################

def dia_kask_koy():
    try:
        kaskbul = p.locateOnScreen("images/kask.png" , grayscale=True)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False




################

def dia_gogusluk_koy():
    try:
        kaskbul = p.locateOnScreen("images/gogusluk.png" , grayscale=True)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False



################

def dia_pant_koy():
    try:
        kaskbul = p.locateOnScreen("images/pant.png" , grayscale=True)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False



################

def dia_ayakkabi_koy():
    try:
        kaskbul = p.locateOnScreen("images/ayakkabi.png" , grayscale=True)
        if kaskbul is not None:
            p.moveTo(kaskbul)
            
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        return False


################


def otuzlvlbekle():
    p.moveTo(ekransolalt)
    try:
        solaltparlak = p.locateOnScreen("images/level30renkli.png")
    except p.ImageNotFoundException:
        solaltparlak = None

    while solaltparlak is None:
        try:
            solaltparlak = p.locateOnScreen("images/level30renkli.png")
            if solaltparlak:
                break
        except p.ImageNotFoundException:
            pass

    p.moveTo(lvlotuzsagalt)

def kitapkoy():
    try:
        book = p.locateOnScreen("images/kitap.png")
        if book is not None:
            p.moveTo(book)
            time.sleep(0.3)
            p.keyDown("shift")
            p.leftClick()
            p.keyUp("shift")
    except p.ImageNotFoundException:
        print("kitap bulunamadı")

def lapiskoy():
    try:
        lapis = p.locateOnScreen("images/lapis.png" , confidence=0.9)
        if lapis is not None:
            
            p.moveTo(lapis)
            time.sleep(0.3)
            p.keyDown('shift')
            p.leftClick()
            p.keyUp('shift')
        else:
            return False
    except p.ImageNotFoundException:
        print("lapisi bulunamadı")

def lapisyenile():
    try:
        lapis = p.locateOnScreen("images/lapis.png" , confidence=0.9)
        if lapis is not None:
            
            p.moveTo(lapiskordi)
            time.sleep(0.3)
            p.doubleClick()
            time.sleep(0.1)
            p.leftClick()
        else:
            return False
    except p.ImageNotFoundException:
        print("lapisi bulunamadı")

def koruma4check():
    try:
        kirkontrol = p.locateOnScreen("images/koruma4.jpg" , confidence=0.9 ,grayscale=True)
        return True
    except p.ImageNotFoundException:
        return False

def keskinlik4check():
    try:
        kirkontrol = p.locateOnScreen("images/keskinlik4.png", confidence=0.8 ,grayscale=True)
        return True
    except p.ImageNotFoundException:
        return False

def yumrukcheck():
    try:
        kirkontrol = p.locateOnScreen("images/yumruk2.png", confidence=0.8 ,grayscale=True)
        return True
    except p.ImageNotFoundException:
        return False

def otuzlevelgit():
    global lvlkontrol
    try:
        lvlkontrol = p.locateOnScreen("images/level30renkli.png")
    except p.ImageNotFoundException:
        lvlkontrol = False
        pass

    if lvlkontrol:
        p.moveTo(lvlkontrol)
    else:
        try:
            lvlkontrol2 = p.locateOnScreen("images/level30renksiz.png")
            if lvlkontrol2:
                p.moveTo(lvlotuzsagalt)
        except p.ImageNotFoundException:
            return print("bug oluştu!")

def beslevelkitapbas():
    global levelbesvarmi
    try:
        sagust = p.locateOnScreen("images/level5renkli.png")
        levelbesvarmi = True
    except p.ImageNotFoundException:
        sagust = None

    if sagust is None:
        while sagust is None:
            try:
                sagust = p.locateOnScreen("images/level5renkli.png")
                if sagust:
                    break
            except p.ImageNotFoundException:
                pass
    if levelbesvarmi == True:
        p.moveTo(lvlbesagalt)
        p.leftClick()
            
    try:
        enchbook = p.locateOnScreen("images/basilmiskitap.png", confidence=0.8)
        if enchbook:
            p.moveTo(enchbook)
            p.keyDown('q')
            p.keyUp('q')
    except p.ImageNotFoundException:
        print("basilmis kitap bulunamadı")

def otuzlevelgit():
    p.moveTo(lvlotuzsagalt)
    


def main():
    global tkafalikvarmi
    global tgoguslukvarmi
    global tpantvarmi
    global tayakkabivarmi
    global kaskvarmi
    global goguslukvarmi
    global pantvarmi
    global ayakkabivarmi
    global kilicvarmi
    global yayvarmi
    
    global dia_pant_durum
    global dia_bot_durum
    global dia_kask_durum
    global dia_cp_durum
    global tit_kask_durum
    global tit_cp_durum
    global tit_pant_durum
    global tit_bot_durum
    global dia_kilic_durum
    global yay_durum
    global tkilicvarmi

    keyboard.wait("enter")
    checkboxlogla()
    kafalik_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183080398511669339/Enchanted_Diamond_Helmet_29-3.png?ex=6587087b&is=6574937b&hm=14052bc038f042207339889552abda1a3dcec928e1c73f2b0370d717ca1c7268&"
    cp_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183079675896012871/unnamed.png?ex=658707cf&is=657492cf&hm=9759cdd1b557ded51eec655e89d1ef453f7849b16372b234d5968a98110fc93a&"
    pant_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183080398830457002/Enchanted_Diamond_Leggings_29-28.png?ex=6587087b&is=6574937b&hm=7518144a94faf7ab85d3050533a736eb4c6eb8e111fe4290a83ec8a8cb8bbf39&"
    bot_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183079675652755497/Diamond_Enchanted_Boots.png?ex=658707cf&is=657492cf&hm=577212fafb6e663a8920bc28bdf14417333273f438218b3f40c2986e180f1ca7&"

    tkafalik_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183083055087353906/basilmistkask.png?ex=65870af4&is=657495f4&hm=4b1f18aacf172d6f3df8143d8c7a950f0a51fd32533d5f106acf1d0281e8f026&"
    tcp_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183083054466613338/basilmistgogusluk.png?ex=65870af4&is=657495f4&hm=24efd8af95d19dc7720d9c732c9b7f083a62523782d743ff4c9c6e4d19cd9652&"
    tpant_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183083054785384529/basilmistpant.png?ex=65870af4&is=657495f4&hm=b6b3599ddd93283ef9544f29900a67d4b91aa5ad1e3a30f9864477ed4516e9a5&"
    tbot_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183083054223327232/basilmistbot.png?ex=65870af4&is=657495f4&hm=986f14562da93375d706ce471e2d7646abd78cc89e1c022c794e85a701d2bffe&"

    kilic_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183079676969762816/basilmiskilic.png?ex=658707cf&is=657492cf&hm=8ae642a440969787439f71870b83cb67ce6046df18b83728b3663303edd2f26a&"
    yay_resim_url = "https://cdn.discordapp.com/attachments/1183062249720516649/1183079676713914528/basilmisyay.png?ex=658707cf&is=657492cf&hm=f29c7e407031e3dda14b472a23df0a24804d2d454ce73abe8ecee0c1e6b0e134&"  

    kafaliksayac = 0
    cpsayac = 0
    pantsayac = 0
    botsayac = 0
    tkafaliksayac = 0
    tcpsayac = 0
    tpantsayac = 0
    tbotsayac = 0
    diakilicsayac = 0
    yaysayac = 0
    tkilicsayac = 0
    lapiskoy()
    while True:
        lapisyenile()
        if dia_kask_durum:
            diakaskvarmi = dia_kask_koy()
            if diakaskvarmi == False:
                diakafalikkontrol = False
            else:
                otuzlevelgit()  
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    kafaliksayac += 1
                    webhook_mesaj_gonder(item_ismi="Elmas kask",resim_url=kafalik_resim_url,aciklama=f"Seçtiğiniz elmas kask basıldı. \n Başarı ile basılmış item sayısı : {kafaliksayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()

        if dia_cp_durum:
            diamemelikvarmi = dia_gogusluk_koy()
            if diamemelikvarmi == False:
                diagoguslukvarmi = False
            else:
                otuzlevelgit()
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    cpsayac += 1
                    webhook_mesaj_gonder(item_ismi="Elmas göğüslük",resim_url=cp_resim_url,aciklama=f"Seçtiğiniz elmas göğüslük basıldı. \n Başarı ile basılmış item sayısı : {cpsayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
        if dia_pant_durum:
            diapantvarmi = dia_pant_koy()
            if diapantvarmi == False:
                diapantkontrol = False
            else:
                otuzlevelgit()
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    
                    otuzlvlbekle()
                    p.leftClick()
                    pantsayac += 1
                    webhook_mesaj_gonder(item_ismi="Elmas pant",resim_url=pant_resim_url,aciklama=f"Seçtiğiniz elmas pant basıldı. \n Başarı ile basılmış item sayısı : {pantsayac}")
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()

        if dia_bot_durum:
            papucvarmi = dia_ayakkabi_koy()
            if papucvarmi == False:
                diaayakkabivarmi = False
            else:
                otuzlevelgit()
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    botsayac += 1
                    webhook_mesaj_gonder(item_ismi="Elmas bot",resim_url=bot_resim_url,aciklama=f"Seçtiğiniz elmas bot basıldı. \n Başarı ile basılmış item sayısı : {botsayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()

        if tit_kask_durum:
            tkaskvarmi = t_kask_koy()
            if tkaskvarmi == False:
                tkafalikvarmi = False
            else:
                otuzlevelgit()
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    tkafaliksayac += 1
                    webhook_mesaj_gonder(item_ismi="Titanyum kask",resim_url=tkafalik_resim_url,aciklama=f"Seçtiğiniz titanyum kafalık basıldı. \n Başarı ile basılmış item sayısı : {tkafaliksayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
        if tit_cp_durum:
            memelikvarmi = t_gogusluk_koy()
            if memelikvarmi == False:
                tgoguslukvarmi = False
            else:
                otuzlevelgit()
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    tcpsayac += 1
                    webhook_mesaj_gonder(item_ismi="Titanyum göğüslük",resim_url=tcp_resim_url,aciklama=f"Seçtiğiniz titanyum göğüslük basıldı. \n Başarı ile basılmış item sayısı : {tcpsayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
        if tit_pant_durum:
            tpantvarmiw = t_pant_koy()
            if tpantvarmiw == False:
                tpantvarmi = False
            else: 
                otuzlevelgit()
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    tpantsayac += 1
                    webhook_mesaj_gonder(item_ismi="Titanyum pantalon",resim_url=tpant_resim_url,aciklama=f"Seçtiğiniz titanyum pantalon basıldı. \n Başarı ile basılmış item sayısı : {tpantsayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
        if tit_bot_durum:
            tbotvarmi = t_ayakkabi_koy()
            if tbotvarmi == False:
                tayakkabivarmi = False
            else:
                otuzlevelgit()
                
                kontrol = koruma4check()
                time.sleep(0.25)
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    tbotsayac += 1
                    webhook_mesaj_gonder(item_ismi="Titanyum bot",resim_url=tbot_resim_url,aciklama=f"Seçtiğiniz titanyum bot basıldı. \n Başarı ile basılmış item sayısı : {tbotsayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()

        if dia_kilic_durum:
            kilickon = dia_kilic_koy()
            if kilickon == False:
                kilicvarmi = False
            else:
                otuzlevelgit()
                
                kontrol = keskinlik4check()
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    diakilicsayac += 1
                    webhook_mesaj_gonder(item_ismi="Elmas kılıç",resim_url=kilic_resim_url,aciklama=f"Seçtiğiniz elmas kılıç basıldı. \n Başarı ile basılmış item sayısı : {diakilicsayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
        if tit_kilic_durum:
            tkilickoy = t_kilic_koy()
            if tkilickoy == False:
                tkilicvarmi = False
            else:
                otuzlevelgit()
                
                kontrol = keskinlik4check()
                if kontrol:
                    
                    otuzlvlbekle()
                    p.leftClick()
                    tkilicsayac += 1
                    webhook_mesaj_gonder(item_ismi="Titanyum kılıç",resim_url=kilic_resim_url,aciklama=f"Seçtiğiniz Titanyum kılıç basıldı. \n Başarı ile basılmış item sayısı : {diakilicsayac}")
                    
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()
                else:
                    p.moveTo(basilacakitem)
                    time.sleep(0.3)
                    shiftsolclick()     
        if yay_durum:
            try:
                yaykontrol = yay_koy()
                if yaykontrol == False:
                    yayvarmi = False
                else:
                    otuzlevelgit()
                    
                    kontrol = yumrukcheck()
                    if kontrol:
                        
                        otuzlvlbekle()
                        p.leftClick()
                        yaysayac += 1
                        webhook_mesaj_gonder(item_ismi="Yay",resim_url=yay_resim_url,aciklama=f"Seçtiğiniz yay basıldı. \n Başarı ile basılmış item sayısı : {yaysayac}")
                        
                        p.moveTo(basilacakitem)
                        time.sleep(0.3)
                        shiftsolclick()
                    else:
                        yay_al()
            except p.ImageNotFoundException:
               yayvarmi = False
                        

        kitapkoy()
        lapisyenile()
        beslevelkitapbas()
        if tkafalikvarmi == False and tgoguslukvarmi == False and tpantvarmi == False and tayakkabivarmi == False and diakafalikkontrol == False and diagoguslukvarmi == False and diapantkontrol == False and diaayakkabivarmi == False and kilicvarmi == False and yayvarmi == False and tkilicvarmi:
            p.keyDown('escape')
            p.keyUp('escape')
            break