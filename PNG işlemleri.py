#masaüstünde a.png olması gerek

dosya = open("C:/Users/Mehmet KAHRAMAN/Desktop/a.png", "rb")
ram = dosya.read(8)

print(ram)     #binary verisi farklı sayı sisteminde kodlanmış olabilir

if ram[:8] == b"\211PNG\r\n\032\n":   #bu kod tüm sistemde geçerlidir.
    print("\n Bu dosya PNG olarak kanıtlanmıştır.")
else:
    print("\n Bu dosya PNG türünde değildir.")


