import os
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture microphone input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            # Adjust for ambient noise and listen
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return "I didn't catch that."
        except sr.RequestError:
            return "Service is down."
        except sr.WaitTimeoutError:
            return "Timeout."

def execute_command(command):
    """Match and execute system commands."""
    if "open browser" in command:
        speak("Opening your default browser.")
        os.system("xdg-open https://www.google.com")
    elif "what time is it" in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}.")
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown now")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Voice assistant activated. Say a command.")
    while True:
        user_command = listen()
        print(f"You said: {user_command}")
        execute_command(user_command)
