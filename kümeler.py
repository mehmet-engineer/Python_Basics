küme = {"python", "C", "JavaScript"}
print(type(küme))         #----->  class 'set'

boş_küme = {}   #-----> !!! class 'dict'
boş_küme = set()    #böyle de olur...
boş_küme = set(boş_küme)
print(type(boş_küme))      #----->  class 'set'

#kümeler aynı elemandan en fazla 1 tane bulundurur ve ögeler rastgeledir.
metin = "Python Programlama Dili"
kümemiz = set(metin)
print(kümemiz)

#üzerinde değişiklik yapılmayan performans kümesi -> dondurulmuş küme
frozen_küme = frozenset(["elma", "armut", "ayva"])
