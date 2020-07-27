print("""
*************
Kullanıcı Giriş Sistemi
*************""")

sys_kullanici = "batuhan"
sys_parola = "123456"

kullaniciadi = input("Kullanıcı Adı:")
parola = input("Parola Giriniz:")

if (kullaniciadi == sys_kullanici and parola == sys_parola):
    print("Bilgiler doğru, giriş başarılı.")
elif (kullaniciadi != sys_kullanici and parola == sys_parola):
    print("Kullanıcı adı hatalı, tekrar deneyin.")
elif (kullaniciadi == sys_kullanici and parola != sys_parola):
    print("Parola hatalı, tekrar deneyin.")
else:
    print("Kullanıcı adı ve Parola hatalı, tekrar deneyin.")