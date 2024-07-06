from flask import Flask, render_template
from threading import Thread

# from db_tools import*
import requests
import time
from datetime import datetime

json_logs = {"infos": {}}


def print_to_web(text):
    print(text)
    fecha_actual = datetime.now()
    formato_personalizado = fecha_actual.strftime("%d/%m/%Y %H:%M:%S.%f")
    json_logs["infos"][str(formato_personalizado)] = str(text)


def cargar_pagina(url="https://promo-bot-e3nc.onrender.com"):
    while True:
        time.sleep(30)
        try:
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                print(respuesta.text)
            else:
                print(respuesta.text)

        except:
            pass


app = Flask(__name__)


@app.route("/")
def index():
    return json_logs


def run():

    app.run(host="0.0.0.0", port=8080)


# server_py()


def keep_alive():
    # t2 = Thread(target=server_py)
    # t2.start()
    t = Thread(target=run)

    t1 = Thread(target=cargar_pagina)
    t.start()

    t1.start()
