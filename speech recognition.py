import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# open the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something:")
    # record the audio
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)