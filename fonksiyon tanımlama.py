#(define a function)

def menu_fonk(isim, soy, dep):
    print("-"*25)
    print("isim/ad  :", isim)
    print("soyisim  :", soy)
    print("Departman:", dep)

isim = input(" Lütfen isim girin: ")
soy = input(" Lütfen soyadı girin: ")
dep = input(" Lütfen departman girin: ")

print("\n Kayıt başarıyla oluşturuldu...")
print()

menu_fonk(isim,soy,dep)
