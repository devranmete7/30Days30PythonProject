gecmis_sonuclar = []  # Tüm sonuçları saklayacak liste

while True:
    secim = input("\nİşlemi seçiniz (1: Topla, 2: Çıkar, 3: Çarp, 4: Böl, çıkış: Programı bitir): ")
    
    if secim.lower() == "çıkış":
        print("\nProgramdan çıkılıyor...")
        break

    if secim not in ["1", "2", "3", "4"]:
        print("Hata: Geçersiz seçim! Lütfen 1-4 arasında bir seçim yapın.")
        continue

    # Sayı girişleri
    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))
    except ValueError:
        print("Hata: Geçerli bir sayı girilmedi.")
        continue

    # İşlem yapılır
    if secim == "1":
        sonuc = sayi1 + sayi2
    elif secim == "2":
        sonuc = sayi1 - sayi2
    elif secim == "3":
        sonuc = sayi1 * sayi2
    elif secim == "4":
        if sayi2 == 0:
            print("Hata: Sıfıra bölme hatası!")
            continue
        sonuc = sayi1 / sayi2

    # Sonucu yazdır
    print("Sonuç:", sonuc)

    # Negatif uyarı
    if sonuc < 0:
        print("Uyarı: Negatif sonuç oluştu!")

    # Sınıflandırma
    if 0 <= sonuc < 30:
        print("Sınıf: Düşük")
    elif 30 <= sonuc <= 70:
        print("Sınıf: Orta")
    elif sonuc > 70:
        print("Sınıf: Yüksek")

    # Sonucu listeye ekle
    gecmis_sonuclar.append(sonuc)

    # Tüm geçmiş işlemleri yazdır
    print("Geçmiş Sonuçlar:", gecmis_sonuclar)
