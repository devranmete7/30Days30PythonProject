while True:
    ad = input("Adınızı girin (çıkmak için 'exit' yazın): ").strip()
    if ad.lower() == "exit":
        print("Programdan çıkılıyor...")
        break

    soyad = input("Soyadınızı girin: ").strip()

    # 1. Ad ve soyad ters çevrilmiş hali
    ters_ad = ad[::-1]
    ters_soyad = soyad[::-1]
    print(f"Ters çevrilmiş: {ters_ad} {ters_soyad}")

    # 2. Ad uzunluğu kontrolü
    if len(ad) > 5:
        print("Güzel bir isimmiş!")

    # 3. "a" harfi sayısı
    a_sayisi = ad.lower().count("a")
    print(f"Adınızda {a_sayisi} tane 'a' harfi var.")

    # 4. Baş harflerle kısa ad
    kisa_ad = f"{ad[0].upper()}.{soyad[0].upper()}."
    print(f"Kısa isim: {kisa_ad}")

    print("-" * 30)  # Ayraç çizgisi
