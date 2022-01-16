ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

if sorgu not in ing_sözlük:  #yoksa...
    print("Bu kelime veritabanımızda yoktur!")
else:
    print(ing_sözlük[sorgu])
