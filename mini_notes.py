def not_ekle(dosya_adi, not_metni):
    with open(dosya_adi, "a", encoding="utf-8") as f:
        f.write(not_metni + "\n")
    print("✅ Not eklendi.")

def notlari_goster(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            notlar = f.readlines()
            if notlar:
                print("\n📒 Kayıtlı Notlar:")
                for i, not_ in enumerate(notlar, 1):
                    print(f"{i}. {not_.strip()}")
            else:
                print("📭 Hiç not bulunamadı.")
    except FileNotFoundError:
        print("❌ notlar.txt bulunamadı.")

def not_sil(dosya_adi, silinecek_index):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            notlar = f.readlines()

        if 0 < silinecek_index <= len(notlar):
            silinen = notlar.pop(silinecek_index - 1)
            with open(dosya_adi, "w", encoding="utf-8") as f:
                f.writelines(notlar)
            print(f"🗑️ Silinen not: {silinen.strip()}")
        else:
            print("⚠️ Geçersiz not numarası.")
    except FileNotFoundError:
        print("❌ notlar.txt bulunamadı.")

def not_ara(dosya_adi, anahtar_kelime):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            notlar = f.readlines()
            bulunanlar = [n.strip() for n in notlar if anahtar_kelime.lower() in n.lower()]
            if bulunanlar:
                print("\n🔍 Arama Sonuçları:")
                for i, not_ in enumerate(bulunanlar, 1):
                    print(f"{i}. {not_}")
            else:
                print("🔎 Hiçbir not eşleşmedi.")
    except FileNotFoundError:
        print("❌ notlar.txt bulunamadı.")

def uygulama():
    dosya_adi = "notlar.txt"
    while True:
        print("\n1. Not Ekle\n2. Notları Göster\n3. Not Sil\n4. Not Ara\n5. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            not_metni = input("Eklemek istediğiniz not: ")
            not_ekle(dosya_adi, not_metni)
        elif secim == "2":
            notlari_goster(dosya_adi)
        elif secim == "3":
            notlari_goster(dosya_adi)
            try:
                index = int(input("Silmek istediğiniz not numarası: "))
                not_sil(dosya_adi, index)
            except ValueError:
                print("⚠️ Lütfen bir sayı girin.")
        elif secim == "4":
            anahtar = input("Aranacak kelime: ")
            not_ara(dosya_adi, anahtar)
        elif secim == "5":
            print("👋 Görüşmek üzere!")
            break
        else:
            print("⚠️ Geçersiz seçim.")

uygulama()
