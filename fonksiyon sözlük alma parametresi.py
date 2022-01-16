def kayıt_oluştur(**bilgiler):  #bu kullanım sınırsız parametreyi sözlükleştirir
    print("-"*30)
    for anahtar, değer in bilgiler.items():
        print("{:<10}: {}".format(anahtar, değer))
    print("-"*30)

kayıt_oluştur(Adı="Mehmet", Soyadı="Kahraman", Meslek="Mühendis", tel="0123456789")

#{:<10} ifadesi kelimeyi yaz ve 10 karakterlik alanı boşlukla doldur
