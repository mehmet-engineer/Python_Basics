#harfleri baytlara çevirme veya karakter kodlamada sıkıntı çıkarsa
#manuel olarak kodlayabiliriz

harfler = "abcç"

for i in harfler:

    if i == "ç":
        print(i, "| kodlanmış bayt hali ->", i.encode("cp1254"))
    else:
        print(i, "| kodlanmış bayt hali ->", i.encode("ascii"))
