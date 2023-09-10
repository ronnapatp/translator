# Import necessary modules for text-to-speech (TTS) and audio playback.
# นำเข้าโมดูลที่จำเป็นสำหรับการแปลงข้อความเป็นเสียง (TTS) และการเล่นเสียง
from gtts import gTTS
import pygame.mixer
import time

# Initialize the pygame mixer for audio playback.
# เริ่มต้น pygame mixer เพื่อเล่นเสียง
pygame.mixer.init()

# Define a function to convert text to speech and play it.
# กำหนดฟังก์ชันในการแปลงข้อความเป็นเสียงและเล่นเสียง
def textSpeech(text, language):
    # Create a gTTS object with the specified text and language.
    # สร้างอ็อบเจ็กต์ gTTS ด้วยข้อความและภาษาที่ระบุ
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the generated speech as an MP3 file.
    # บันทึกเสียงที่สร้างเป็นไฟล์ MP3
    tts.save("output.mp3")

    # Load the saved MP3 file for playback.
    # โหลดไฟล์ MP3 ที่บันทึกไว้เพื่อเล่น
    sound = pygame.mixer.Sound('output.mp3')

    # Play the generated speech.
    # เล่นเสียงที่สร้างขึ้น
    sound.play()

    # Pause the program execution until the audio playback is complete.
    # หยุดการทำงานของโปรแกรมจนกว่าการเล่นเสียงจะเสร็จสมบูรณ์
    time.sleep(sound.get_length())
