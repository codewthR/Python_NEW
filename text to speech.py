from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    """
    Converts text to speech and saves it to an audio file.
    
    Parameters:
        text (str): The text to convert to speech.
        language (str): The language of the text. Defaults to 'en' (English).
        
    Returns:
        str: The filename of the generated audio file.
    """
    tts = gTTS(text=text, lang=language)
    filename = "output.mp3"  # You can customize the filename or path here
    tts.save(filename)
    return filename

# Example usage
text = "Hello , coder "
audio_file = text_to_speech(text)
os.system(f"start {audio_file}")  

''' you need to install the inn your cmd "pip install gtts" before the execution of code'''