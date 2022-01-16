dosyam = open("C:/Users/Mehmet KAHRAMAN/Desktop/deneme.txt", "w")
#dosyayı oluştur

dosyam.write("Mehmet KAHRAMAN")
#dosyaya yazı yaz

print("\n\n - bir_tevhidi.muhendis", file=dosyam)
#dosyaya yazı ekle

dosyam = open("C:/Users/Mehmet KAHRAMAN/Desktop/deneme.txt", "r") 
ram = dosyam.read()                                         #"r" dosyası
#dosyayı oku

dosyam.close()
print("Dosya içeriği:\n", ram)

