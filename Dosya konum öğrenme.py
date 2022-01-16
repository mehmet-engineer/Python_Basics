dosya = open("deneme.txt", "w")

print("Mehmet_KAHRAMAN", file=dosya)
dosya.close()

import os
print("\n DOSYA KONUMU", "-"*20)
print(os.getcwd())
