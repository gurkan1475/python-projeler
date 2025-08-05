import shutil
import os

klasor_adi = input("Zip'e çevirmek istediğin klasörün adını yaz: ")

if os.path.exists(klasor_adi):
    shutil.make_archive(klasor_adi, 'zip', klasor_adi)
    print(f"{klasor_adi}.zip başarıyla oluşturuldu.")
else:
    print("Böyle bir klasör bulunamadı.")
