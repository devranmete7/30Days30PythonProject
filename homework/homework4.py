# 🎯 Ödevler:
# Kullanıcının kaç denemede doğru tahmin yaptığını yazdır.
# Tahmin doğruysa "Tebrikler", 3 kez yanlışsa “İpucu” ver (örn: Daha büyük).
# 5 deneme hakkı ver, deneme bitince “Kaybettin” yaz ve doğru sayıyı göster.
# Skor sistemi kur: Her doğru tahmin +10 puan, her yanlış tahmin -2 puan.
# Her oyunun sonunda kullanıcı isterse tekrar oynayabilsin (while ile).

import random
while True:
    sayi = random.randint(1, 100)
    deneme_sayisi = 0
    max_hak = 5
    skor = 0

    print("\n🟡 1 ile 100 arasında bir sayı tuttum. Tahmin etmeye çalış!")
    
    while deneme_sayisi < max_hak:
        tahmin = int(input(f"Tahmin ({deneme_sayisi+1}/{max_hak}): "))
        deneme_sayisi += 1

        if tahmin < sayi:
            print("Daha büyük bir sayı dene.")
        elif tahmin > sayi:
            print("Daha küçük bir sayı dene.")
        else:
            print(f"🎉 Tebrikler! {deneme_sayisi}. denemede doğru tahmin ettin.")
            skor += 10
            break

        # 3 yanlış denemede ipucu
        if deneme_sayisi == 3 and tahmin != sayi:
            if sayi % 2 == 0:
                print("🔎 İpucu: Sayı çift.")
            else:
                print("🔎 İpucu: Sayı tek.")

        # Her yanlış denemede -2 puan
        skor -= 2

    # Deneme hakkı bitti ama bilemedi
    if tahmin != sayi:
        print(f"❌ Kaybettin! Doğru sayı: {sayi}")

    print(f"🔢 Bu oyundaki skorun: {skor}")

    # Oyun sonu tekrar sor
    devam = input("\nTekrar oynamak ister misin? (evet/hayır): ").lower()
    if devam != "evet":
        print("👋 Oyun bitti. Hoşça kal!")
        break
