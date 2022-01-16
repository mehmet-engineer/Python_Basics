import time

""" 
time() ve sleep() fonksiyonları işimize yarar.
time() metodu mutlak sıfır olarak kabul edilen geçmiş zamandan (örn 1970 yılının başı)
bu fonksiyonu yazdığımız zamana kadar saniye bazında ölçer. Şöyle kullanabiliriz;    
"""
veri1 = time.time()
time.sleep(3)           #3 saniye
veri2 = time.time()

geçen_zaman = veri2 - veri1
print("beklenen zaman:", geçen_zaman)


