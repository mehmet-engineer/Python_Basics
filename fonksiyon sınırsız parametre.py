def çarpma_fonk(*sayılar):
    çarpım = 1
    for i in sayılar:
        çarpım = çarpım * i
    print(" Girilen sayıların çarpımı --> {}".format(çarpım))

çarpma_fonk(2, 3, 5, 4)  #girilen sınırsız parametre
