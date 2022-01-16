import os

dizinim = "C:\\Users\\Mehmet KAHRAMAN\\Desktop\\University\\Programming Dilleri\\Algoritma Temelleri"
listemiz = os.listdir(dizinim)

for i in listemiz:
    if i.endswith(".pdf") == True:    #sadece pdf dosyalarını yazdırdık
        print(i)