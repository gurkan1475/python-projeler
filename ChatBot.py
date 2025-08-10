# chatbot.py

def chatbot():
    print("Merhaba! Ben senin asistanın. Çıkmak için 'çık' yaz.")
    while True:
        user_input = input("Sen: ").lower()

        if user_input == "çık":
            print("Chatbot: Görüşürüz!")
            break

        elif "merhaba" in user_input:
            print("Chatbot: Sana da merhaba!")

        elif "nasılsın" in user_input:
            print("Chatbot: İyiyim, teşekkürler. Sen nasılsın?")

        elif "saat kaç" in user_input:
            from datetime import datetime
            print("Chatbot:", datetime.now().strftime("%H:%M:%S"))

        else:
            print("Chatbot: Bunu henüz bilmiyorum.")

if __name__ == "__main__":
    chatbot()
