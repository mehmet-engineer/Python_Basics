#masaüstünde "a.jpg" isimli bir resim olması lazım

dosya = open("C:/Users/Mehmet KAHRAMAN/Desktop/a.jpg", "rb")
data = dosya.read(10)   #dosyanın ilk 10 baytını oku

print(data)
print(" Okunan tür:", type(data))

if data[6:11] in [b"JFIF", b"Exif"]:
    print("\n Bu dosyanın JPG türünde olduğu kanıtlanmıştır")
else:
    print("\n Bu dosya JPG değildir.")
