from flask import render_template, request
from cmd_n_control import app



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    return
