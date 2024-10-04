from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada
base_datos = {
    "usuarios": [
        {"id": 1, "nombre": "Juan"},
        {"id": 2, "nombre": "María"}
    ]
}

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(base_datos["usuarios"])

if __name__ == '__main__':
    app.run(port=5000)
