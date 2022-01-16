import datetime

şuan = datetime.datetime.now()    #modülün datetime sınıfından metot fonksiyonu
print("yıl:", şuan.year)
print("ay:", şuan.month) 
print("gün:", şuan.day) 
print("saat:", şuan.hour) 
print("dakika:", şuan.minute)

tarih = datetime.datetime.ctime(şuan)   #now() parametresiyle özet tarih verir
print("Özet tarih:", tarih)

print("--------------------------------------------------------")

#iki tarih arası toplam günü bulma;
bugün = datetime.datetime.today()
hedef_tarih = datetime.datetime(2023,1,1)   #2023 ocak 1'den...
kalan_bilgi = hedef_tarih - bugün
print("Kalan gün:", kalan_bilgi.days)

print("--------------------------------------------------------")

#bilmem kaç gün sonra veya önce hangi tarihe denk gelir?
bugün = datetime.datetime.today()
ek_gün = datetime.timedelta(days=200)     #200 gün sonra...
gelecek = bugün + ek_gün
print("200 gün sonra: {} yılının {}. ayın {}. günü".format(gelecek.year, gelecek.month, gelecek.day))