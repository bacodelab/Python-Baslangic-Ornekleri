"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""

vize1 = int(input("Vize 1 Notunuzu Giriniz:"))
vize2 = int(input("Vize 2 Notunuzu Giriniz:"))
final = int(input("Final Notunuzu Giriniz:"))

vize1not = vize1 * 0.30
vize2not = vize2 * 0.30
finalnot = final * 0.40

if (vize1not+vize2not+finalnot >= 90):
    print("Harf Notunuz: AA")
elif (vize1not+vize2not+finalnot >= 85):
    print("Harf Notunuz: BA")

"""
Şeklinde devam edip türetebilirsiniz.
"""
