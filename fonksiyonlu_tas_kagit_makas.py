import random

secenekler = ["tas", "kagit", "makas"]

def bilgisayar_secimi():
    return random.choice(secenekler)

def kazanan_kontrol(oyuncu, bilgisayar):
    if oyuncu == bilgisayar:
        return "Berabere"
    elif (oyuncu == "tas" and bilgisayar == "makas") or \
         (oyuncu == "kagit" and bilgisayar == "tas") or \
         (oyuncu == "makas" and bilgisayar == "kagit"):
        return "Kazandın!"
    else:
        return "Kaybettin!"

def oyunu_baslat():
    while True:
        oyuncu = input("Seç (tas/kagit/makas): ").lower()
        if oyuncu not in secenekler:
            print("Geçersiz seçim!")
            continue

        bilgisayar = bilgisayar_secimi()
        print("Bilgisayar:", bilgisayar)
        print(kazanan_kontrol(oyuncu, bilgisayar))

        tekrar = input("Tekrar oynamak ister misin? (e/h): ").lower()
        if tekrar != "e":
            break

oyunu_baslat()