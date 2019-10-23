from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"

@app.route('/api/<int:id>')
def api(id):
    universidades = ["UTEPSA","UAGRM"]
    if id == 0:
        return jsonify({"error":"id no disponible"}), 402
    elif id == 1:
        return jsonify({
            "name":"iden",
            "educacion":universidades,
            "edad": 21
        })
    elif id == 2:
        return jsonify({
            "name":"alex",
            "educacion":"ninguna xddd",
            "edad": 16
        })
if __name__ == '__main__':
    app.run()
 