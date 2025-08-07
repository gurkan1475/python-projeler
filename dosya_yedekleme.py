import os
import shutil
from datetime import datetime

def yedekle(kaynak_klasor, hedef_klasor):
    os.makedirs(hedef_klasor, exist_ok=True)

    yedeklenenler = 0
    atlananlar = 0

    for klasor_yolu, alt_klasorler, dosyalar in os.walk(kaynak_klasor):
        for dosya in dosyalar:
            kaynak_dosya = os.path.join(klasor_yolu, dosya)
            hedef_dosya = os.path.join(hedef_klasor, dosya)

            if not os.path.exists(hedef_dosya):
                shutil.copy2(kaynak_dosya, hedef_dosya)
                print(f"[✓] {dosya} yedeklendi.")
                yedeklenenler += 1
            else:
                print(f"[!] {dosya} zaten yedeklenmiş, atlandı.")
                atlananlar += 1

    # Log kaydı oluştur
    log_bilgisi = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - '{kaynak_klasor}' klasöründen '{hedef_klasor}' klasörüne {yedeklenenler} dosya yedeklendi, {atlananlar} dosya atlandı.\n"
    
    with open("yedek_kayit.txt", "a", encoding="utf-8") as log:
        log.write(log_bilgisi)

    print("\n--- Yedekleme tamamlandı ---")
    print(log_bilgisi)

def main():
    print("📦 Dosya Yedekleme Programı")
    print("Çıkmak için her zaman 'q' yazabilirsin.\n")

    while True:
        kaynak = input("Yedeklenecek klasör yolunu gir: ")
        if kaynak.lower() == 'q':
            print("Program sonlandırıldı.")
            break

        hedef = input("Yedeklerin kaydedileceği klasör yolunu gir: ")
        if hedef.lower() == 'q':
            print("Program sonlandırıldı.")
            break

        if os.path.exists(kaynak):
            yedekle(kaynak, hedef)
        else:
            print("⚠️ Kaynak klasör bulunamadı. Lütfen doğru yol gir.")

if __name__ == "__main__":
    main()
