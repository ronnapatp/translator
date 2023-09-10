from gtts import gTTS
import pygame.mixer
import time

pygame.mixer.init()

def textSpeech(text, language):
    tts = gTTS(text=text, lang=language, slow=False)

    tts.save("output.mp3")

    sound = pygame.mixer.Sound('output.mp3')
    sound.play()
    time.sleep(sound.get_length())