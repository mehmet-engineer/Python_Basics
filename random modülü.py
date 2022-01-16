import random

sayı = random.randint(0, 10)  #0 ile 10 arası (0 ve 10 dahil) rastgele bir sayı üret.
print("Random ->", sayı)

liste = ["mehmet", "ahmet", "ibrahim", "zeynel", "sinan"]
kura = random.sample(liste,1)   #listeden 1 tane numune kurası seç
print("Kura sonucu ->", kura)

def sayı_üret(başlangıç=0, bitiş=500, adet=6):
    sayılar = set() #küme oluştur
    while len(sayılar) < adet:
        kura = random.randint(başlangıç,bitiş)
        sayılar.add(kura)
    return sayılar

print(sayı_üret())
