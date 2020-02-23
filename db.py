from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import json


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'smarthome'
app.config['MYSQL_DATABASE_HOST'] = '91.210.169.48'
mysql.init_app(app)

@app.route('/city', methods=['GET'])
def index():
    conn = mysql.connect()
    cursor =conn.cursor()
    # cursor.execute("INSERT leisan(id, colone, coltwo, colthre) VALUES (67, 666, 5, 76000)")
    # cursor.execute("DELETE FROM leisan WHERE id=67")
    # cursor.execute("UPDATE leisan SET id = 89")
    cursor.execute("SELECT * FROM plants") where token = 9999
    conn.commit() 
    # mysql = select, delete, update, insert
    data = cursor.fetchall() #typle
    resp = jsonify(data) #convert to json
    return resp #возврат   

@app.route('/city/client', methods=['POST'])
def city():
    cityy = request.form.get('city')
    tokenn = request.form.get('token')    
    conn = mysql.connect()
    cursor =conn.cursor()
    # cursor.execute(" INSERT city(id, city) VALUES (67, 'ddddd') ")
    cursor.execute(" INSERT user(id, city, token) VALUES (67, %s, %s) ", (cityy, tokenn))
    conn.commit() 
    data = cursor.fetchall()
    resp = jsonify(data)
    return cityy   

# FROM LEISAN
select plants.id, users.id
    from plants
    inner join users on users.id = plants.huy
            where users.id = 1


select plants.*,  
    from plants
    inner join users on users.id = plants.huy
    where users.token = 999