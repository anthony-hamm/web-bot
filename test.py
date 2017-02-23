#!flask/bin/python
from flask import Flask
from flask import Flask, request, jsonify, json, Response

app = Flask(__name__)

json_test = {
    "algo1": "def HelloWorld():",
    "algo2": "  print('hello world print')",
    "algo3": "  return 'final de hello world'"
}


@app.route('/')
def index():
    return "index"


@app.route('/push_json', methods=['GET'])
def pushtojson():
    try:
        json_result = json_test
        with open('sandbox.py', 'a') as outfile:
            json.dump(json_result, outfile)
    except Exception as e:
        return "Server error (500) - El metodo tiene un error", print(e)
    else:
        return "Se agrego el JSON test"


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


@app.route('/ejecute/HelloWorld')
def test3():
    import sandbox
    sandbox.HelloWorld()
    return "Ejecuté la función HelloWorld desde otro archivo"


@app.errorhandler(404)
def page_not_found(error):
    return 'Esta ruta no existe', 404


## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
