def not_durumu(n):
    if n in range(0, 50):
        return 'F'
    if n in range(50, 70):
        return 'D'
    if n in range(70, 80):
        return 'C'
    if n in range(80, 90):
        return 'B'
    if n in range(90, 101):
        return 'A'

sayı = int(input("Harf notu için sınav sonucunu girin: "))
print(sayı, "-->", not_durumu(sayı))
