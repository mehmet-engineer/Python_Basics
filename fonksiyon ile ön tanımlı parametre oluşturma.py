def kare_olustur(boyut=4):  #öntanımlı 4 olarak ayarlandı
                                     #istenirse değiştirilebilecek
    print("-"*30)                      

    for i in range(0,boyut):
        for j in range(0,boyut):
            print("*", end="")
            
        print() #satırdan sonra alta geçsin
        
    print("-"*30)


print("Kare oluşturmak için boyut ayarlaması;")
print("-- Ön tanımlı kare için 1'i")
print("-- Özel tanımlı kare için 2'yi")
tuş = int(input("Tuşlayınız: "))

if tuş == 1:
    kare_olustur()  #ön tanımlı varsayılan 4x4

if tuş == 2:
    boyut = int(input(" Kenar Boyutu: "))
    kare_olustur(boyut)
