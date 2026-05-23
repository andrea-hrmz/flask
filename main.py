from flask import Flask
import random

app = Flask(__name__)
facts_list = [
    "ve a tocar pasto",
    "Mientras que twiteas migajeando a hahadit_ el que te gustaba en la primaria es feliz con otra, suelta el celu",
    "Duermes 5 horas y pasas 12 en tiktok",
    "Por lo menos podrías estar haciendo algo de provecho con la pantalla",
    "Se te van a caer los ojos"
]

coin_list = [
    "Te salió cara",
    "Te salió cruz"
]

img_list = [
    '<img src="/static/img_1.jpg">',
    '<img src="/static/img_2.jpg">',
    '<img src="/static/img_3.jpg">',
    '<img src="/static/img_4.jpg">',
    '<img src="/static/img_5.jpg">',
    '<img src="/static/img_6.jpg">',
    '<img src="/static/img_7.jpg">'
]

@app.route("/")
def home():
    return'<h1>Adicción a la tecnología</h1><a href="/facts">¡Ver un dato aleatorio!</a>''<a href="/coin">!Tira una moneda porque sí!</a>''<a href="/img">!Genera una imagen con mucha aura!</a>'

@app.route("/facts")
def facts():
    return f'<p>{random.choice(facts_list)}</p><a href="/">Volver a la página principal</a>''<a href="/facts">!Ve otro dato!</a>'

@app.route("/coin")
def coin():
    return f'<p>{random.choice(coin_list)}</p><a href="/">Volver a la página principal</a>' '<a href="/coin">!Vuelve a tirar!</a>'

@app.route("/img")
def img():
    return f'<p>{random.choice(img_list)}</p><a href="/">Volver a la página principal</a>' '<a href="/img">!Genera otra imagen!</a>'

app.run(debug=True)