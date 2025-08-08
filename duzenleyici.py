import os
import shutil

def klasor_duzenle():
    # Masaüstü yolunu otomatik bul
    masaustu_yolu = os.path.join(os.path.expanduser("~"), "Desktop", "Duzenlenecek")

    # Eğer klasör yoksa oluştur
    if not os.path.exists(masaustu_yolu):
        os.makedirs(masaustu_yolu)
        print(f"'{masaustu_yolu}' klasörü oluşturuldu. Dosyalarınızı buraya ekleyin ve tekrar çalıştırın.")
        return

    # Uzantılara göre klasörler
    uzanti_klasorleri = {
        ".txt": "Metin Dosyaları",
        ".jpg": "Resimler",
        ".jpeg": "Resimler",
        ".png": "Resimler",
        ".pdf": "PDF Dosyaları",
        ".mp3": "Müzikler",
        ".mp4": "Videolar",
        ".zip": "Arşivler"
    }

    # Her dosyayı uzantısına göre taşı
    for dosya in os.listdir(masaustu_yolu):
        dosya_yolu = os.path.join(masaustu_yolu, dosya)
        if os.path.isfile(dosya_yolu):
            uzanti = os.path.splitext(dosya)[1].lower()
            if uzanti in uzanti_klasorleri:
                hedef_klasor = os.path.join(masaustu_yolu, uzanti_klasorleri[uzanti])
                os.makedirs(hedef_klasor, exist_ok=True)
                shutil.move(dosya_yolu, os.path.join(hedef_klasor, dosya))
                print(f"{dosya} → {uzanti_klasorleri[uzanti]} klasörüne taşındı.")

    print("📂 Klasör düzenleme tamamlandı!")

# Çalıştır
klasor_duzenle()
