import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
from tkinter import messagebox
import io
import cairosvg
from textToSpeech import textSpeech
from download import fileType, fileTypeToFunction, downloadCVS, downloadTXT

translator = Translator()

def on_resize(event):
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.rowconfigure(1, weight=1)

def errorMessage(message):
    messagebox.showerror("Error : ", message)

def translate_text():
    text = inputText.get("1.0", "end-1c")

    if sourceLang.get() == destinationLang.get():
        errorMessage("Original and Translated languages are the same.")
    elif not text:
        errorMessage("No input found")
    else:
        translation = translator.translate(text, src=sourceLang.get(), dest=destinationLang.get())
        outputText.config(state="normal")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", translation.text)
        outputText.config(state="disabled")

def text_to_speech(textType):
    languageIndex = languagesList.index(destinationLang.get() if textType == "translated" else sourceLang.get())
    text = outputText.get("1.0", "end-1c") if textType == "translated" else inputText.get("1.0", "end-1c")
    try:
        textSpeech(text, list(LANGUAGES)[languageIndex])
    except Exception as error:
        errorMessage(error)

def clearText():
    outputText.config(state="normal")
    outputText.delete("1.0", "end")
    outputText.config(state="disabled")
    inputText.delete("1.0", "end")


def onDownloadSelect(event):
    selectedValue = fileTypeDownload.get()
    selectedFunction = fileTypeToFunction.get(selectedValue)
    if selectedFunction == "TXT":
        downloadTXT(sourceLang.get(), inputText.get("1.0", "end-1c"), destinationLang.get(), outputText.get("1.0", "end-1c"))
    elif selectedFunction == "CVS": 
        downloadCVS(sourceLang.get(), inputText.get("1.0", "end-1c"), destinationLang.get(), outputText.get("1.0", "end-1c"))
    else:
        errorMessage("Please Select Valid File Type")

languagesListBF = list(LANGUAGES.values())
languagesList = []

for item in languagesListBF:
    languagesList.append(item.capitalize())

root = tk.Tk()
root.title("Translator")

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

for i in range(3):
    main_frame.columnconfigure(i, weight=1)
    main_frame.rowconfigure(0, weight=1)

inputText = tk.Text(main_frame, height=5, width=30)
inputText.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

outputText = tk.Text(main_frame, height=5, width=30, state="disabled")
outputText.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

sourceLang = tk.StringVar()
destinationLang = tk.StringVar()

sourceLangCombobox = ttk.Combobox(main_frame, textvariable=sourceLang, values=languagesList)
sourceLangCombobox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

destinationLangCombobox = ttk.Combobox(main_frame, textvariable=destinationLang, values=languagesList)
destinationLangCombobox.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

sourceLangCombobox.set("English")
destinationLangCombobox.set("Thai")

translateButton = tk.Button(main_frame, text="Translate", command=translate_text)
translateButton.grid(row=1, column=1, padx=10, pady=10)

clearButton = tk.Button(main_frame, text="Clear", command=clearText)
clearButton.grid(row=2, column=1, padx=10, pady=10)

svg_data = '''
<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 640 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M533.6 32.5C598.5 85.3 640 165.8 640 256s-41.5 170.8-106.4 223.5c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C557.5 398.2 592 331.2 592 256s-34.5-142.2-88.7-186.3c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zM473.1 107c43.2 35.2 70.9 88.9 70.9 149s-27.7 113.8-70.9 149c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C475.3 341.3 496 301.1 496 256s-20.7-85.3-53.2-111.8c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zm-60.5 74.5C434.1 199.1 448 225.9 448 256s-13.9 56.9-35.4 74.5c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C393.1 284.4 400 271 400 256s-6.9-28.4-17.7-37.3c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zM301.1 34.8C312.6 40 320 51.4 320 64V448c0 12.6-7.4 24-18.9 29.2s-25 3.1-34.4-5.3L131.8 352H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h67.8L266.7 40.1c9.4-8.4 22.9-10.4 34.4-5.3z"/></svg>
'''
button_width = 40
button_height = 40

png_data = cairosvg.svg2png(bytestring=svg_data.encode(), output_width=button_width, output_height=button_height)
png_image = Image.open(io.BytesIO(png_data))

tts_icon = ImageTk.PhotoImage(png_image)
ttsButtonDestination = tk.Button(main_frame, text="", image=tts_icon, compound=tk.LEFT, command=lambda: text_to_speech("translated"), width=40, height=40)
ttsButtonDestination.grid(row=2, column=2, padx=10, pady=10)

ttsButtonOriginal = tk.Button(main_frame, text="", image=tts_icon, compound=tk.LEFT, command=lambda: text_to_speech("original"), width=40, height=40)
ttsButtonOriginal.grid(row=2, column=0, padx=10, pady=10)

fileTypeDownload = tk.StringVar()

downloadCombobox = ttk.Combobox(main_frame, textvariable=fileTypeDownload, values=fileType)
downloadCombobox.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

downloadCombobox.set("Click to download")

downloadCombobox.bind("<<ComboboxSelected>>", onDownloadSelect)

root.bind("<Configure>", on_resize)

root.mainloop()