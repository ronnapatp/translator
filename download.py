# Import necessary modules for file handling, date, and CSV operations.
# นำเข้าโมดูลที่จำเป็นสำหรับการจัดการไฟล์ วันที่ เวลา และการดำเนินการ CSV
from tkinter.filedialog import asksaveasfilename
import datetime
import csv

# Define a list of file types for download options.
# กำหนดรายการประเภทของไฟล์สำหรับตัวเลือกการดาวน์โหลด
fileType = ['Download as TXT', 'Download as CSV']

# Get the current date and time.
# รับวันที่และเวลาปัจจุบัน
currentDatetime = datetime.datetime.now()
day = currentDatetime.day
month = currentDatetime.month
year = currentDatetime.year
hours = currentDatetime.time().hour
minutes = currentDatetime.time().minute
seconds = currentDatetime.time().second

# Define a function to download text content as a TXT file.
# กำหนดฟังก์ชันในการดาวน์โหลดเนื้อหาข้อความเป็นไฟล์ TXT
def downloadTXT(originalLang, originalText, destinationLang, translatedText):
    # Prompt the user to select a save location for the TXT file.
    # แจ้งให้ผู้ใช้เลือกตำแหน่งที่จะบันทึกไฟล์ TXT
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], initialfile=f"Translation ({originalLang}-{destinationLang})")

    if file_path:
        try:
            # Write translation content to the selected file.
            # เขียนเนื้อหาแปลเป็นไฟล์ที่เลือก
            content = f"{originalLang} : {originalText}\n{destinationLang} : {translatedText} \n\nDownloaded Time is {hours} : {minutes} : {seconds} ({day}/{month}/{year})"
            with open(file_path, "w") as file:
                file.write(content)
            print(f"File saved to {file_path}")

        # Catch error if it appears.
        # รับข้อผิดพลาดถ้ามีการเกิดขึ้น
        except Exception as e:
            print(f"Error saving file: {str(e)}")

# Define a function to download text content as a CSV file.
# กำหนดฟังก์ชันในการดาวน์โหลดเนื้อหาข้อความเป็นไฟล์ CSV
def downloadCVS(originalLang, originalText, destinationLang, translatedText):
    # Prepare data for CSV file in a list format.
    # เตรียมข้อมูลสำหรับไฟล์ CSV ในรูปแบบรายการ
    data = [
        [originalLang, destinationLang],
        [originalText, translatedText],
    ]

    # Prompt the user to select a save location for the CSV file.
    # แจ้งให้ผู้ใช้เลือกตำแหน่งที่จะบันทึกไฟล์ CSV
    file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], initialfile=f"Translation ({originalLang}-{destinationLang})")

    if file_path:
        try:
            # Write data to the selected CSV file.
            # เขียนข้อมูลลงในไฟล์ CSV ที่เลือก
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            
            print(f"CSV file saved to {file_path}")

        # Catch error if it appears.
        # รับข้อผิดพลาดถ้ามีการเกิดขึ้น
        except Exception as e:
            print(f"Error: {str(e)}")

# Define a dictionary mapping file types to their corresponding download functions.
# กำหนดพจนานุกรมที่ใช้สำหรับแมปประเภทของไฟล์กับฟังก์ชันดาวน์โหลดที่เกี่ยวข้อง
fileTypeToFunction = {
    "Download as TXT": "TXT",
    "Download as CSV": "CSV"
}
