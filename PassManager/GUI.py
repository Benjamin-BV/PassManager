#Web-interface imports
from flask import Flask, render_template
import webbrowser

#Backend functionality from other files, minus testing main()
from findpass import findservice
from  passwordgen import genPass, generate, askPass, askService

#Main program functionality

app = Flask(__name__)

@app.route("/")#Setting path to current path

#Test function for flask
def index():
    return render_template('index.html');

#Allow webservice interactions with user files, maybe Tkinter is better for this project(?) since it is ENTIRELY local
if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:8001");
    app.run(port=8001, host= "127.0.0.1"); #Run on localhost, on unintrusive port(port 0 selects random unused port in non-reserved range)


