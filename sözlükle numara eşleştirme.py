alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
sözlük = {}

for sayı,harf in enumerate(alfabe):
    sözlük[harf] = sayı

print(sözlük)

def sırala_fonk(*kelimeler):
    liste = [i for i in kelimeler]
    print(liste)

sırala_fonk("ahmet","mehmet","ibrahim")
