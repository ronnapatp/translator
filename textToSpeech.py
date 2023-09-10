# Import necessary modules for text-to-speech (TTS) and audio playback.
from gtts import gTTS
import pygame.mixer
import time

# Initialize the pygame mixer for audio playback.
pygame.mixer.init()

# Define a function to convert text to speech and play it.
def textSpeech(text, language):
    # Create a gTTS object with the specified text and language.
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the generated speech as an MP3 file.
    tts.save("output.mp3")

    # Load the saved MP3 file for playback.
    sound = pygame.mixer.Sound('output.mp3')

    # Play the generated speech.
    sound.play()

    # Pause the program execution until the audio playback is complete.
    time.sleep(sound.get_length())
