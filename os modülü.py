import os

os.chdir("C:\\Users\\Mehmet KAHRAMAN\\Desktop")    #şu dizine git... (masaüstünde deneme.txt olmalı)
os.startfile("deneme.txt")    #çalıştır...

print("----------------------------------------------------------------")

mevcut_dizin = os.getcwd()
print(mevcut_dizin)
listemiz = os.listdir(mevcut_dizin)   #mevcut dizindeki tüm dosyaları listeler
print("Dosyalar: --------------------------------------")

for i in listemiz:
    print(i)
    if i.endswith(".py"):
        print("python dosyası bulundu")  #dosya formatı arama

print("----------------------------------------------------------------")

os.mkdir("yeni klasör")    #masaüstünde yeni klasör oluştu
os.makedirs("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\new folder\\örnek_1\\1a")  #birden fazla dizin klasörü açma...
os.rename("yeni klasör","yeni isim")
os.rmdir("yeni isim")

os.system("Calc.exe")   #dizine gitmeden çalıştır...

aranan_dizin = os.path.abspath('deneme.txt')      #aranan dosyanın hangi dizinde olduğunu gösterir
print("deneme dosyası şu dizinde:", aranan_dizin)

print("----------------------------------------------------------------")

if os.path.exists("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\abc") == False:   #dosya sorgulama işi yapar...
    print("abc diye bir dosya masaüstünde bulunmuyor.")