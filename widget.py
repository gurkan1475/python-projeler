import tkinter as tk
import time
import random

# Motivasyon sözleri listesi
motivasyon_sozleri = [
    "Başarısızlık, pes etmediğin sürece gerçek değildir.",
    "Küçük adımlar, büyük hayallerin başlangıcıdır.",
    "Zor zamanlar, güçlü insanları yaratır.",
    "Vazgeçmek yok, hedefe devam!",
    "En zor kararları, en güçlü iradeler verir."
    "made by gurkan1475"
]

def guncelle_saat():
    """Saati sürekli günceller."""
    anlik_saat = time.strftime("%H:%M:%S")
    saat_label.config(text=anlik_saat)
    pencere.after(1000, guncelle_saat)  # Her 1 saniyede güncelle

# Tkinter pencere ayarları
pencere = tk.Tk()
pencere.title("Motivasyon Widget")
pencere.geometry("300x150")
pencere.configure(bg="#1e1e1e")
pencere.resizable(False, False)

# Saat etiketi
saat_label = tk.Label(
    pencere, 
    text="", 
    font=("Helvetica", 32, "bold"), 
    fg="white", 
    bg="#1e1e1e"
)
saat_label.pack(pady=10)

# Motivasyon sözü etiketi
soz_label = tk.Label(
    pencere, 
    text=random.choice(motivasyon_sozleri), 
    font=("Helvetica", 10, "italic"), 
    fg="#ffcc00", 
    bg="#1e1e1e", 
    wraplength=280,
    justify="center"
)
soz_label.pack(pady=5)

# Saati başlat
guncelle_saat()

# Pencereyi çalıştır
pencere.mainloop()
