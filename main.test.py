import speech_recognition as sr

def test_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mikrofon ishlayapti... Gapirishni boshlang.")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Tashqi shovqinni yo'q qilish uchun sozlash
        try:
            print("Ovoz yozilmoqda...")
            audio = recognizer.listen(source)
            print("Ovoz yozib olindi! Tahlil qilinmoqda...")
            text = recognizer.recognize_google(audio, language="uz-UZ")  # "uz-UZ" til kodi
            print(f"Aniqlangan matn: {text}")
        except sr.UnknownValueError:
            print("Ovozni tushunib bo'lmadi. Iltimos, qayta gapiring.")
        except sr.RequestError as e:
            print(f"Xatolik yuz berdi: {e}")

# Mikrofonni sinash
test_microphone()
