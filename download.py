# Import necessary modules for file handling, date, and CSV operations.
from tkinter.filedialog import asksaveasfilename
import datetime
import csv

# Define a list of file types for download options.
fileType = ['Download as TXT', 'Download as CVS']

# Get the current date and time.
currentDatetime = datetime.datetime.now()
day = currentDatetime.day
month = currentDatetime.month
year = currentDatetime.year
hours = currentDatetime.time().hour
minutes = currentDatetime.time().minute
seconds = currentDatetime.time().second

# Define a function to download text content as a TXT file.
def downloadTXT(originalLang, originalText, destinationLang, translatedText):
    # Prompt the user to select a save location for the TXT file.
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], initialfile=f"Translation ({originalLang}-{destinationLang})")

    if file_path:
        try:
            # Write translation content to the selected file.
            content = f"{originalLang} : {originalText}\n{destinationLang} : {translatedText} \n\nDownloaded Time is {hours} : {minutes} : {seconds} ({day}/{month}/{year})"
            with open(file_path, "w") as file:
                file.write(content)
            print(f"File saved to {file_path}")

        # catch error if it appears
        except Exception as e:
            print(f"Error saving file: {str(e)}")

# Define a function to download text content as a CSV file.
def downloadCVS(originalLang, originalText, destinationLang, translatedText):
    # Prepare data for CSV file in a list format.
    data = [
        [originalLang, destinationLang],
        [originalText, translatedText],
    ]

    # Prompt the user to select a save location for the CSV file.
    file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], initialfile=f"Translation ({originalLang}-{destinationLang})")

    if file_path:
        try:
            # Write data to the selected CSV file.
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            
            print(f"CSV file saved to {file_path}")

        # catch error if it appears
        except Exception as e:
            print(f"Error: {str(e)}")

# Define a dictionary mapping file types to their corresponding download functions.
fileTypeToFunction = {
    "Download as TXT": "TXT",
    "Download as CVS": "CVS"
}
