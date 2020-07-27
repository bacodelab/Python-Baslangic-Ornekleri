"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

"""

km = int(input("Aracın Kilometrede Yaktığı Tutar:"))
yol = int(input("Gittiğiniz Yol:"))

print("Toplam Ücret : {} TL".format(km*yol))