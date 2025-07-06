# ✅ 5. Gün: Çift - Tek Sayı Bulucu
# Temel Konu: Mod alma, mantıksal kontrol

# 🎯 Ödevler:
# Girilen sayının çift veya tekliğine ek olarak pozitif/negatif olup olmadığını yaz.

# 10 farklı sayı girilmesini iste, her birinin tek/çift sonuçlarını liste olarak döndür.

# Kullanıcı “liste” girdiğinde 1–100 arası tüm çift sayıları listele.

# Sayı 5’in katıysa özel bir mesaj ver: “Bu sayı hem tek/çift hem de 5'in katı.”

# 0 sayısı girilirse "Ne tek ne çift" yazıp programdan çık.



#? 🎯 1. Ödev: Sayının pozitif/negatif ve tek/çift olup olmadığını bul
sayi = int(input("Bir sayı girin: "))

if sayi == 0:
    print("Sayı 0: Ne tek ne çift.")
elif sayi % 2 == 0:
    print("Çift", end=", ")
else:
    print("Tek", end=", ")

if sayi > 0:
    print("pozitif.")
elif sayi < 0:
    print("negatif.")


#?🎯 2. Ödev: 10 farklı sayı gir, tek/çift listesini oluştur
sonuclar = []

for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    if sayi % 2 == 0:
        sonuclar.append("Çift")
    else:
        sonuclar.append("Tek")

print("Sonuçlar:", sonuclar)


#?🎯 3. Ödev: Kullanıcı "liste" yazarsa 1–100 arası çift sayıları göster
komut = input('Bir komut girin ("liste" yaz çift sayıları gör): ')

if komut.lower() == "liste":
    ciftler = [s for s in range(1, 101) if s % 2 == 0]
    print("1–100 Arası Çift Sayılar:", ciftler)
    

#?🎯 4. Ödev: Sayı 5’in katıysa özel mesaj y
sayi = int(input("Bir sayı girin: "))

if sayi % 5 == 0:
    if sayi % 2 == 0:
        print("Bu sayı çift ve aynı zamanda 5'in katı.")
    else:
        print("Bu sayı tek ve aynı zamanda 5'in katı.")
else:
    print("Sayı 5’in katı değil.")
   
#?🎯 5. Ödev: 0 girilirse mesaj ver ve programdan çık

sayi = int(input("Bir sayı girin: "))

if sayi == 0:
    print("Ne tek ne çift. Programdan çıkılıyor.")
else:
    print("İşlem devam ediyor...")
