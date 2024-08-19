import random
import sys


def tas_kagit_makas_MUSTAFA_BERAT_BERBER():

    kullanici_genel_skor = 0
    bil_genel_skor = 0
    kullanici_secim = ""
    bil_secim = ""
    secenekler = ["taş", "kağıt", "makas", "spock", "kertenkele"]
    tur_sayac = 0
    seans_sayac = 0


    #kullanici oyun hakkinda bilgilendiriliyor
    bilgilendirme = """########## BİLGİLENDİRME ##########\n
Selam, Hoşgeldin! Bu Oyun Taş, Kağıt, Makas Oyunun The Big Bang Theory Versiyonudur.
5 Tane Seçeneğiniz Var: Taş, Kağıt, Makas, Spock, Kertenkele
    
Kurallar Şöyle:
Bir Oyunda Kimin Tur Sonu Skoru Önce 2'ye Ulaşırsa Oyunu Kazanır.
Kimin Genel Skoru Önce 2'ye Ulaşırsa Oyunu Kazanır.
İstediğiniz Zaman Sonlandırabilir Veya Tamamen Oyundan Çıkabilirsiniz.
    
Seçeneklerin Birbirlerine Göre Üstünlük Durumu Şöyle:
Taş > Kertenkele
Taş > Makas
Kağıt > Spock
Kağıt > Taş
Makas > Kağıt
Makas > Kertenkele
Spock > Taş
Spock > Makas
Kertenkele > Kağıt
Kertenkele > Spock

Bilgilendirme Bu Kadardı İyi Şanslar!"""

    print(bilgilendirme)

#Kod tasarimi ve while dongulerinin kullanimi:
#Kullanicidan input almak icin kullanilan try-except ve while donguleri haricince 3 ana while dongusu var:

#3. katman: turları temsil eden while dongusu -> kullanici veya bilgisayarin tur sonu skoru 2 olana kadar devam ediyor

#2. katman: seansları temsil eden while dongusu -> Bilgisayarin ve kullanicinin genel skorlari burada.
#Turlari temsil eden while'dan cikilinca kim daha yüksekse onun genel skoruna 1 ekleniyor

#1. katman: genel oyunu temsil eden while donugusu -> Bu dongu seanslari icine alir.
#Eger kullanici genel skorları sifirlamak isterse programi acip kapatmasina gerek kalmaz.

    while True:
        #Oyuna baslamak icin onay aliniyor.

        try:
            kullanici_secim = input("Başlamak İster Misiniz(Evet / Hayır)?")
            kullanici_secim = kullanici_secim.strip()
            
        except:
            print("Tekrar Deneyin.")

        if kullanici_secim == "evet" or kullanici_secim == "hayır":
            break

    if kullanici_secim.lower() == "hayır":
        print("Madem oynamayacaktin oyuna neden girdin kardeşim? Neyse görüşürüz.")
        sys.exit()

    #1. katman while dongusu
    while True:

        

        #Genel oyun icin belirlenen skorlar.
        kullanici_genel_skor = 0
        bil_genel_skor = 0


        #Genel oyunu temsil eden while dongusu.
        while True:

            #seans bitiminde ortaya cikan skorlar
            kullanici_seans_skor = 0
            bil_seans_skor = 0

            print(f"########## {seans_sayac + 1}. SEANS ##########")
            print(f"""\
########## GENEL SKOR TABLOSU ##########
Siz: {kullanici_genel_skor}
Bilgisayar: {bil_genel_skor}""")


            #bir seansı temsil eden while döngüsü
            while True:     
                print(f"########## {tur_sayac+1}. TUR ##########")
                
                #kullanıcıdan düzgün bir girdi almak için while döngüsü içinde try-except kullanıldı
                while True:     
                    
                    try:
                        
                        kullanici_secim = input("""\
Lütfen Seçiminizi Yapın (Taş, Kağıt, Makas, Spock, Kertenkele)
Ya Da Bu Seansı Sonlandırmak İsterseniz "Çıkış" Yazın: """)
                        
                        kullanici_secim = kullanici_secim.lower()

                        if kullanici_secim in secenekler or kullanici_secim == "çıkış" or kullanici_secim == "cikis":
                            break
                    except:
                        print("Lütfen Tekrar Seçim Yapın: ")

                if kullanici_secim == "cikis" or kullanici_secim == "çıkış":
                    print("Seans sonlandırılıyor.")
                    break
                else:
                    bil_secim = random.choice(secenekler)

                    print(f"""
Siz: {kullanici_secim.capitalize()}
Bilgisayar: {bil_secim.capitalize()}""")

                    if bil_secim == kullanici_secim:
                        print("Berabere!")

                    elif kullanici_secim == "taş" and bil_secim == "kertenkele" or \
                        kullanici_secim == "taş" and bil_secim == "makas" or \
                        kullanici_secim == "kağıt" and bil_secim == "spock" or \
                        kullanici_secim == "kağıt" and bil_secim == "taş" or \
                        kullanici_secim == "makas" and bil_secim == "kağıt" or \
                        kullanici_secim == "makas" and bil_secim == "kertenkele" or \
                        kullanici_secim == "spock" and bil_secim == "taş" or \
                        kullanici_secim == "spock" and bil_secim == "makas" or \
                        kullanici_secim == "kertenkele" and bil_secim == "kağıt" or \
                        kullanici_secim == "kertenkele" and bil_secim == "spock":

                        print("Siz Kazandınız!")
                        kullanici_seans_skor = kullanici_seans_skor + 1

                    else:
                        print("Bilgisayar Kazandı!")
                        bil_seans_skor = bil_seans_skor + 1

                    print(f"""
########## SKOR TABLOSU ##########
Siz: {kullanici_seans_skor}
Bilgisayar: {bil_seans_skor}
########## SKOR TABLOSU ##########""")

                    if kullanici_seans_skor == 2 or bil_seans_skor == 2:
                        print("Bu seans bitmiştir.")

                        if kullanici_seans_skor == 2:
                            print("Siz Kazandınız!")
                            kullanici_genel_skor = kullanici_genel_skor + 1
                        else:
                            print("Bilgisayar Kazandı!")
                            bil_genel_skor = bil_genel_skor + 1
                        break

                    
                    #kullaniciya seansa devam etmek isteyip istemedigi soruluyor
                    while True:     
                        try:
                            secim = input("Devam Etmek İster misiniz(Evet / Hayır)?: ")
                            secim = secim.lower()

                        except:
                            print("Lütfen Tekrar Deneyin: ")
                            secim = input("Devam Etmek İster misiniz(Evet / Hayır)?: ")
                            secim = secim.lower()

                        if secim == "evet" or secim == "hayır":
                            break

                    if secim == "hayır":
                        break
                    else:
                        tur_sayac = tur_sayac + 1

                        print(f"""\
########## GENEL SKOR TABLOSU ##########
Siz: {kullanici_genel_skor}
Bilgisayar: {bil_genel_skor}""")
                        
            if kullanici_genel_skor == 2:
                
                print("Oyunu Siz Kazandınız!")
                break
            elif bil_genel_skor == 2:
                print("Oyunu Bilgisayar Kazandı!")
                break


            #tur sayaci resetleniyor
            tur_sayac = 0

            #Kullaniciya oyundan cikmak isteyip istemedigi soruluyor
            while True:     
                try:
                    kullanici_secim = input("Genel Skoru Resetleyip Sıfırdan Başlamak İçin 'Evet', Devam Etmek İçin 'Hayır' Girin.(Evet / Hayır)?: ").lower()

                    if kullanici_secim == "evet" or kullanici_secim == "hayır":
                        break
                except:
                    print("Lütfen Tekrar Deneyin: ")

            if kullanici_secim == "hayır":

                
                #kullanici oyuna devam etmek istedigi icin ayni soru bilgisayara soruluyor
                print("-" * 20)
                print("Sayın Bilgisayar, Siz Devam Etmek İster Misiniz?")
                
                #bilgisayarin karari devam etme ihtimali %50 olarak ayarlandi
                bil_secim = random.randint(0, 1)

                if bil_secim == 1:
                    print("Evet, Devam Etmek İsterim!")
                    seans_sayac = seans_sayac + 1
                else:
                    print("Hayır, Ben Devam Etmek İstemiyorum!")

            if kullanici_secim == "evet" or bil_secim == 0:
                print("Oyun Sonlandırılıyor. Görüşmek Üzere!")
                seans_sayac = 0
                break

tas_kagit_makas_MUSTAFA_BERAT_BERBER()