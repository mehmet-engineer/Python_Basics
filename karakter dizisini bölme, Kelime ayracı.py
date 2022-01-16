cumle = input("\n Cumlenizi girin: ")
cumle = cumle + " "
print("\n", end="")

i_sıra = -1          #(cumle[a:b] karakter dizisinin parça halini alır)
k_sayacı = 1         #(ancak a dahilken, b dahil olanın bi sonrakini temsil eder)
count = 0            #(cumle[ilk_k:son_k:atlama_sayısı] ise harfleri seçerek alır.)

for i in cumle:       

    i_sıra = i_sıra + 1
    
    if i == " ":
        print(" {}. kelime: {}".format(k_sayacı, cumle[count:i_sıra]))
        k_sayacı = k_sayacı + 1
        count = i_sıra + 1


