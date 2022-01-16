d1 = open("C:/Users/Mehmet KAHRAMAN/Desktop/d_1.txt", "w")
print(" - Mehmet\n - Ahmet\n - Sinan", file=d1)

d1 = open("C:/Users/Mehmet KAHRAMAN/Desktop/d_1.txt", "r")
ram_1 = d1.readlines()      #tüm satırları okuyup listeler.
                                 
d1 = open("C:/Users/Mehmet KAHRAMAN/Desktop/d_1.txt", "r")
ram_2 = d1.readline()    #sadece ilk satırı karakter dizisi tipinde okur

d2 = open("C:/Users/Mehmet KAHRAMAN/Desktop/d_2.txt", "w")
d2.writelines(ram_1)     #listeyi karakter dizisi biçiminde yazdırır

d1.close()
d2.close()

print(" readlines() ile alınan veri -->", ram_1)
print("\n readline() ile alınan veri...\n ", ram_2)
