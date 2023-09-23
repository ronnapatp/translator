import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
from tkinter import messagebox
from textToSpeech import textSpeech
from download import fileType, fileTypeToFunction, downloadCSV, downloadTXT
import pyperclip

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

def clipboard(textType):
    text = outputText.get("1.0", "end-1c") if textType == "translated" else inputText.get("1.0", "end-1c")
    try:
        pyperclip.copy(text)
        errorMessage("Copied!")
    except Exception as error:
        errorMessage(error)


def clearText():
    outputText.config(state="normal")
    outputText.delete("1.0", "end")
    outputText.config(state="disabled")
    inputText.delete("1.0", "end")

def switchSide():
    outputText.config(state="normal")
    output = outputText.get("1.0", "end-1c")
    outputText.delete("1.0","end")
    outputText.insert("1.0", inputText.get("1.0", "end-1c"))
    inputText.delete("1.0","end")
    inputText.insert("1.0", output)
    outputText.config(state="disabled")

    outputLang = destinationLang.get()
    destinationLang.set(sourceLang.get())
    sourceLang.set(outputLang)


def onDownloadSelect(event):
    selectedValue = fileTypeDownload.get()
    selectedFunction = fileTypeToFunction.get(selectedValue)
    if selectedFunction == "TXT":
        downloadTXT(sourceLang.get(), inputText.get("1.0", "end-1c"), destinationLang.get(), outputText.get("1.0", "end-1c"))
    elif selectedFunction == "CSV": 
        downloadCSV(sourceLang.get(), inputText.get("1.0", "end-1c"), destinationLang.get(), outputText.get("1.0", "end-1c"))
    else:
        errorMessage("Please Select Valid File Type")

languagesListBF = list(LANGUAGES.values())
languagesList = []

for item in languagesListBF:
    languagesList.append(item.capitalize())

root = tk.Tk()
root.title("Translator")
root.iconbitmap("./image/icon.png")

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

switchButton = tk.Button(main_frame, text="Switch", command=switchSide)
switchButton.grid(row=0, column=1, padx=10, pady=10)

ttsButtonDestination = tk.Button(main_frame, text="Speak", compound=tk.LEFT, command=lambda: text_to_speech("translated"), width=10, height=5)
ttsButtonDestination.grid(row=2, column=2, padx=10, pady=10)

ttsButtonOriginal = tk.Button(main_frame, text="Speak", compound=tk.LEFT, command=lambda: text_to_speech("original"), width=10, height=5)
ttsButtonOriginal.grid(row=2, column=0, padx=10, pady=10)

copyButtonDestination = tk.Button(main_frame, text="Copy", compound=tk.LEFT, command=lambda: clipboard("translated"), width=10, height=5)
copyButtonDestination.grid(row=3, column=2, padx=10, pady=10)

copyButtonOriginal = tk.Button(main_frame, text="Copy", compound=tk.LEFT, command=lambda: clipboard("original"), width=10, height=5)
copyButtonOriginal.grid(row=3, column=0, padx=10, pady=10)

fileTypeDownload = tk.StringVar()

downloadCombobox = ttk.Combobox(main_frame, textvariable=fileTypeDownload, values=fileType, state="readonly")
downloadCombobox.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

downloadCombobox.set("Click to download")

downloadCombobox.bind("<<ComboboxSelected>>", onDownloadSelect)

root.bind("<Configure>", on_resize)

root.mainloop()