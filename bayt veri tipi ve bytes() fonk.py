bayt = b''
print(type(bayt))

b = bytes("ş", "utf-8")
print(b)

c = bytes("yalın", "ascii", errors="replace")
print(c)

#bytes veri tipi üzerinde demetler gibi değişiklik yapılmaz
#bytearray veri tipi üzerinde değişiklik yapılabilir

veri = bytearray(b"")
print(type(veri))


