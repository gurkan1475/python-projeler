import os
import shutil

kaynak_klasor = "notlar"
hedef_klasor = "yedek"

if not os.path.exists(hedef_klasor):
    os.mkdir(hedef_klasor)

for dosya in os.listdir(kaynak_klasor):
    if dosya.endswith(".txt"):
        tam_yol = os.path.join(kaynak_klasor, dosya)
        shutil.copy(tam_yol, hedef_klasor)

print("Yedekleme tamamlandı.")
