ön_tanımlı = [512, 25, 3, 100, 220]
büyük = max(ön_tanımlı)
küçük = min(ön_tanımlı)
print("\n ön tanımlı listedeki maximum sayı --> {}".format(büyük))
print(" ön tanımlı listedeki minimum sayı --> {}".format(küçük))

print("----------------------------------------------------------")

liste = []
print("\n Sizden 3 tane farklı uzunlukta isim girmenizi istiyoruz.")

for i in range(3):
    isim = input(" {}. isim: ".format(i+1))
    liste = liste + [isim]

en_uzun = max(liste, key=len)
length = len(en_uzun)

print("\n girilen en uzun isim {} karakterle {}'dir.".format(length, en_uzun))
