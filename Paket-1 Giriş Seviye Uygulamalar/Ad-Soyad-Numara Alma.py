"""

Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.


"""

ad = input("Adınızı Giriniz:")
soyad = input("Soyadınızı Giriniz:")
numara = int(input("Numaranızı Giriniz:"))

bilgiler = [ad,soyad,numara]

print("Adı: {}\nSoyadı: {}\nNumarası: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

