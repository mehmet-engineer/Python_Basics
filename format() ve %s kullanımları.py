k_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız : ")
u1 = len(k_adı)
u2 = len(parola)

print("Kullanıcı adı {} karakterden oluşuyor.".format(u1))
print("parola toplam %s karakterden oluşuyor." %(u2))

#format() ve %() fonksiyonları...

print("-------------------------------------------------------")

yazı = " - %(kitap)s 1 \n - %(kitap)s 2 \n - %(kitap)s 3"
print(yazı % {"kitap": "Python Programlama Kitabı"})

#(eğer aynı şeyi yazmak zorundaysan hayat kurtaran kullanım)

print("-------------------------------------------------------")

print(" {0} takımı {1}'yi yendi. {1} çok üzüldü.".format("FB","GS"))
#format kelime seçimi çok kullanışlıdır
