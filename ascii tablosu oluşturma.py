alfabe = "abcdefghijklmnoprstuvyz"

print("\n ASCII Tablosu...")
print("\n Onluk Temsili | Binary Kodu | Karakter")

for i in range(128):
    print(" "*6, i, " "*13, bin(i)[2:], " "*10, repr(chr(i)), sep="")

#repr() fonksiyonu "represent in python" anlamındadır.
#Örn: "\n" karakterini yazdırdığımızda çıktıda göremeyiz

print("----------------------------------------------------------------")

print(" ASCII latin alfabe karakterleri...\n")
print(" Karakter | Onluk Kodu | İkili Kodu")

for i in alfabe:
    print(" "*4, i, " "*11, ord(i), " "*9, bin(ord(i))[2:], sep="")
