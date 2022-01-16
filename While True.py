while True:  #quit() gibi bişeyle aksi belirtilmediği sürece...

    veri = input(" 1 ile 10 arası bir sayı girin: ")
    a = int(veri)

    if a in range(0,11):
        print("\n Tebrikler, işlem tamamlandı...")
        quit()

    else:
        print(" Geçersiz sayı tekrar girin\n")
        
