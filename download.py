from tkinter.filedialog import asksaveasfilename
import datetime
import csv

fileType = ['Download as TXT', 'Download as CVS']

currentDatetime = datetime.datetime.now()

day = currentDatetime.day
month = currentDatetime.month
year = currentDatetime.year
hours = currentDatetime.time().hour
minutes = currentDatetime.time().minute
seconds = currentDatetime.time().second


def downloadTXT(originalLang, originalText, destinationLang, translatedText):
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], initialfile=f"Translation ({originalLang}-{destinationLang})")

    if file_path:
        try:
            with open(file_path, "w") as file:
                content = f"{originalLang} : {originalText}\n{destinationLang} : {translatedText} \n\nDownloaded Time is {hours} : {minutes} : {seconds} ({day}/{month}/{year})"
                file.write(content)
            print(f"File saved to {file_path}")
        except Exception as e:
            print(f"Error saving file: {str(e)}")

def downloadCVS(originalLang, originalText, destinationLang, translatedText):
    data = [
        [originalLang, destinationLang],
        [originalText, translatedText],
    ]

    file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], initialfile=f"Translation ({originalLang}-{destinationLang})")

    if file_path:
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            
            print(f"CSV file saved to {file_path}")

        except Exception as e:
            print(f"Error: {str(e)}")

fileTypeToFunction = {
    "Download as TXT": "TXT",
    "Download as CVS": "CVS"
}