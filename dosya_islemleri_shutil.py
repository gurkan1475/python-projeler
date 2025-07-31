import shutil

# 1. Dosyayı kopyalama
shutil.copy("deneme_klasoru/ornek.txt", "ornek_kopya.txt")

# 2. Dosyayı taşıma
shutil.move("ornek_kopya.txt", "deneme_klasoru/ornek_tasindi.txt")

# 3. Dosya silme
os.remove("deneme_klasoru/ornek_tasindi.txt")

# 4. Klasör silme
shutil.rmtree("deneme_klasoru")
