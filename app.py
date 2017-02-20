from flask import Flask, request, render_template

import configs
import pdf_creator
import send_fax

app = Flask(__name__)

@app.route("/")
def default():
    return render_template("index.html")

@app.route("/create_pdf")
def create_pdf():
    #Takes a message from RapidPro or wherever, returns a pdf (Which is currently being written to the resources dir, but Where will it ultimately go?)

    message = request.args.get("message")

    try:
        pdf_file_path = pdf_creator.create_pdf(message)
        send_fax_app(pdf_file_path)
        return render_template("index.html", file_path=pdf_file_path, response_message="Pdf successfully created with text: " + message)
    except:
        return render_template("index.html", response_message="Failed to create pdf.")

@app.route("/send_fax")
def send_fax_app(pdf_file_path):
#Takes a pdf from wherever we're keeping them, sends a fax

    try:
        send_fax.send_fax(pdf_file_path)
        return render_template("index.html", response_message="Fax sent to: " + configs.fax_number)
    except:
        return render_template("index.html", response_message="Failed to send fax.")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")