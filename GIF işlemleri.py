dosya = open("C:/Users/Mehmet KAHRAMAN/Desktop/a.gif", "wb")

dosya = open("C:/Users/Mehmet KAHRAMAN/Desktop/a.gif", "rb")
ram = dosya.read(10)

print(ram)

if ram[:3] == b'GIF':
    print("\n Bu dosya türünün GIF olduğu kanıtlanmıştır.")
else:
    print("\n Bu dosya GIF türünde değildir.")
