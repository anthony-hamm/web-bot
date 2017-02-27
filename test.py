#!flask/bin/python
import logging
from logging import getLogger

from flask import Flask
from flask import Flask, request, jsonify, json, Response, render_template

app = Flask(__name__)

data = {
    "code":
        "def HelloWorld():\n  print(\"hello world print\")\n  return \"final de hello world\"\n\n"
}

logging.basicConfig(filename='web_bot.log')
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/aprender/test', methods=['GET'])
def getCode():
    try:
        json_result = json.dumps(data)
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
        logger.warning("%s : %s" %(e,'metodo tiene un error'))
        return "Server error (500) - El metodo tiene un error", print(e)
    else:
        logger.info("%s : %s" %(pushtojson, "aprendio de forma exitosa %s"))
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
    import sandbox
    sandbox.HelloWorld()
    return "Ejecuté la función HelloWorld desde otro archivo"


@app.errorhandler(404)
def page_not_found(error):
    logger.info("la ruta no existe")
    return 'Esta ruta no existe', 404


## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
