import pyttsx3
import PyPDF3
book = open("What is Python.pdf","rb")
pdf_reader = PyPDF3.PdfFileReader(book)

text = ""
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text += page.extractText()
friend = pyttsx3.init()
friend.say(text)
friend.runAndWait()
book.close()