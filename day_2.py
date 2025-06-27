sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))


print("İşlemi seçiniz:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi giriniz (1/2/3/4): ")


if secim == "1":
    print("Sonuç:", sayi1 + sayi2)
elif secim == "2":
    print("Sonuç:", sayi1 - sayi2)
elif secim == "3":
    print("Sonuç:", sayi1 * sayi2)
elif secim == "4":
    if sayi2 !=0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Hata: Sıfıra bölme hatası!")
else:
    print("Hata: Geçersiz seçim!")            



#!  Cevabı yorumlarda belirtiniz.
#?  if  ile  else arasındaki  farklılık  nedir?