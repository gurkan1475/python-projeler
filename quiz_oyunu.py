import random

def sorulari_oku(dosya_adi):
    sorular = []
    with open(dosya_adi, "r", encoding="utf-8") as f:
        for satir in f:
            if "|" in satir:
                soru, cevap = satir.strip().split("|")
                sorular.append({"soru": soru, "cevap": cevap.lower()})
    return sorular

def quiz_oyunu():
    sorular = sorulari_oku("sorular.txt")
    toplam_soru = len(sorular)

    if toplam_soru == 0:
        print("Hiç soru bulunamadı! sorular.txt dosyasını kontrol et.")
        return

    print("Bilgi Yarışmasına Hoş Geldin!")
    print("İstediğin zaman 'çıkış' yazarak oyunu bitirebilirsin.\n")

    # Kullanıcıdan soru sayısı al
    istenen_sayi = int(input(f"Kaç soru istersin? (Max {toplam_soru}): "))
    if istenen_sayi > toplam_soru:
        print(f"Maksimum soru sayısını aştınız! Soru sayısı {toplam_soru} olarak ayarlandı.")
        istenen_sayi = toplam_soru

    # Soruları rastgele seç
    secilen_sorular = random.sample(sorular, istenen_sayi)

    dogru = 0
    for i, s in enumerate(secilen_sorular, 1):
        cevap = input(f"{i}. Soru: {s['soru']} ").lower()
        if cevap == "çıkış":
            print("Oyundan çıkış yaptın!")
            break
        if cevap == s["cevap"]:
            print("Doğru!\n")
            dogru += 1
        else:
            print(f"Yanlış! Doğru cevap: {s['cevap']}\n")

    # Doğruluk oranını hesapla
    if i > 0:
        oran = round((dogru / i) * 100)
        print(f"Yarışma bitti! {dogru}/{i} doğru bildin.")
        print(f"Doğruluk oranı: %{oran}")

quiz_oyunu()
