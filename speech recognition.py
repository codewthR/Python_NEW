import speech_recognition as sr
r = sr.Recognizer()
# open the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something:")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)
