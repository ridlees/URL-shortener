from flask import Flask, render_template, request, send_from_directory, redirect
from dotenv import load_dotenv
import os
import json
from os.path import join, dirname

load_dotenv()

domain = os.environ.get("DOMAIN")

def random_url_id():
    #TO DO random character generator
    pass
    return url

def check_url(url_id):
    # TO DO look into database and check for url. 
    return "test"

def get_url(url_id):
    # TO DO  look into database and get url + increase visit count ++
    url = "https://nolog.cz"
    return url

def create_url(url, url_id = None):
    # TO DO call random_url_id if none url_id specified and add thing to database
    pass
    return "AsWgAZTO"

app = Flask(__name__, template_folder='./conf/templates')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/u/<url_id>")
def redirecter(url_id):
    url = get_url(url_id)
    return redirect(url, code=302)

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route("/create", methods=['POST'])
def create_route():
    if request.method == 'POST':
        url = request.form.get("url")
        url_id = request.form.get("url_id")
        print(url, url_id)
        url_id = create_url(url, url_id)
        return f"{domain}/{url_id}"

@app.route("/curl/<url>")
def curl_create_route(url):
    url_id = create_url(url)
    return f"{domain}/{url_id}"
