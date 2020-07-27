"""
Harf Notu Hesaplama Sistemi(İf-Elif-Else)

"""

print("Harf Notu Hesaplama Sistemi")

note = float(input("Notunuzu Giriniz:"))

if (note >= 90):
    print("Harf Notunuz:AA")
elif (note >= 70):
    print("Harf Notunuz:BB")
elif (note >= 50):
    print("Harf Notunuz:CC")
elif (note >= 30):
    print("Harf Notunuz:DD")
elif (note >= 0):
    print("Harf Notunuz:FF")
else:
    print("Geçersiz Not Girişi Yaptınız.")

