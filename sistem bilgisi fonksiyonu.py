def sistem_info():
    import sys
    print("\nSistemde kurulu Python;")
    print(" - Ana sürüm numarası:", sys.version_info.major)
    print(" - Alt sürüm numarası:", sys.version_info.minor)
    print(" - Minik sürüm numarası:", sys.version_info.micro)
    print("\nKullanılan işletim sisteminin;")
    print(" - Adı:", sys.platform)

sistem_info()
