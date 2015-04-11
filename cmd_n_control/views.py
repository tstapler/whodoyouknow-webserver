from flask import render_template
from cmd_n_control import app

@app.route('/')
def index():
    user = {'nickname': "Tyler"}
    return render_template('index.html',user=user)
