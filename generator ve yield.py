# iterasyon;
liste = [1,2,3]
for i in liste:
    print(i)

# iterasyonlarda liste içindeki tüm veriler hafızada saklanır
# resim gibi fazla verilerin olduğu listeler bilgisayarı ağırlaştırabilir

# generator;
generator = (x for x in range(1,4))
for i in generator:
    print(i)

# generasyonlarda veriler bellekte saklanmaz
# çağrıldıktan sonra verileri üretir

def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i

# iterasyondaki return == generasyondaki yield

generator = createGenerator()
print(generator)