# Sayı  Tahmin Oyunu
# Kullanıcıdan 1-100 arasında bir sayı tahmin etmesini isteyin.


import random 


sayi = random.randint(1, 100)
tahmin= 0

while  tahmin  != sayi:
    tahmin =  int(input("1-100 arasında bir sayı tahmin edin: "))
    if  tahmin <sayi:
        print("Daha büyük bir sayı tahmin edin.")
    elif tahmin > sayi:
        print ("Daha küçük bir sayı tahmin edin.")
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break        



