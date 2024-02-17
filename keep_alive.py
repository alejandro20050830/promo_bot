from flask import Flask,render_template
from threading import Thread
import requests
import time

def cargar_pagina(url='https://py-xfxl.onrender.com'):
    

    while True:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            
            print(respuesta.text)
        else:
            
            print(respuesta.text)
        
        
        time.sleep(30)



app=Flask(__name__)

@app.route('/')

def index():
    return "alive"

def run():
    app.run(host='0.0.0.0',port=8080)
    
def keep_alive():
   
    t=Thread(target=run)
    t1=Thread(target=cargar_pagina)
    t.start()  
    t1.start()
    
