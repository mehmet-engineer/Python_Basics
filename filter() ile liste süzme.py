def filtrele(n):
    return n>=70  #girilen değer 70den yüksek ise True çıktısı ver
                                #n>=70 ifadesinin sorgulamasını döndür...
notlar = {'Ahmet' : 60,
          'Sinan' : 50,
          'Mehmet' : 45,
          'Cem' : 98,
          'Can' : 51,
          'Hakan' : 66,
          'Mahmut' : 80}

puanlar = notlar.values()     #filter(True ifadeli Fonksiyon, uygulanan liste)
süzülmüş_hal = filter(filtrele, puanlar)

print(*süzülmüş_hal)    #her bir puanı yan yana diz
    
