cumle = "bir tevhidi muhendis"
a = len(cumle)
sayı_ram = cumle.count("i",0,a)  #(0. karakterden sonuna kadar i harfini say)

print(" '{}' cumlesinde i harfi {} kez geçiyor.".format(cumle,sayı_ram))

print("------------------------------------------------------------")

cumle = "bir tevhidi muhendis"
konum = cumle.index("i",11,a)    #(11-a karakterleri arası i'nin konumu)

print(""" Bu cümlede 11. ve {}. karakterler arası 'i' harfi
 soldan {} konumunda bulunuyor.""".format(a,konum))
