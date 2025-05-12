import sqlite3
from flask import Flask, render_template, request
from markupsafe import escape
# import routers

app = Flask(__name__)

@app.route('/', methods=['POST'])
def auth_user():

    request_data = request.get_json()
    language = request_data['language']
    framework = request_data['framework']
    python_version = request_data['version_info']['python']
    example = request_data['examples'][0]
    boolean_test = request_data['boolean_test']

    return f"language: {language}\nframework: {framework}\n and so on"


if __name__ == '__main__':
    app.run(debug=True)