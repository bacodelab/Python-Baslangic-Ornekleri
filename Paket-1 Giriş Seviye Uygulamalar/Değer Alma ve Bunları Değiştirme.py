"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

"""

a = int(input("Birinci Sayısı Girin:"))
b = int(input("İkinci Sayıyı Girin:"))

sayılar = [a,b]

print("Birinci Sayı: {}\nİkinci Sayı: {}\n".format(sayılar[0],sayılar[1]))

print("Değişiklikler yapılıyor..")

sayılar = [b,a]

print("Birinci Sayı: {}\nİkinci Sayı: {}\n".format(sayılar[0],sayılar[1]))
