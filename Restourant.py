menu = {
    "Cheese Burger": 10,
    "Barbekü Deluxe Burger": 20,
    "Vegan Burger": 30,
    "Şefin Özel Tavsiyesi": 40,
    "Peynir Leziz Burger": 50,
    "Adıyaman Çiğköftesi" : 90,
    "Künefe" : 100,
    "Profiterol" : 110,
    "Kola" : 24,
    "Fanta" : 22,
    "Su" : 50,
    "Milkshake" : 20,
    "İtalyan Makarna" : 35,
    "Okul Kantini Tostu" : 10,
    "Pizza Tost" : 15,
    "Döner" : 20
}
#Menü Tanıtımı

masalar = {}
for a in range(1,21):
    masalar[a] = 0
#Masaların tanıtımı


def masalari_goruntule():
    for a in range(1, 21):
        print("{}. Masanın Ücreti: {}".format(a, masalar[a]))
#Masa ücretini yazdıran komut


def menu_goster():
    for x in menu:
          print(x)
#Menüyü yazdıran komut


def siparis_ver():

    flag2 = False
    while (flag2 == False):

        try:
            a = int(input("Masa numarası giriniz: "))
            flag2 = True

        except:
            print("Hatalı bir işlem yaptınız")
            flag2 = False
#Masa numarası yanlış girilirse tekrar girmesini ister


    while (True):
        if (a < 21 and a > 0):
#Masa numarası istenen aralıkta mı diye kontrol eder

            print("""
                1-Yeni Sipariş Gir
                2-Ana menüye dön""")


            flag3 = False
            while (flag3 == False):
                try:
                    secim = int(input("Seçiminiz?"))
                    flag3 = True
                except:
                    print("Hatalı bir işlem yaptınız")
                    flag3 = False
#Seçimini alır ve yanlış değerse tekrar ister


            if (secim == 1):
                print("Yemekler:")
                menu_goster()
#Sipariş ekranında menü gösterir

                flag4 = False
                while (flag4 == False):

                    try:
                        urun = str(input("\nNe Almak İstersiniz:\n"))
                        flag4 = True

                    except:
                        print("Hatalı bir işlem yaptınız")
                        flag4 = False
#İstenilen veri (Sipariş edilen yemek) yanlış girilirse tekrar girmesini ister

                flag5 = False
                while (flag5 == False):

                    try:
                        miktar = float(input("Kaç adet?"))
                        flag5 = True

                    except:
                        print("Hatalı bir işlem yaptınız")
                        flag5 = False
#İstenilen veri (Sipariş adedi) yanlış girilirse tekrar girmesini ister

                toplam = masalar[a] + float(menu[urun]) * miktar
                masalar[a] = toplam
                break
#Siparişi alır ve veriyi günceller

            elif (secim == 2):
                break
#Ana menüye döndürür

            else:
                print("Hatalı bir giriş yaptınız.")
                break
#Tekrar hangi seçimi istediğini sorar


        else:
            print("Hatalı bir işlem yaptınız")
            break
#Masa numarası yanlış girilirse tekrar ister


def hesap_cikar():

    flag6 = False
    while (flag6 == False):

        try:
            a = int(input("Masa numarası giriniz: "))
            flag6 = True

        except:
            print("Hatalı bir işlem yaptınız")
            flag6 = False
#Masa numarası yanlış girilirse tekrar girmesini ister

    while (True):

        if (a < 21 and a > 0):
#Masa numarası istenen aralıkta mı kontrol eder

            if (masalar[a] == 0):
                print("Ödemeniz gereken tutar: ", masalar[a], "TL")
                return 0
            print("Ödemeniz gereken tutar: ", masalar[a], "TL")
#Ödenilmesi gereken tutar 0 ise ödemeyi durdurur

            while (True):

                flag7 = False
                while (flag7 == False):

                    try:
                        odenen_tutar = float(input("Ödeme yapın: "))
                        flag7 = True

                    except:
                        print("Hatalı bir işlem yaptınız")
                        flag7 = False
#İstenilen veri(ödenilen para miktarı) hatalı ise tekrar ister

                if (masalar[a] == odenen_tutar):
                    total = masalar[a] - odenen_tutar
                    masalar[a]=0
                    print("Faturanız ödenmiştir.")
                    break
#ödenilen tutar faturaya eşitse ödemeyi alır ve bitirir

                elif (odenen_tutar > masalar[a]):
                    print("Para üstünüz: ", odenen_tutar - masalar[a], "TL")
                    masalar[a] = float(0)
                    break
#ödenilen tutar faturadan fazlaysa ödemeyi alır ve para üstü verir

                elif (masalar[a] > odenen_tutar):
                    total = masalar[a] - odenen_tutar
                    masalar[a] = total
                    break
#Fatura ödenilen tutardan daha fazla ise ödemeyi alır ve kalan tutarı ister

        else:
            print("Hatalı bir işlem yaptınız")
            break
#Masa numarası istenilen aralık dışındaysa ana menüye döndürür


def hesap_kontrolu(dosya_adi):
    try:
        file = open(dosya_adi)
        bilgiler = file.read()
        bilgiler = bilgiler.split("\n")
        bilgiler.pop()
        file.close()
        kontrol = True
    except FileNotFoundError:
        file = open(dosya_adi,"x")
        file.close()
        print("Dosya sıfırdan oluşturuldu.")
        kontrol = False

    if (kontrol):
        for a in enumerate(bilgiler):
            masalar[a[0]] = float(a[1])

    else:
        pass


def guncelle():
    file = open("masalar.txt","w")
    file.write("0")
    for a in range(1,21):
        ucret = masalar[a]
        ucret = str(ucret)
        file.write("\n"+ucret)
    file.close()
#dosyadaki masa verilerini günceller

def fonksiyon():
    hesap_kontrolu("masalar.txt")

    while True:

        guncelle()
        print("""
        1-Masaları Görüntüle
        2-Sipariş Ver
        3-Hesap Öde
        4-Çıkış yap
        """)

        flag8 = False
        while (flag8 == False):

            try:
                secim2 = int(input("Yapmak istediğiniz işlemi seçiniz: "))
                flag8 = True
            except:
                print("Hatalı bir işlem yaptınız")
                flag8 = False
#Yapılmak istenilen işlem seçimi yanlış ise tekrar ister



        if (secim2 == 1):
            masalari_goruntule()
        elif(secim2 == 2):
            siparis_ver()
        elif(secim2 == 3):
            hesap_cikar()
        elif (secim2 == 4):
            quit()
        else:
            print("Lütfen tabloya göre işlem yapınız.")
#istenilen işleme yönlendirir ve işlem bitince ana menüye döndürür

fonksiyon()