import os

# 1. Klasör oluşturma
os.mkdir("deneme_klasoru")

# 2. Mevcut klasördeki dosyaları listeleme
print(os.listdir())

# 3. Çalışma dizinini öğrenme
print("Çalışma dizini:", os.getcwd())

# 4. Dizin değiştirme
os.chdir("deneme_klasoru")
print("Yeni dizin:", os.getcwd())

# 5. Dosya oluşturma
with open("ornek.txt", "w") as dosya:
    dosya.write("Merhaba dünya!")

# 6. Bir üst klasöre çık
os.chdir("..")
