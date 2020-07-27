"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2

"""

a = int(input("Üçgenin Birinci Dik Kenarı:"))
b = int(input("Üçgenin İkinci Dik Kenarı:"))

c = (a ** 2 + b ** 2) ** 0.5


print("Hipotenüs uzunluğu: {}\n".format(c))

