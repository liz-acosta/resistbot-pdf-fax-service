import configs
import os

from fpdf import FPDF

def create_pdf(message):

    pdf = FPDF()
    pdf_file_name = "test-001.pdf"
    pdf_file_path = (os.path.join(os.getcwd())) + "/resources/" + pdf_file_name
    message_text = message #This should be some bit of Twilio code that retrieves the body from a text message or from wherever else we're going to keep these messages

    pdf.add_page()
    pdf.set_font("Arial", "", 10)
    pdf.cell(40, 10, message_text, "C")
    pdf.output((os.path.join(os.getcwd())) + "/resources/" + pdf_file_name)

    print "Pdf created" #Replace with logging of your choice
    return pdf_file_path

