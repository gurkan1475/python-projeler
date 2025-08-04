import os
import shutil

kaynak_klasor = "indirilenler"
uzanti_klasor_map = {
    ".jpg": "resimler",
    ".png": "resimler",
    ".pdf": "belgeler",
    ".docx": "belgeler",
    ".mp3": "muzikler",
    ".mp4": "videolar"
}

for dosya in os.listdir(kaynak_klasor):
    dosya_yolu = os.path.join(kaynak_klasor, dosya)
    if os.path.isfile(dosya_yolu):
        _, uzanti = os.path.splitext(dosya)
        hedef_klasor = uzanti_klasor_map.get(uzanti.lower())
        if hedef_klasor:
            hedef_yol = os.path.join(kaynak_klasor, hedef_klasor)
            os.makedirs(hedef_yol, exist_ok=True)
            shutil.move(dosya_yolu, os.path.join(hedef_yol, dosya))
            print(f"{dosya} → {hedef_klasor}/")
