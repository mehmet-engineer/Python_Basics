cumle = "ahmet abi"

cumle_1 = cumle.replace("a","A")
print(cumle_1)   #Ahmet Abi

cumle_2 = cumle.replace("ahmet", "mehmet")
print(cumle_2)   #Kelime değişimi

cumle_3 = cumle.replace(" ","")
print(cumle_3)   #Boşluk karakterlerini sil

cumle = "memleket"
cumle_4 = cumle.replace("e","",2)
print(cumle_4)    #(baştan 2.ye kadar olan e karakterleri)

print("-----------------------------------------------------")

cumle = "İstanbul Büyükşehir Belediyesi"
cumle_5 = cumle.split()  #cümleyi kelimelerine ayırarak listele
print(cumle_5)           #listeyi yazdır

print("\n Kısaltma: ", end="")

for kelime in cumle_5:        #cumle_5'deki her kelime elemanının ilk harfi için...
    print(kelime[0], end="")

yeni_str = " ".join(cumle_5)  #listedeki elemanları " " karakteriyle birleştir
print("\n ", yeni_str)
