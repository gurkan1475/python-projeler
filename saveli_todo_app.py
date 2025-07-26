import os

DOSYA_ADI = "yapilacaklar.txt"

def dosyadan_oku():
    if os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI, "r", encoding="utf-8") as f:
            return [satir.strip() for satir in f.readlines()]
    return []

def dosyaya_yaz(liste):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        for item in liste:
            f.write(item + "\n")

def menu():
    print("\nYapılacaklar Uygulaması")
    print("1. Yapılacak Ekle")
    print("2. Yapılacakları Listele")
    print("3. Yapılacak Sil")
    print("4. Çıkış")

yapilacaklar = dosyadan_oku()

while True:
    menu()
    secim = input("Seçiminiz: ")

    if secim == "1":
        item = input("Eklemek istediğiniz işi yazın: ")
        yapilacaklar.append(item)
        dosyaya_yaz(yapilacaklar)
        print(f"'{item}' listeye eklendi.")
    elif secim == "2":
        print("\n--- Yapılacaklar ---")
        if not yapilacaklar:
            print("Liste boş!")
        else:
            for i, item in enumerate(yapilacaklar, 1):
                print(f"{i}. {item}")
    elif secim == "3":
        sil = int(input("Silmek istediğiniz numarayı girin: "))
        if 1 <= sil <= len(yapilacaklar):
            silinen = yapilacaklar.pop(sil-1)
            dosyaya_yaz(yapilacaklar)
            print(f"'{silinen}' silindi.")
        else:
            print("Geçersiz numara!")
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")