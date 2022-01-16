sayı = 25
binary = bin(sayı)[2:]
bellek_bit = sayı.bit_length()

metin = "\n {} sayısı, ikili sistemde {} sayısına tekabül edip\n bellekte {} bit yer kaplamaktadır."
print(metin.format(sayı,binary,bellek_bit))
