import os
from datetime import datetime

# Kullanıcıdan taranacak klasör yolunu al
klasor_yolu = input("Taranacak klasör yolunu girin: ")

# Rapor dosya adı
rapor_adi = f"rapor_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Dosya ve klasörleri listele
with open(rapor_adi, "w", encoding="utf-8") as rapor:
    rapor.write(f"{klasor_yolu} dizin raporu\n")
    rapor.write("-" * 40 + "\n\n")

    for kok, klasorler, dosyalar in os.walk(klasor_yolu):
        rapor.write(f"Klasör: {kok}\n")
        for k in klasorler:
            rapor.write(f"   [Klasör] {k}\n")
        for d in dosyalar:
            rapor.write(f"   [Dosya] {d}\n")
        rapor.write("\n")

print(f"Rapor oluşturuldu: {rapor_adi}")
