import random
import os

REKOR_DOSYA = "rekor.txt"
GEÇMIŞ_DOSYA = "gecmis.txt"

def rekor_oku():
    if os.path.exists(REKOR_DOSYA):
        with open(REKOR_DOSYA, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    return None

def rekor_yaz(deneme):
    with open(REKOR_DOSYA, "w", encoding="utf-8") as f:
        f.write(str(deneme))

def gecmis_ekle(deneme, aralik):
    with open(GEÇMIŞ_DOSYA, "a", encoding="utf-8") as f:
        f.write(f"{aralik} aralığında {deneme} denemede bildi.\n")

def gecmisi_goster():
    if os.path.exists(GEÇMIŞ_DOSYA):
        with open(GEÇMIŞ_DOSYA, "r", encoding="utf-8") as f:
            print("\n--- Geçmiş Tahminler ---")
            print(f.read())
    else:
        print("\nHenüz geçmiş bulunmuyor.")

def performans_yorumu(deneme):
    if deneme == 1:
        return "Mükemmel!"
    elif deneme <= 3:
        return "Çok İyi!"
    elif deneme <= 5:
        return "İyi!"
    elif deneme <= 7:
        return "İdare Eder."
    elif deneme <= 10:
        return "Kötü."
    else:
        return "Çok Kötü!"

def zorluk_seviyesi():
    print("Zorluk Seviyesini Seç:")
    print("1. Kolay (1-50)")
    print("2. Orta (1-100)")
    print("3. Zor (1-200)")

    while True:
        secim = input("Seçiminiz (1/2/3): ")
        if secim == "1":
            return 1, 50
        elif secim == "2":
            return 1, 100
        elif secim == "3":
            return 1, 200
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")

def sayi_tahmin_oyunu():
    alt, ust = zorluk_seviyesi()
    sayi = random.randint(alt, ust)
    deneme = 0

    print(f"\n{alt} ile {ust} arasında bir sayı tuttum. Tahmin et!")

    while True:
        tahmin = int(input("Tahminin: "))
        deneme += 1

        if tahmin < sayi:
            print("Daha büyük bir sayı dene!")
        elif tahmin > sayi:
            print("Daha küçük bir sayı dene!")
        else:
            print(f"\nTebrikler! {deneme} denemede bildin.")
            print(performans_yorumu(deneme))

            # Geçmişe kaydet
            aralik = f"{alt}-{ust}"
            gecmis_ekle(deneme, aralik)

            # Rekor kontrolü
            eski_rekor = rekor_oku()
            if eski_rekor is None or deneme < eski_rekor:
                rekor_yaz(deneme)
                print(f"🎉 Yeni rekor! {deneme} deneme.")
            else:
                print(f"Mevcut rekor: {eski_rekor} deneme.")

            # Geçmiş görmek ister mi?
            goster = input("\nGeçmiş tahminlerini görmek ister misin? (e/h): ").lower()
            if goster == "e":
                gecmisi_goster()
            break

sayi_tahmin_oyunu()