#!flask/bin/python
import logging
from logging import getLogger

import requests

from flask import Flask
from flask import Flask, request, jsonify, json, Response, render_template
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash           # Import helper from wekzeug.security to create hash password

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'web-bot'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


logging.basicConfig(filename='web_bot.log')
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


data = {
    "code":
        "def HelloWorld():\n  print(\"hello world print\")\n  return \"final de hello world\"\n\n"
}

data1 = {
    "code":
        "def Suma(param1, param2):\n  return param1+param2\n\n"
}

data2 = {
    "code":
        "def Resta(param1, param2):\n  return param1-param2\n\n"
}

data3 = {
    "code":
        "def Multiplicacion(param1, param2):\n  return param1*param2\n\n"
}

data4 = {
    "code":
        "def Divicion(param1, param2):\n  return param1/param2\n\n"
}

def Suma(param1, param2):
  return param1+param2


@app.route('/abc', methods=['POST'])
def abc():
        json_result = json.dumps(request.json)
        json_output = json.loads(json_result)
        print(json_output['code'] + "\n")
        print(json_output['name'] + "\n")
        print(json_output['description'] + "\n")
        print(json_output['callback'] + "\n")
        return "true"


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    try:
        # read the posted values from the form
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            connection = mysql.connect()
            cursor = connection.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
            data = cursor.fetchall()
            if len(data) is 0:
                connection.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dump({'error': str(data[0])})
        else:
            return json.dump({'html': '<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dump({'error': str(e)})
    finally:
        cursor.close()
        connection.close()


@app.route('/learnAction', methods=['POST'])
def LearnAction():
    if request.headers['Content-Type'] == 'application/json':
        # convert the json request into a readable format
        json_result = json.dumps(request.json)
        json_output = json.loads(json_result)

        # Add action reference to the DB
        SaveActionToDB(json_output)

        # Add action code to the memory file (sandbox.py)
        WriteCodeToSandbox(json_output)

        # Add action log to the DB
        action = "Learned Action: " + json_output['name'] + " via HTTP POST /learnAction "
        SaveLogToDB(action)
        return "Action added successfully"
    else:
        return "415 Unsupported Media Type"

# Agrega referencias de memoria a la base de datos
def SaveActionToDB(json_output):
    try:
        # read the posted values from the form
        _action_name = json_output['name']
        _action_description = json_output['description']
        _action_callback = json_output['callback']

        # validate the received values
        if _action_name and _action_description and _action_callback:
            # create mySQL connection
            connection = mysql.connect()
            # create the cursor to query the store procedure
            cursor = connection.cursor()
            # call the store procedure on the database to insert the data if it doesn't exist yet
            cursor.callproc('sp_addAction', (_action_name, _action_description, _action_callback))
            data = cursor.fetchall()
            if len(data) is 0:
                connection.commit()
            else:
                return json.dump({'error': str(data[0])}), 409
        else:
            return json.dump({'html': '<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dump({'error': str(e)})
    finally:
        cursor.close()
        connection.close()

def WriteCodeToSandbox(json_output):
    try:
        with open('sandbox.py', 'a') as myFile:
            myFile.write(json_output['code'])
    except Exception as e:
        logger.warning("%s : %s" % (e, 'El método tiene un error'))
    else:
        logger.info("%s : %s" % (getCode, "Se aprendió de forma exitosa"))
        return 'Se agregó el JSON test', 200

def SaveLogToDB(action):
    try:
        add_log = ("INSERT INTO tbl_log "
                   "(log_user, log_action) "
                   "VALUES (%s, %s)")
        # create mySQL connection
        connection = mysql.connect()
        # create the cursor to query the store procedure
        cursor = connection.cursor()
        # call the store procedure on the database to insert the data if it doesn't exist yet
        current_user = "Current User ( " + request.remote_addr + " )"
        cursor.execute(add_log, (current_user, action))
        connection.commit()
    except Exception as e:
        return json.dump({'error': str(e)})
    finally:
        cursor.close()
        connection.close()


@app.route('/showActions', methods=['GET'])
def ShowActions():
    infoArray = GetActionsInfo()
    name = infoArray[0]
    description = infoArray[1]
    json_content = {}
    for i in range(0, len(name)):
        temp = {name[i]:description[i]}
        if json_content == {}:
            json_content = dict(temp)
        else:
            json_content.update(temp)
    res = json.dumps({"Actions": [json_content]})
    return res

def GetActionsInfo():
    # sqlActions = "SELECT action_name FROM `web-bot`.tbl_action;"
    # Query all the rows from a database table
    sql = "SELECT * FROM `web-bot`.tbl_action;"
    try:
        name, description = [], []
        # create mySQL connection
        connection = mysql.connect()
        # create the cursor to query the store procedure
        cursor = connection.cursor()
        # executes the sql query to pull the tbl_action table values
        cursor.execute(sql)
        rcount = cursor.fetchall()
        for r in rcount:
            # row = cursor.fetchone()
            name.append(r[1])
            description.append(r[2])
        infoArray = [name, description]
        return infoArray
    except Exception as e:
        return json.dump({'error': str(e)})
    finally:
        cursor.close()
        connection.close()


@app.route('/deleteAllActions', methods=['DELETE'])
def DeleteAllActions():
    try:
        with open('sandbox.py', 'w') as myFile:
            myFile.write("")
    except Exception as e:
        logger.warning("%s : %s" % (e, 'El método tiene un error'))
        return 'No se pudo eliminar toda la memoria de forma exitosa' + json.dump({'error': str(e)}), 500
    else:
        logger.info("%s : %s" % (getCode, "Se eliminó toda la memoria de forma exitosa"))
        return 'Se eliminó toda la memoria de forma exitosa', 200





@app.route('/aprender/test', methods=['GET'])
def getCode():
    try:
        array = [data1,data2,data3,data4]
        for i in range(len(array)-1):
            json_result = json.dumps(array[i])
            json_output = json.loads(json_result)
            print(json_output['code'])
            with open('sandbox.py', 'a') as myFile:
                myFile.write(json_output['code'])
    except Exception as e:
        logger.warning("%s : %s" % (e, 'El método tiene un error'))
    else:
        logger.info("%s : %s" % (getCode, "Se aprendió de forma exitosa"))
        return 'Se agregó el JSON test', 200


@app.route('/push_json', methods=['GET'])
def pushtojson():
    try:
        json_result = data
        with open('sandbox.py', 'a') as outfile:
            json.dump(json_result, outfile)
    except Exception as e:
        logger.warning("%s : %s" %(e,'Server error (500) - El metodo tiene un error'))
        return "Server error (500) - El metodo tiene un error", print(e)
    else:
        logger.info("%s : %s" %(pushtojson, "Se aprendió de forma exitosa %s"))
        return 'Se agregó el JSON test', 200


@app.route('/aprender/HelloWorld')
def test1():
    with open('sandbox.py', "a") as myfile:
        myfile.write("def HelloWorld():")
        myfile.write("\n")
        myfile.write('  print("hello world print")')
        myfile.write("\n")
        myfile.write('  return "final de hello world"')
        myfile.write("\n")
    return "He aprendido: def HelloWorld():"


@app.route('/ejecutar/test')
def test3():
    try:
        import sandbox
        sandbox.Suma()
    except Exception as e:
        logger.warning("%s : %s" % (e, 'metodo tiene un error'))
    else:
        logger.info("%s : %s" % (pushtojson, "Se ejecutó de forma exitosa"))
        return "Ejecuté la función HelloWorld desde otro archivo"


@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "415 Unsupported Media Type ;)"

@app.route('/weather_api', methods=['GET' , 'POST'])
def weather_api(param):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + param + '&appid=c0962fc3e51084c18e901448850e176f').json()
    return jsonify(r)


@app.route('/clima', methods=['GET' , 'POST'])
def implementar():
    json_result = json.dumps(request.json)
    json_output = json.loads(json_result)
    return weather_api(json_output['pais'])


@app.errorhandler(404)
def page_not_found(error):
    logger.info("la ruta no existe")
    return 'Esta ruta no existe', 404


## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
