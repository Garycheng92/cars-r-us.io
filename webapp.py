from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')