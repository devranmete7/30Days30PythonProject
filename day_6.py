#✅ Yeni 6. Gün Projesi: Kelime Sayacı

#kullanıcıdan  bir  metin  girmesini  istiyoruz.
metin = input("Bir metin giriniz: ")

#Girilen   metin boşluklardan ayırarak  kelimleri  bölüyoruz
kelimeler = metin.split()

# Metindeki tüm boşlukları çıkarıp sadece harflerin uzunluğunu hesaplıyoruz
harf_sayisi = len (metin.replace(" ", ""))


# Kelime listesinin uzunluğunu (kaç kelime olduğunu) buluyoruz
kelime_sayisi = len(kelimeler)

# Sonuçları ekrana yazdırıyoruz
print(f"Kelime sayısı: {kelime_sayisi}")
print(f"Harf sayısı (boşluksuz): {harf_sayisi}")


#!Bu  sorunu cevplarını  yorumlarda paylaşabilirsiniz.
#? bu koda len ne için kullanılıyor?