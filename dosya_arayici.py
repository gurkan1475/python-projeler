import os

def dosya_arama(kok_klasor, hedef_dosya):
    for klasor_yolu, alt_klasorler, dosyalar in os.walk(kok_klasor):
        if hedef_dosya in dosyalar:
            return os.path.join(klasor_yolu, hedef_dosya)
    return None

kok = "C:\\Users\\kullanici_adi\\Masaüstü"  # kendi yoluna göre değiştir
aranacak = input("Aramak istediğiniz dosyanın adını girin (örn: not.txt): ")

sonuc = dosya_arama(kok, aranacak)
if sonuc:
    print(f"Dosya bulundu: {sonuc}")
else:
    print("Dosya bulunamadı.")
