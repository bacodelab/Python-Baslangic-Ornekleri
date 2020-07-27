"""
İf-Elif-Else Komutları Kullanımı

Basit bir hesap makinesi

"""

print("Basit Hesap Makinesi")

sayi1 = int(input("1. Değeri Giriniz:"))
sayi2 = int(input("2. Değeri Giriniz:"))
islem = int(input("İşlem Seçiniz/Toplama(1),Çıkarma(2),Çarpma(3),Bölme(4):"))

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
