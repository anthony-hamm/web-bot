#!flask/bin/python
from flask import Flask
from flask import Flask, request, jsonify, json, Response

#
# This is an example of the Flask uses Json to solve some problems ;)
# by marguedas
#
1
app = Flask(__name__)

json_var = {
        "widget":
            {
                "debug": "on",
                "window": {
                    "title": "Sample Konfabulator Widget",
                    "name": "main_window",
                    "width": 500,
                    "height": 500
                },
                "image": {
                    "src": "Images/Sun.png",
                    "name": "sun1",
                    "hOffset": 250,
                    "vOffset": 250,
                    "alignment": "center"
                },
                "text": {
                    "data": "Click Here",
                    "size": 36,
                    "style": "bold",
                    "name": "text1",
                    "hOffset": 250,
                    "vOffset": 100,
                    "alignment": "center",
                    "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
                }

            }
}

json_test = {
        "algo1": "def HelloWorld():",
        "algo2":"  print('hello world print')",
        "algo3":"  return 'final de he\nllo world'"
}

@app.route('/')
def index():

    json_result = json_var
    js = json.dumps(json_result)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://ecommerce.com'

    return resp

@app.route('/push_json')
def pushtojson():
    json_result = json_test
    with open('sandbox.py', 'w') as outfile:
        json.dump(json_result, outfile)
    return "Se agrego el JSON test"

@app.route('/api/ejemplo1', methods=['GET'])
def ejemplo_1():
    return "Ejemplo 2"


@app.route('/api/cds/titulo/autor/<nombre>', methods=['GET'])
def ejemplo_cds(nombre):
    return "Ejemplo 2"

@app.route('/api/ejemplo2')
def ejemplo_2():
    return "Ejemplo 2"

@app.route('/api/ejemplo_param')
def ejemplo_param():

    in_args = request.args                  # Primero Obtener los Parametros
    param = in_args['dato_enviado']         # Seleccionar el parametro deseado

    result = {
        'param_1': param                    # Crear una respuesta Json
    }


    resp = Response(json.dumps(result), status=200, mimetype='application/json') # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp


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

@app.route('/aprender/HelloPlanet')
def test2():
    with open('sandbox.py', "a") as myfile:
        myfile.write("def HelloPlanet():")
        myfile.write("\n")
        myfile.write('  print("hello planet print")')
        myfile.write("\n")
        myfile.write('  return "final de hello planet"')
        myfile.write("\n")
    return "He aprendido: def HelloPlanet():"

@app.route('/ejecute/HelloWorld')
def test3():
    import sandbox
    sandbox.HelloWorld()
    return "Ejecuté la función HelloWorld desde otro archivo"

@app.route('/ejecute/HelloPlanet')
def test4():
    import sandbox
    sandbox.HelloPlanet()
    return "Ejecuté la función HelloPlanet desde otro archivo"

@app.errorhandler(404)
def page_not_found(error):
    return 'Esta ruta no existe', 404


## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')