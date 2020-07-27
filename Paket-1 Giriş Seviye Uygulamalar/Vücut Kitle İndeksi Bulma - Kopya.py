"""

Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

"""

print("Vücut Kitle İndeksi Bulucu ")

kilo = int(input("Kilonuzu Giriniz:"))
boy = int(input("Boyunuzu Giriniz:"))

print("Vücut Kitle İndeksi: {}".format(kilo/boy))