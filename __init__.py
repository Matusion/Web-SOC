from flask import Flask
from time import sleep
from plc import getLocation


app = Flask(__name__)
global prev
prev = -10000000000     #Nastavý predcháďzajúci polohu na nemožné číslo aby sa poloha zobrazila

@app.route('/') #Zobrazí vebstránku pri zadaní ip:5000/
def site():
    def generate():
        while True:
            location = int(getLocation())   #Získa polohu
            if prev == location:    #Zistí či sa zmenila poloha
                yield ''    #Ak nie pošle naspeť len prázdnu odpoveď
            else: 
                prev = location 
                yield '{}\n'.format(str(location))      #Ak áno tak odošle nové informácie
            sleep(1)    #Počká 1 sekundu a zopauje
    return app.response_class(generate(), mimetype='text/css') 

app.run(debug=False, port=5000, host='0.0.0.0')     #Spustí webstránku