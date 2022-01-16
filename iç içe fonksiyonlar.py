def azalt_fonk(kelime):
    length = len(kelime)
    if length == 1:
        print(kelime)
    else:
        print(kelime)
        length = length-1
        a = kelime[:length]
        return azalt_fonk(a)
    

azalt_fonk("mehmet")
