import zipfile
import os

zip_adi = input("Açmak istediğin zip dosyasının adını gir (örn: deneme.zip): ")

if os.path.exists(zip_adi):
    with zipfile.ZipFile(zip_adi, 'r') as zip_ref:
        hedef_klasor = zip_adi.replace('.zip', '_acildi')
        os.makedirs(hedef_klasor, exist_ok=True)
        zip_ref.extractall(hedef_klasor)
        print(f"Zip başarıyla açıldı → {hedef_klasor}/")
else:
    print("Zip dosyası bulunamadı.")
