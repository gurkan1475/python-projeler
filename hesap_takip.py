import os

DOSYA = "hesap.txt"

def bakiye_oku():
    """Mevcut bakiyeyi dosyadan oku."""
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as f:
            satirlar = [s.strip() for s in f.readlines()]
        if satirlar:
            # Dosyadaki son bakiye değerini al
            return int(satirlar[-1].split(":")[-1])
    return 0

def hareket_ekle(tur, miktar, bakiye):
    """Yeni hareketi dosyaya kaydet."""
    with open(DOSYA, "a", encoding="utf-8") as f:
        f.write(f"{tur}: {miktar} TL | Bakiye: {bakiye}\n")

def hareketleri_goster():
    """Geçmiş hareketleri ekrana yazdır."""
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as f:
            print("\n--- Geçmiş Hareketler ---")
            print(f.read())
    else:
        print("Henüz hareket yok.")

# Başlangıç bakiyesi
bakiye = bakiye_oku()

# Menü döngüsü
while True:
    print("\n--- Mini Finans Uygulaması ---")
    print("1. Para Ekle")
    print("2. Harcama Yap")
    print("3. Bakiye Gör")
    print("4. Geçmiş Hareketler")
    print("5. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        miktar = int(input("Eklenecek miktar: "))
        bakiye += miktar
        hareket_ekle("Para Eklendi", miktar, bakiye)
        print(f"{miktar} TL eklendi. Güncel bakiye: {bakiye} TL")

    elif secim == "2":
        miktar = int(input("Harcama miktarı: "))
        if miktar <= bakiye:
            bakiye -= miktar
            hareket_ekle("Harcama", miktar, bakiye)
            print(f"{miktar} TL harcandı. Güncel bakiye: {bakiye} TL")
        else:
            print("Yetersiz bakiye!")

    elif secim == "3":
        print(f"Güncel Bakiye: {bakiye} TL")

    elif secim == "4":
        hareketleri_goster()

    elif secim == "5":
        print("Çıkılıyor...")
        break

    else:
        print("Geçersiz seçim!")