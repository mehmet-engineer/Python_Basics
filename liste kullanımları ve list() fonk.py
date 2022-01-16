liste = ["mehmet", "ahmet", "sinan"]
print(" Liste verisinin türü:", type(liste))

print("-----------------------------------------------")

liste_2 = ["mehmet", 2, ["a", "b"], 3.14]

for eleman in liste_2:
    print(eleman, "->...", type(eleman))

print("-----------------------------------------------")

cumle = "fb gs bjk"       #cumleyi kelimelerine listele ve ilk elemanı yazdır
liste = cumle.split()
print("listenin ilk elemanı:", liste[0])

eleman_sayı = len(liste)   #len() fonksiyonu burada eleman sayısını ölçüyor
print("listenin eleman sayısı:", eleman_sayı)

print("\nLiST() Fonksiyonu ---------------------------")

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
a_liste = list(alfabe)      
                         #list() fonksiyonu ile her bir karakteri eleman yapma
print(a_liste)   

print("-----------------------------------------------")

listem = ["0", "20", "35"]
listem[0] = "10"              #listenin ilk elemanını değiştir
del listem[2]                 #listenin 2.elemanını sil
listem = listem + ["30"]      #listenin sonuna eleman ekle

print(listem)
