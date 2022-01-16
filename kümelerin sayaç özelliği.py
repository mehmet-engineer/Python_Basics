liste = ["elma", "armut", "elma", "elma", "armut", "çilek"]
liste_kümesi = set(liste)

for i in liste_kümesi:
    print("{} meyvesi {} kere geçiyor.".format(i,liste.count(i)))

#kümelerde aynı eleman 1 den fazla bulunmaz!
