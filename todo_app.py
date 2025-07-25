yapilacaklar = []

def menu():
    print("\nYapılacaklar Uygulaması")
    print("1. Yapılacak Ekle")
    print("2. Yapılacakları Listele")
    print("3. Yapılacak Sil")
    print("4. Çıkış")

while True:
    menu()
    secim = input("Seçiminiz: ")

    if secim == "1":
        item = input("Eklemek istediğiniz işi yazın: ")
        yapilacaklar.append(item)
        print(f"'{item}' listeye eklendi.")
    elif secim == "2":
        print("\n--- Yapılacaklar ---")
        for i, item in enumerate(yapilacaklar, 1):
            print(f"{i}. {item}")
    elif secim == "3":
        sil = int(input("Silmek istediğiniz numarayı girin: "))
        if 1 <= sil <= len(yapilacaklar):
            silinen = yapilacaklar.pop(sil-1)
            print(f"'{silinen}' silindi.")
        else:
            print("Geçersiz numara!")
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")