import time
import datetime
print("3 Saniye sonra yazmaya başlayın, hazır olun.")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Go!")
time.sleep(0.2)
before = datetime.datetime.now()

text=input("Yazmaya başlayın:")
after = datetime.datetime.now()

speed = after - before
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text) / seconds,1)

print("Yazma süreniz : {} saniye.".format(seconds))
print("Her harfi {} saniyede yazdınız.".format(letter_per_second))