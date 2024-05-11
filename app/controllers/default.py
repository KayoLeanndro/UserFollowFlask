from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello world"

@app.route("/teste", defaults ={'nome': None})
@app.route("/teste/<nome>")
def return_name(nome):
    if nome:
        return "Olá, %s!" % nome
    else:
        return "Olá, usuario"
    

app.route("/rotaget", methods=['GET'])
def getreturn():
    return "Oi!"