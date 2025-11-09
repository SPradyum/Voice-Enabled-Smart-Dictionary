import pyttsx3
import speech_recognition as sr
from nltk.corpus import wordnet as wn


# ✅ Text-to-speech function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# ✅ Initialize TTS Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# ✅ Listen function
def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
    except Exception as e:
        print("❌ Microphone error:", e)
        return None

    try:
        print("✅ Recognizing...")
        text = r.recognize_google(audio, language="en-IN")
        print("You said:", text)
        return text
    except Exception as e:
        print("❌ Speech not recognized:", e)
        return None


# ✅ Get meaning from WordNet
def get_meaning(word):
    synsets = wn.synsets(word)
    if not synsets:
        return None

    meanings = []
    for s in synsets:
        meanings.append((s.pos(), s.definition()))

    return meanings


# ✅ MAIN PROGRAM
speak("Sir, please say the word you want to know the meaning of.")

word = None
while word is None:
    word = listen()

meanings = get_meaning(word)

if meanings:
    speak(f"Sir, here are the meanings of {word}:")
    print("\n📘 MEANINGS:\n")

    shown_pos = set()   # ✅ to avoid duplicate POS outputs

    for pos, meaning in meanings:

        if pos in shown_pos:
            continue  # ✅ Skip if same POS is already printed

        shown_pos.add(pos)

        # ✅ Convert POS to readable format
        pos_full = {
            "n": "noun",
            "v": "verb",
            "a": "adjective",
            "r": "adverb"
        }.get(pos, pos)

        print(f"{pos_full}: {meaning}")
        speak(f"As a {pos_full}, it means: {meaning}")

        if len(shown_pos) >= 2:   # ✅ Limit to top 2 meanings
            break

else:
    speak("Sorry sir, I could not find the meaning.")
