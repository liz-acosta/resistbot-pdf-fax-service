MAKING A BIG BIG CHANGE!!!

Flask service providing endpoints for other Resistbot services. Takes in text, creates a pdf, and sends a fax of that pdf.

Not anywhere near complete, but it's something to work with.

You can run it locally by:
- Establishing and activating a virtual environment
<br>In the project folder:
<br>`$ pip install virtualenv`
<br>`$ virtualenv venv`
<br>`$ source venv/bin/activate`
- Installing the requirements.txt file:
<br>`$ pip install requirements.txt`
- Creating your own `configs.py` following the <a href="https://github.com/liz-acosta/resistbot-pdf-fax-service/blob/master/configs_example.py">configs_example.py</a> and filling in your own keys
- Running `$ python app.py` from command line
- Navigating to <a href="localhost:5000">localhost</a>

The web interface is provided simply for testing purposes and is not intended for the final project.

To check if your faxes have been successful:
 - <a href="https://console.phaxio.com/dashboard">Phaxio dashboard</a>
 - <a href="http://www.faxburner.com/voicemail/index">F@xBurner dashboard</a>

 *Please note these services both require signup*
