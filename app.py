from flask import Flask, request, jsonify
import pymysql, json

db = pymysql.connect("91.210.168.226", "root", "password", "test")

app = Flask(__name__)

@app.route('/cities')
def someName():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM city"
    cursor.execute(sql)
    rows = cursor.fetchall()
    resp = jsonify(rows)
    return resp

@app.route('/accounts', methods=["post"])
def createAccounts():
    try:
        i = request.get_json()
        token = i["token"]
        city = i["city"]
        fcm = i["fcm"]
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT users(token, city_id, fcm) VALUES (%s, %s, %s)", (token, city, fcm))
        rows = cursor.fetchall()
        db.commit()
        resp = jsonify(rows)
        return resp
    except Exception as e:
	    return(str(e))
        
@app.route('/plants/accounts', methods=["post"])
def createPlants():
    try:
        i = request.get_json()
        user_id = i["user_id"]
        name = i["name"]
        wateringFrequencyDry = i["wateringFrequencyDry"]
        wateringFrequencyRain = i["wateringFrequencyRain"]
        distanceBetweenPlants = i["distanceBetweenPlants"]
        seedingStartDate = i["seedingStartDate"]
        seedingEndDate = i["seedingEndDate"]
        description = i["description"]
        nextWatering = i["nextWatering"]
        lastWatering = i["lastWatering"]
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""INSERT plants(user_id, name, wateringFrequencyDry, wateringFrequencyRain, distanceBetweenPlants, 
        seedingStartDate, seedingEndDate, description, nextWatering, lastWatering) 
        VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)""", (user_id, name, wateringFrequencyDry, wateringFrequencyRain, distanceBetweenPlants, 
        seedingStartDate, seedingEndDate, description, nextWatering, lastWatering))
        rows = cursor.fetchall()
        db.commit()
        resp = jsonify(rows)
        return resp
    except Exception as e:
	    return(str(e))

@app.route('/plants/accounts/dates', methods=["get"])
def DatePlants():
    try:
        i = request.get_json()
        user_id_from_postan = i["user_id"]
        data = i["data"]
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT * FROM plants where huy = %s and nextWateringHuiy = %s """, (user_id_from_postan, data))
        rows = cursor.fetchall()
        if not rows:
            resp = jsonify({
                "description": "",
                "distanceBetweenPlants": "",
                "huy": "",
                "id": "",
                "lastWatering": "",
                "name": "",
                "nextWateringHuiy": "",
                "seedingEndDate": "",
                "seedingStartDate": "",
                "wateringFrequencyDry": "",
                "wateringFrequencyRain": ""
            })
            return resp
        else:
            resp = jsonify(rows)
            return resp
    except Exception as e:
	    return(str(e))

@app.route('/plants/accounts/search', methods=["get"])
def searchPlants():
    try:
        i = request.get_json()
        name = i["name"]
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM plants where name = %s", (name))
        rows = cursor.fetchall()
        if not rows:
            resp = jsonify({
                "description": "",
                "distanceBetweenPlants": "",
                "huy": "",
                "id": "",
                "lastWatering": "",
                "name": "",
                "nextWateringHuiy": "",
                "seedingEndDate": "",
                "seedingStartDate": "",
                "wateringFrequencyDry": "",
                "wateringFrequencyRain": ""
            })
            return resp
        else:
            resp = jsonify(rows)
            return resp
    except Exception as e:
	    return(str(e))

@app.route('/plants/<int:plants_id>/accounts/<int:user_id>', methods=["patch"])
def watering(plants_id, user_id):
    i = request.get_json()
    data =i["lastWatering"]
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("UPDATE plants SET lastWatering = %s where huy=%s and id = %s", (data, user_id, plants_id))
        db.commit()
        if not rows:
            resp = jsonify({
                "description": "",
                "distanceBetweenPlants": "",
                "huy": "",
                "id": "",
                "lastWatering": "",
                "name": "",
                "nextWateringHuiy": "",
                "seedingEndDate": "",
                "seedingStartDate": "",
                "wateringFrequencyDry": "",
                "wateringFrequencyRain": ""
            })
            return resp
        else:
            resp = jsonify(rows)
            return resp
    except Exception as e:
	    return(str(e))

@app.route('/plants/accounts/token/<int:token>', methods=["get"])
def plantsByToken(token):
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""select plants.*  
        from plants
        inner join users on users.id = plants.huy
        where users.token = %s """, (token))
        rows = cursor.fetchall()
        if not rows:
            resp = jsonify({
                "description": "",
                "distanceBetweenPlants": "",
                "huy": "",
                "id": "",
                "lastWatering": "",
                "name": "",
                "nextWateringHuiy": "",
                "seedingEndDate": "",
                "seedingStartDate": "",
                "wateringFrequencyDry": "",
                "wateringFrequencyRain": ""
            })
            return resp
        else:
            resp = jsonify(rows)
            return resp
    except Exception as e:
	    return(str(e))



if __name__ == '__main__':
    app.run(debug=True)