kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"

çevirme_motoru = str.maketrans(kaynak, hedef)   #çevirme işlemlerini hazır et
metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(çevirme_motoru))          #çevirme işlemini metin üzerine uygula
