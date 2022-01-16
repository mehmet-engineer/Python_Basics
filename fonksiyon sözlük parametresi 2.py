def dictionary_fonk(*aranacaklar, **sözlük):  #bu kullanım * ile sınırsız,
    for kelime in aranacaklar:                  # ** ile sabit parametre oluşturabilmekte
        if kelime in sözlük:
            print("{} = {}".format(kelime, sözlük[kelime]))
        else:
            print("{} kelimesi sözlükte yok!".format(kelime))

sözlük = {"kitap" : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

dictionary_fonk("kitap", "bilgisayar", "programlama", "ab", **sözlük)
