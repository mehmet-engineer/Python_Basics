#lambda ileri düzey fonksiyonu...

#fonk_ismi = parametreler : döndürülecek işlem
fonksiyon_1 = lambda x: x*x + 3*x +5
fonksiyon_2 = lambda cümle, ara: ara.join(cümle.split())

print(fonksiyon_1(2))
print(fonksiyon_2("mehmet kahraman", "-"))
