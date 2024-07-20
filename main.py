from flask import Flask, render_template, request, send_from_directory, redirect, json
from dotenv import load_dotenv
import os
import json
from os.path import join, dirname
import sqlite3
from urllib.parse import urlparse


import random_url

load_dotenv()

domain = os.environ.get("DOMAIN")
sample_size = int(os.environ.get("SAMPLE_SIZE"))

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False

def connect_to_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    return c, conn

def random_url_id():
    url_id = random_url.generate_random_string(sample_size)
    if check_url(url_id):
        url_id = random_url_id()
    return url_id

def check_url(url_id):
    c, conn = connect_to_db()
    c.execute("SELECT EXISTS(SELECT 1 FROM urls WHERE url_id=? LIMIT 1)", (url_id,))
    record = c.fetchone()
    if record[0] == 1:
        return True
    else:
        return False

def get_url(url_id):
    c, conn = connect_to_db()
    c.execute("SELECT * FROM urls WHERE url_id=? LIMIT 1", (url_id,))
    record = c.fetchone()
    url = record[1]
    visit_counter = record[2]
    visit_counter = visit_counter + 1
    print(visit_counter)
    c.execute("UPDATE urls SET visit_counter = ? WHERE url_id = ?", (visit_counter, url_id))
    conn.commit()
    return url

def create_url(url, email, url_id = None):
    if url_id == "":
        url_id = random_url_id()
        pass
    if check_url(url_id):
        url_id = random_url_id()
    item = [url_id,url,0, email]
    print(item)
    c, conn = connect_to_db()
    c.execute('insert into urls values (?,?,?,?)', item)
    conn.commit()
    return url_id

app = Flask(__name__, template_folder='./conf/templates')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'conf/static'),
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
        content_type = request.headers.get('Content-Type')
        data = ""
        if (content_type == 'application/x-www-form-urlencoded'):
            data = request.form
        elif (content_type == 'application/json'):
            data = request.json
        else:
            data = json.loads(request.data)
        url = data["url"]
        print(validate_url(url))
        url_id = data["url_id"]
        email = data["email"]
        print(url, url_id, email)
        url_id = create_url(url,email, url_id )
        return f'<span hx-on:click="!window.s?s=this.textContent:null;navigator.clipboard.writeText(s);this.textContent=\'Copied\';setTimeout(()=>{{this.textContent=s}}, 1000)">{domain}/u/{url_id}</span>'

