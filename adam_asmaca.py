import random

def adam_cizimi(hak):
    asamalar = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return asamalar[6 - hak]

def adam_asmaca():
    kelimeler = [
        "python", "bilgisayar", "yazilim", "programlama", "openai", "chatgpt",
        "internet", "klavye", "monitor", "veritabani", "algoritma", "fonksiyon",
        "dongu", "degisken", "sinif", "nesne", "kalitim", "polimorfizm", "modul",
        "paket", "yapayzeka", "siniragi", "verimlilik", "uygulama", "araclar"
    ]
    skor = 0
    while True:
        secilen_kelime = random.choice(kelimeler)
        tahmin_edilen = ["_"] * len(secilen_kelime)
        hak = 6
        kullanilan_harfler = []

        print("\nYeni oyun başladı! Kelimenin harf sayısı:", len(secilen_kelime))

        while hak > 0 and "_" in tahmin_edilen:
            print(adam_cizimi(hak))
            print("Tahmin edilen kelime:", " ".join(tahmin_edilen))
            print("Kullanılan harfler:", " ".join(sorted(kullanilan_harfler)))
            print(f"Kalan hakkın: {hak}  |  Skorun: {skor}")

            tahmin = input("Bir harf tahmin et (veya 'çık' yaz oyunu bitir): ").lower()

            if tahmin == "çık":
                print(f"Oyun bitti! Son skorun: {skor}")
                return

            if len(tahmin) != 1 or not tahmin.isalpha():
                print("Lütfen sadece bir harf gir.")
                continue

            if tahmin in kullanilan_harfler:
                print("Bu harfi zaten tahmin ettin.")
                continue

            kullanilan_harfler.append(tahmin)

            if tahmin in secilen_kelime:
                for i, harf in enumerate(secilen_kelime):
                    if harf == tahmin:
                        tahmin_edilen[i] = tahmin
                print("Doğru tahmin!")
            else:
                hak -= 1
                skor -= 1
                print("Yanlış tahmin!")

        if "_" not in tahmin_edilen:
            skor += 5
            print("\nTebrikler! Kelimeyi doğru bildin:", secilen_kelime)
            print(f"Skorun: {skor}")
        else:
            print(adam_cizimi(hak))
            print("\nHakkın bitti. Kelime şuydu:", secilen_kelime)
            print(f"Skorun: {skor}")

        devam = input("Tekrar oynamak ister misin? (e/h): ").lower()
        if devam != "e":
            print(f"Oyunu bitirdin. Final skorun: {skor}")
            break

if __name__ == "__main__":
    adam_asmaca()
