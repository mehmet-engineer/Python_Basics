dosyam = open("C:/Users/Mehmet KAHRAMAN/Desktop/PDF_File.pdf", "rb")
okunan = dosyam.read()

#PDF dosyasının içeriği çok karışıktır, bu yüzden henüz hemen yazdıramıyoruz.

konum = okunan.index(b"/Producer")  #üreticinin ilk karakteri "/" nin konumunu öğreniyoruz (b...parametresine dikkat!!)
kod = okunan[konum]          #okunan verideki karakterin karakter tipinde değil binary kodu tipinde olduğunu biliyoruz
karakter = chr(kod)          #binary kodunu yani baytları chr() fonksiyonu ile karaktere çeviriyoruz. 

print("\n '/Producer' bilgisinin ilk karakteri {}. konumda bulunuyor.".format(konum))
print(" Bu dosyadaki aranan karakterin kodu {} dir.".format(kod))
print(" Bu kod karakter olarak '{}' işaretine tekabül eder.".format(karakter))
