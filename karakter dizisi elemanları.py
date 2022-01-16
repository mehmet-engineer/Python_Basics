isim = "mehmet kahraman"
a = 0

print("\n mehmet kahraman adlı karakter dizisinin:", end="\n\n ")

while a < len(isim):
    print("{}. terimi:".format(a+1), isim[a], end="\n ")
    a = a+1
