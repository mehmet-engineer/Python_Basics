def f(x):
    print(" Fonksiyon tanımı -> f(x)= x^2+3x-1")
    sonuç = x**2 + 3*x -1
    return sonuç

girdi = int(input(" Lütfen bir x değeri girin: "))
çıktı = f(girdi)   #return ile fonksiyonu değişkenlerle de kullanabiliriz

print("\nİŞLEM SONUCU: -------------------------------------------")
print("f({}) = {}".format(girdi, çıktı))
