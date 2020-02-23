# cd C:\dev\1
# venv\Scripts\activate
# set FLASK_APP=main.py    
# python -m flask run
# baseUrl/Localhost =  http://127.0.0.1:5000
# ctrl + C

from flask import Flask
app = Flask(__name__)

@app.route('/user')
def hello_world():
    # бизнес-логика
    return '{"user":"sss"}'


@app.route('/street')
def name():
    return "xrv"

    # LAMP

    # linux
    # apache
    # mysql
    # php

    # 127.0.0.1
    # 0.0.0.0 
    # localhost:5000  localhost:3306
