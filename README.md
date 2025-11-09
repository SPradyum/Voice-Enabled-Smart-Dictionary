# 🎤 Voice-Enabled Smart Dictionary  
A Python-based Speech-to-Text Dictionary that listens to your voice, recognizes the spoken word, and speaks back the meaning using NLP (WordNet). This project combines speech recognition, text-to-speech, and natural language processing to create an interactive dictionary assistant.

---

## ✅ Features
- 🎙️ **Hands-free operation** — Speak the word you want to know.
- 🧠 **NLP-powered meanings** — Uses WordNet for accurate definitions.
- 🔊 **Voice output** — Reads out the meaning to the user.
- 🎧 **Noise-adjusted listening** — Improves recognition accuracy.
- 🔁 **No duplicate definitions** — Only the most relevant meanings shown.
- 🌐 **Indian English optimized (en-IN)** for better recognition.

---

## ✅ Technologies Used
- **Python**
- **SpeechRecognition**
- **PyAudio**
- **pyttsx3** (Text-to-Speech)
- **NLTK WordNet** (Dictionary Engine)

---

## ✅ Installation

### 1. Install dependencies
```bash
pip install SpeechRecognition pyttsx3 nltk pyaudio
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
```
## ✅ How It Works
- The assistant asks you to speak a word.
- Your speech is converted to text.
- WordNet fetches accurate meanings.
- The assistant speaks and prints the meanings.
- Duplicate and rare meanings are filtered out.

## ✅ Future Enhancements

- Add synonyms and antonyms
- Add example sentences
- GUI/Tkinter interface
- Offline local dictionary
- Save spoken history
