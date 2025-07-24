import random
import string

def sifre_uret(uzunluk=12):
    """Belirtilen uzunlukta rastgele bir şifre üretir."""
    karakterler = string.ascii_letters + string.digits + "!@#$%^&*()"
    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

def sifre_uretici_programi():
    print("Rastgele Şifre Üreticiye Hoş Geldin!")
    uzunluk = int(input("Şifre uzunluğunu gir: "))
    sifre = sifre_uret(uzunluk)
    print("Oluşturulan şifre:", sifre)

# Programı çalıştır
sifre_uretici_programi()