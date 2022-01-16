#bytes() fonksiyonu yazılan karakteri baytlara çevirir.

print(bytes("abcçdef", "cp857"))
print(bytes("abcçdef", "utf-8"))
print(bytes("abcçdef", "ascii", errors="replace"))
