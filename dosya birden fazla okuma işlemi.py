dosya = open("C:/Users/Mehmet KAHRAMAN/Desktop/dosyam.txt", "w")
metin = " - mehmet\n kahraman."
dosya.write(metin)

dosya = open("C:/Users/Mehmet KAHRAMAN/Desktop/dosyam.txt", "r")
ram = dosya.read()             #ilk okumayı gerçekleştirir
print(ram)                   

dosya.seek(0)                  #okuma imlecini başa alır 
ram_2 = dosya.read()           #dosyayı tekrar okur
print(ram_2)

dosya.close()
