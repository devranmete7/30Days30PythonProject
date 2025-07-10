# 🎯 Ödevler:
# En uzun kelimeyi bulun.
# Metindeki sesli harfleri say.
# Aynı kelime birden fazla geçiyorsa kaç kez geçtiğini yaz.
# Tüm kelimeleri küçük harfe çevirip alfabetik sıraya diz.
# “Python” kelimesi geçtiyse özel mesaj yaz.   bana   bunu daha   düzenlibirşeklde ver  ekrangörüntüsnalıppylaşaçağım    
# çokkıas değier günlerde verdiğinaynısın  solsu 

#🎯 1) En uzun kelimeyi bulun
metin = input("Metin girin: ")
kelimeler = metin.split()

# En uzun kelimeyi bul
en_uzun = max(kelimeler, key=len)
print("En uzun kelime:", en_uzun)


#🎯 2) Metindeki sesli harfleri say
metin = input("Metin girin: ").lower()
sesliler = "aeıioöuü"

# Her harfi kontrol et, sesli ise say
adet = sum(1 for harf in metin if harf in sesliler)
print("Sesli harf sayısı:", adet)


#🎯 3) Aynı kelime birden fazla geçtiyse kaç kez geçtiğini yaz
metin = input("Metin girin: ").lower()
kelimeler = metin.split()
kelime_sayilari = {}

# Her kelimeyi say
for kelime in kelimeler:
    kelime_sayilari[kelime] = kelime_sayilari.get(kelime, 0) + 1

# 2’den fazla geçenleri yazdır
for k, v in kelime_sayilari.items():
    if v > 1:
        print(f"{k} kelimesi {v} kez geçti.")



#🎯 4) Tüm kelimeleri küçük harfe çevirip alfabetik sıraya diz
metin = input("Metin girin: ")
kelimeler = metin.lower().split()

# Alfabetik sırala
kelimeler.sort()
print("Alfabetik sırayla kelimeler:", kelimeler)



# 🎯 5) “Python” kelimesi geçtiyse özel mesaj yaz
metin = input("Metin girin: ").lower()

# "python" geçiyorsa mesaj ver
if "python" in metin:
    print("🐍 Python harika bir dil!")
else:
    print("Python kelimesi geçmiyor.")

