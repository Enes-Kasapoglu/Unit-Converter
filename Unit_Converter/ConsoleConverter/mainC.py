import os

print("\nBirim Çevirme Programına Hoşgeldiniz.")

while True:
    
    print("\n1- Sıcaklık Birimleri") 
    print("2- Uzunluk Birimleri")
    print("0- Çıkış\n")
    
    homeChoice = int(input("Seçiminizi Yapınız: "))
    
    if(homeChoice==1):
        
        while True:
            
            print("\n1- Derece(*C) - Fahrenheit(F)")
            print("2- Fahrenheit(F)- Derece(*C)")
            print("3- Derece(*C) - Kelvin(K)")
            print("4- Fahrenheit(F) - Kelvin(K)")
            print("5- Kelvin(K) - Derece(*C)")
            print("6- Kelvin(K) - Fahrenheit(F)")
            print("0- Çıkış\n")
        
            sChoice = int(input("Seçiminizi Yapınız: "))
            
            if(sChoice == 0):
                break
            
            elif(sChoice == 1):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    derece = float(input("Fahrenheit birimine çevirmek istediğiniz Derece değerini giriniz: "))
                    if(derece == 000):
                        break
                    else:    
                        fahrenheit = (derece*9/5)+32
                        print("\nF: {0}\n".format(fahrenheit))
            
            elif(sChoice == 2):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    fahrenheit = float(input("Derece birimine çevirmek istediğiniz Fahrenheit değerini giriniz: "))
                    if(fahrenheit == 000):
                        break
                    else:    
                        derece = (fahrenheit-32)*5/9
                        print("\n*C: {0}\n".format(derece))
                        
            elif(sChoice == 3):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    derece = float(input("Kelvin birimine çevirmek istediğiniz Derece değerini giriniz: "))
                    if(derece == 000):
                        break
                    else:    
                        kelvin = derece + 273.15
                        print("\nK: {0}\n".format(kelvin))
                        
            elif(sChoice == 4):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    fahrenheit = float(input("Kelvin birimine çevirmek istediğiniz Fahrenheit değerini giriniz: "))
                    if(fahrenheit == 000):
                        break
                    else:
                        derece = (fahrenheit-32)*5/9
                        kelvin =  derece + 273.15
                        print("\nK: {0}\n".format(kelvin))
                        
            elif(sChoice == 5):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    derece = float(input("Derece birimine çevirmek istediğiniz Kelvin değerini giriniz: "))
                    if(derece == 000):
                        break
                    else:
                        kelvin =  derece - 273.15
                        print("\n*C: {0}\n".format(kelvin))
                        
            elif(sChoice == 6):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    kelvin = float(input("Fahrenheit birimine çevirmek istediğiniz Kelvin değerini giriniz: "))
                    if(kelvin == 000):
                        break
                    else: 
                        fahrenheit = (kelvin-273.15)*1.8000 + 32.00
                        print("\nF: {0}\n".format(fahrenheit))
            
            
    elif(homeChoice == 2):
        
        while True:
            
            print("\n1- Milimetre(mm) - Santimetre(cm)")
            print("2- Milimetre(mm) - Metre(M)")
            print("3- Santimetre(cm) - Milimetre(mm)")
            print("4- Santimetre(cm) - Inç(Inch)")
            print("5- Santimetre(cm) - Metre(M)")
            print("6- Santimetre(cm) - Kilometre(Km)")
            print("7- Metre(M) - Milimetre(mm)")
            print("8- Metre(M) - Santimetre(cm)")
            print("9- Metre(M) - Kilometre(Km)")
            print("10- Kilometre(Km) - Santimetre(cm)")
            print("11- Kilometre(Km) - Metre(M)")
            print("0- Çıkış\n")
       
            uChoice = int(input("Seçiminizi Yapınız: "))
            
            if(uChoice == 0):
                break
            
            elif(uChoice == 1):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    mm = float(input("Santimetre birimine çevirmek istediğiniz Milimetre değerini giriniz: "))
                    if(mm == 000):
                        break
                    else: 
                        cm =  mm/10.000
                        print("cm: {0}\n".format(cm))
                        
            elif(uChoice == 2):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    mm = float(input("Metre birimine çevirmek istediğiniz Milimetre değerini giriniz: "))
                    if(mm == 000):
                        break
                    else: 
                        M =  mm/1000
                        print("M: {0}\n".format(M))
                        
            elif(uChoice == 3):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    cm = float(input("Milimetre birimine çevirmek istediğiniz Santimetre değerini giriniz: "))
                    if(cm == 000):
                        break
                    else: 
                        mm =  cm/0.10000
                        print("mm: {0}\n".format(mm))
                        
            elif(uChoice == 4):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    cm = float(input("İnç birimine çevirmek istediğiniz Santimetre değerini giriniz: "))
                    if(cm == 000):
                        break
                    else: 
                        inc =  cm * 0.39370
                        print("Inch: {0}\n".format(inc))
                        
            elif(uChoice == 5):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    cm = float(input("Metre birimine çevirmek istediğiniz Santimetre değerini giriniz: "))
                    if(cm == 000):
                        break
                    else: 
                        M =  cm / 100.00
                        print("M: {0}\n".format(M))
                        
            elif(uChoice == 6):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    cm = float(input("Kilometre birimine çevirmek istediğiniz Santimetre değerini giriniz: "))
                    if(cm == 000):
                        break
                    else: 
                        Km =  cm / 100000
                        print("Km: {0}\n".format(Km))
                        
            elif(uChoice == 7):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    M = float(input("Milimetre birimine çevirmek istediğiniz Metre değerini giriniz: "))
                    if(M == 000):
                        break
                    else: 
                        mm =  M / 0.0010000
                        print("mm: {0}\n".format(mm))
            
            elif(uChoice == 8):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    M = float(input("Santimetre birimine çevirmek istediğiniz Metre değerini giriniz: "))
                    if(M == 000):
                        break
                    else: 
                        cm =  M / 0.010000
                        print("cm: {0}\n".format(cm))
                        
            elif(uChoice == 9):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    M = float(input("Kilometre birimine çevirmek istediğiniz Metre değerini giriniz: "))
                    if(M == 000):
                        break
                    else: 
                        Km =  M / 1000.0
                        print("Km: {0}\n".format(Km))
                        
            elif(uChoice == 10):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    Km = float(input("Santimetre birimine çevirmek istediğiniz Kilometre değerini giriniz: "))
                    if(Km == 000):
                        break
                    else: 
                        cm =  Km / 0.00010000
                        print("cm: {0}\n".format(cm))
                        print("Artış sayısı 1")
                        
            elif(uChoice == 11):
                while True:
                    print("")
                    print("Çıkış Yapmak için '000' yazın")
                    print("")
                    Km = float(input("Metre birimine çevirmek istediğiniz Kilometre değerini giriniz: "))
                    if(Km == 000):
                        break
                    else: 
                        M =  Km / 0.0010000
                        print("M: {0}\n".format(M))
                        
    elif(homeChoice == 0):
        break
    else:
        print("Üzgünüm, böyle bir seçenek bulunmamaktadır.")
        break