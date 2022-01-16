ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:                          #(Hata içerme ihtimalleri try içinde denenir)
    sayı1 = int(ilk_sayı)     #("except hata_adı:" ile hata vermesi yerine alt işlemler yaptırılır) 
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError:
    print("\n Geçersiz veri girişi. Lütfen bir sayı girin!")
except ZeroDivisionError:
    print("\n Bir sayı sıfıra bölünemez!")
except:
    print("\n Beklenmedik bir hata oluştu")
    #(Eğer başka bir sorun varsa...)
finally:
    print("Finally her zaman çağrılır...")