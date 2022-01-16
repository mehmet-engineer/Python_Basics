#onlu sistemdeki 12 sayısının ikili sistemdeki karşılığı
print(bin(12)[2:])

#onlu sistemdeki 12 sayısının sekizli sistemdeki karşılığı
print(oct(12)[2:])

#onlu sistemdeki 18 sayısının onaltılı sistemdeki karşılığı
print(hex(18)[2:])

print("-----------------------------------------------------")

#herhangi bir sistemdeki sayıyı onluk sisteme çevirme
#formul -> int("...", sistem)

sayı_2 = int("1100", 2)
sayı_8 = int("67", 8)
sayı_16 = int("7bc", 16)

print(" ikili sistemdeki 1100 sayısı == onluk sistemde", sayı_2)
print(" sekizli sistemdeki 67 sayısı == onluk sistemde", sayı_8)
print(" onaltılı sistemdeki 7bc sayısı == onluk sistemde", sayı_16)
