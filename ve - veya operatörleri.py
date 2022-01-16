sayı = input("\n Geçerli bir sayı için 1 ile 10 arası bir sayı girin: ")
sayı = int(sayı)

if sayı <= 10 and sayı >= 1:    # if sayı in range(0,11)
    print(" Girilen sayı geçerli...")
else:
    print(" Girilen sayı geçersiz...")

sayı_2 = input(" \n Şimdi sizden 1 veya 0 rakamlarını tuşlamanızı istiyoruz: ")
sayı_2 = int(sayı_2)

if sayı_2 == 1 or sayı_2 == 0:
    print(" İşlem başarılı...")
else:
    print(" İşlem başarısız...")
    
