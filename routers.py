from flask import render_template
from app import app

@app.route('/')
@app.route('/menucraft')
def index():
    return render_template('index.html')