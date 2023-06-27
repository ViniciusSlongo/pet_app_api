from flask import Flask
from flask import request
from .services import Services

app = Flask(__name__)
services = Services()


@app.route("/", methods=['GET'])
def default():
    return "ok"

@app.route("/api/cadastro", methods=['POST'])
def create_cadastro():
    try:
        data = request.json
        services.create_cadastro(data)

        return "OK", 200
    except Exception as err:
        return str(err), 500

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    res = services.login(data)

    if not res:
        return "", 404
    
    return res, 200

@app.route("/api/publicacoes/<usuario_id>", methods=['GET'])
def get_posts_usuario_id(usuario_id):
    res = services.get_posts(usuario_id)

    if not res:
        return "", 404

    return res, 200


@app.route("/api/publicacoes", methods=['GET'])
def get_posts():
    res = services.get_posts()

    if not res:
        return "", 404

    return res, 200

@app.route("/api/publicacao", methods=['POST'])
def post_publicacao():
    data = request.json
    if not data:
        return
    print("data")
    res = services.create_publicacao(data)
    
    if not res:
        return "", 404
    
    return str(res), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", use_reloader=False)