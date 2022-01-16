küme = set(["elma", "armut", "kebap"])
küme.add("çilek")
print(küme)    #--> {'elma', 'armut', 'kebap', 'çilek'}

k1 = set([1, 2, 3, 5])
k2 = set([2, 3, 10])

kesişim = k1.intersection(k2)  #intersection() yerine '&'(ve) de kullanılabiliyor
fark1 = k1.difference(k2)  #k2 de olmayıp k1 de olan
fark2 = k2.difference(k1)  #k1 de olmayıp k2 de olan
özler = k1.symmetric_difference(k2)  #A-B ve B-A | yani kesişim hariç...

hayvanlar = set(["kedi", "köpek", "at", "insan"])
hayvanlar.discard("insan")   #"insan"ı çıkar

a = set([2, 4, 6, 8])
b = set([1, 3, 5, 7])
a.union(b)   #birleştir... #union() yerine "|" de kullanılabiliyor
