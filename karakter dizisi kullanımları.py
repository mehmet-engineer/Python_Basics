cumle = "mehmet kahraman"

print(cumle[0])        #(karakter dizisinin ilk karakteri)
print(cumle[0:6])      #(0 ile 5 arası karakterler. "5 dahil")
print(cumle[0:6:2])    #(ikili atlamak şartıyla 0 ile 5 arası karakterler)
print(cumle[7:])       #(7. ve sonrası karakterler)
print(cumle[:7])       #(7'ye kadarki karakterler)

#(kelimelerin ilk harfini büyütmek istiyorsak)
yeni_cumle = "M" + cumle[1:7] + "K" + cumle[8:]
print(yeni_cumle)
