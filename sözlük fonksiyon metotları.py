sözlük = {"a": 1, "b": 2, "c": 3}

anahtarlar = list(sözlük.keys())
değerler = list(sözlük.values())

print(anahtarlar, "|", değerler)

print("-----------------------------------------------------------")

stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}
yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}

stok.update(yeni_stok)
print(stok)
