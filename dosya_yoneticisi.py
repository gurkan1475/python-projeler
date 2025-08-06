import os
import shutil

def menu():
    print("\n--- Dosya Yöneticisi ---")
    print("1. Bulunduğun klasörü göster")
    print("2. Klasör içindekileri listele")
    print("3. Yeni klasör oluştur")
    print("4. Dosya/Klasör sil")
    print("5. Dosya/Klasör taşı")
    print("6. Yeniden adlandır")
    print("7. Klasör değiştir")
    print("8. Çıkış")

while True:
    menu()
    secim = input("Bir işlem seç (1-8): ")

    if secim == "1":
        print("Şu anki konum:", os.getcwd())

    elif secim == "2":
        print("Klasör içeriği:")
        for item in os.listdir():
            print("•", item)

    elif secim == "3":
        isim = input("Yeni klasör adı: ")
        os.makedirs(isim, exist_ok=True)
        print(f"{isim} klasörü oluşturuldu.")

    elif secim == "4":
        hedef = input("Silmek istediğin dosya/klasör adı: ")
        if os.path.isdir(hedef):
            shutil.rmtree(hedef)
        elif os.path.isfile(hedef):
            os.remove(hedef)
        else:
            print("Böyle bir dosya ya da klasör yok.")
        print(f"{hedef} silindi.")

    elif secim == "5":
        kaynak = input("Taşınacak dosya/klasör: ")
        hedef = input("Hedef konum (tam yol ya da klasör adı): ")
        shutil.move(kaynak, hedef)
        print("Taşıma tamamlandı.")

    elif secim == "6":
        eski = input("Eski adı: ")
        yeni = input("Yeni adı: ")
        os.rename(eski, yeni)
        print("Yeniden adlandırma tamam.")

    elif secim == "7":
        yeni_klasor = input("Gitmek istediğin klasör (.. ile geri git): ")
        try:
            os.chdir(yeni_klasor)
            print("Klasör değiştirildi:", os.getcwd())
        except FileNotFoundError:
            print("Klasör bulunamadı.")

    elif secim == "8":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen 1-8 arasında bir sayı gir.")
