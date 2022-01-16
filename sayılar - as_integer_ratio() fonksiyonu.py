sayı = 4.5
a = sayı.as_integer_ratio()  #4.5 = 9/2 
print(a)                     #9 ve 2 sayılarını demet şeklinde verir
print(type(a))

for i in a:
    print(i)
