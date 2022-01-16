def üs_alma_fonk(taban, üs):
    işlem = taban ** üs
    çıktı = " {} üzeri {} =="
    print(çıktı.format(taban,üs), işlem)

i = input(" Taban sayısını girin: ")
i = int(i)

j = input(" Üs sayısını girin: ")
j = int(j)

üs_alma_fonk(i, j)
    
