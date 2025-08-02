import os

klasor = "indirilenler"
temizlenecek_uzantilar = [".log", ".tmp", ".bak"]

for dosya in os.listdir(klasor):
    if any(dosya.endswith(uzanti) for uzanti in temizlenecek_uzantilar):
        dosya_yolu = os.path.join(klasor, dosya)
        os.remove(dosya_yolu)
        print(f"{dosya} silindi.")

print("Temizlik tamamlandı.")
