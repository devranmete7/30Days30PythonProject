#✅ Ek Görev: 5 Kullanıcının Doğum Yılı ve En Yaşlıyı Bulma
import datetime

simdiki_yil = datetime.datetime.now().year

# 1. Kullanıcıdan doğum yılı al ve yaşa göre kategori ver
dogum_yili = int(input("Doğum yılınızı girin: "))

# 4. Geçerli yıl kontrolü
if dogum_yili < 1900 or dogum_yili > simdiki_yil:
    print("Geçersiz doğum yılı girdiniz!")
else:
    yas = simdiki_yil - dogum_yili

    # 1. Yaşa göre kategori
    if yas < 13:
        print("Kategori: Çocuk")
    elif yas <= 19:
        print("Kategori: Genç")
    elif yas <= 64:
        print("Kategori: Yetişkin")
    else:
        print("Kategori: Yaşlı")

    # 2. Hangi yılda 18 yaşına gireceğini hesapla
    onsekiz_yili = dogum_yili + 18
    print(f"18 yaşına gireceğiniz yıl: {onsekiz_yili}")

    # 3. Yaş bilgisini kullanıcıdan tekrar al ve kontrol et
    girilen_yas = int(input("Şu anki yaşınızı girin: "))
    hesaplanan_yil = simdiki_yil - girilen_yas

    if hesaplanan_yil == dogum_yili:
        print("Doğum yılınız doğru!")
    else:
        print(f"Doğum yılı tutarsız! Hesaplanan yıl: {hesaplanan_yil}")


#✅ Ek Görev: 5 Kullanıcının Doğum Yılı ve En Yaşlıyı Bulma


dogum_yillari = []
yaslar = []

for i in range(5):
    yil = int(input(f"{i+1}. kişinin doğum yılını girin: "))
    if yil < 1900 or yil > simdiki_yil:
        print("Geçersiz yıl! Atlınıyor...")
        continue
    dogum_yillari.append(yil)
    yaslar.append(simdiki_yil - yil)

# Herkesin yaşını yaz
for i in range(len(yaslar)):
    print(f"{i+1}. kişi: {yaslar[i]} yaşında")

# En yaşlıyı bul
en_yasli_index = yaslar.index(max(yaslar))
print(f"En yaşlı kişi: {en_yasli_index + 1}. kişi ({yaslar[en_yasli_index]} yaşında)")
