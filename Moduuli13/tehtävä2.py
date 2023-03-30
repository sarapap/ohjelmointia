"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
ja kaupungin JSON-muodossa.
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'sarapython',
        password = 'python1',
        autocommit = True
)

def asema(koodi):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{koodi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    yhteys.close()
    return tulos

@app.route('/kenttä/<icao>')

def kenttä(icao):
    app.config['JSON_SORT_KEYS'] = False
    tiedot = asema(icao)
    lista = []
    for i in tiedot:
        lista.append(i)
    vastaus = {
        "ICAO": icao,
        "Name": lista[0][1],
        "Municipality": lista[0][2]
    }
    return jsonify(vastaus)



if __name__ == '__main__':
    app.run(debug=True, port=3001)
