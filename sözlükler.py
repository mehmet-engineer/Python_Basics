#sözlük[key] = value

sözlük = {}
print(type(sözlük))  #sözlük veri tipi --> class 'dict'

sözlük["one"] = "bir"  #eleman ekleme...
print(sözlük)          #NOT: elemanlar rastgele sırayle eklenir

sözlük["one"] = "1"    #eleman değiştirme...

ing_sözlük = {"kitap": "book", "kalem": "pen", "kağıt": "paper"}

sözlük = {"kitap" : "book",
"bilgisayar" : "computer",
"programlama": "programming",
"dil" : "language",
"defter" : "notebook"}  #daha rahat görünüm...

print("\n (TR) Dil --> (İNG)", sözlük["dil"])

for i in sözlük:
    print(" "*2, i.center(10), " ", sözlük[i].center(15))

print("-----------------------------------------------------------------")

bio_sözlük = {"Mehmet KAHRAMAN": ["İstanbul", "Mekatronikçi", 34],
    "Sinan BAVLİ" : ["Ağrı", "Yazılımcı", 34],
    "Ahmet POLAT" : ["İzmir", "Bilgisayarcı", 35]}

print("\n Bio sözlükten -->", bio_sözlük["Mehmet KAHRAMAN"])

#sözlük içinde sözlük elemanı...
kişiler_info = {"Mehmet": {"Memleket": "İstanbul",
                            "Meslek" : "Mühendis",
                            "Yaş" : 20},

                "Ahmet":  {"Memleket": "Adana",
                           "Meslek" : "Mühendis",
                           "Yaş" : 40},

                "İbrahim" : {"Memleket": "İskenderun",
                             "Meslek" : "Doktor",
                             "Yaş" : 30}}

print(" Kişi -> Meslek --> ", end="")
print(kişiler_info["Mehmet"]["Memleket"])
