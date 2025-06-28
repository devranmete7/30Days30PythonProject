#Çift-Tek Sayı Bulucu
#kullanıcınınn girdiği sayının çift mi tek mi olduğunu bulan program


# 1-Kullanıcıdan sayı al:
sayi =int(input("Bir sayı giriniz: "))

# 2-Çift mi diye kontrol et:
if sayi % 2 == 0:
    # 3-Çiftse ekrana yaz:
    print(f"{sayi} sayısı çifttir.")
    # 4-Aksi halde tektir:
else:
    print(f"{sayi} sayısı tektir.")

