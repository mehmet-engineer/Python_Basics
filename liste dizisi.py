toplam = 0
not_list = []    #boş bir liste dizisi oluştur

for i in range(10):
    veri = int(input("{}. not: ".format(i+1)))
    toplam = toplam + veri
    not_list = not_list + [veri]

print("\n Girilen notlar:")
print(*not_list, sep=" - ")
print(" Not ortalamanız: ", toplam/10)
