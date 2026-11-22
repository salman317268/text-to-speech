from gtts import gTTS
import os

print("===== TEXT TO VOICE CONVERTER =====")

print("1. Bangla")
print("2. English")

choice = input("Choose language (1/2): ")

if choice == "1":
    language = "bn"
elif choice == "2":
    language = "en"
else:
    print("Invalid choice!")
    exit()

text = input("Write something: ")

if text.strip():
    voice = gTTS(text=text, lang=language)
    voice.save("voice.mp3")

    print("Voice created successfully!")

    os.startfile("voice.mp3")
else:
    print("Please write something!")
