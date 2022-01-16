import os
os.getcwd()  #açılan dosyanın konumunu gösterir
os.name      #çalıştırılan işletim sistemini söyler ("nt" ise windows)

import sys
sys.version

import subprocess as çalıştır  #bundan sonra bu modülün adı çalıştır :)
çalıştır.call("calc.exe")

import webbrowser as web
web.open("www.subu.edu.tr")

from os import getcwd,rename    #bu kullanım modülden yalnızca belirtilen
getcwd()                        #..fonksiyonlarını kullanıma hazırlar


