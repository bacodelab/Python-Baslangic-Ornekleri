"""

Basit bir hesap makinesi

"""

print("""
*****
Basit Hesap Makinesi

Toplama İşlemi 1
Çıkarma İşlemi 2
Çarpma İşlemi 3
Bölme İşlemi 4

*****
""")

sayi1 = int(input("1. Değeri Giriniz:"))
sayi2 = int(input("2. Değeri Giriniz:"))
islem = int(input("İşlem Seçiniz:"))

if islem == 1:
    print("Sonuç:", sayi1+sayi2)
elif islem == 2:
    print("Sonuç", sayi1-sayi2)
elif islem == 3:
    print("Sonuç", sayi1*sayi2)
elif islem == 4:
    print("Sonuç", sayi1/sayi2)
else:
    print("Geçersiz İşlem Seçtiniz.")
