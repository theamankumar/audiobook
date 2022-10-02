import PyPDF2
import pyttsx3

pdfPath = input("Enter PDF File Path: ")
pdfReader = PyPDF2.PdfFileReader(open(pdfPath, 'rb'))

speaker = pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

audiobook = input("Enter the AudioBook Name(with .mp3 Extension): ") 
engine.save_to_file(text, audiobook)
engine.runAndWait()
