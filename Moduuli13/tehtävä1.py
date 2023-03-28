"""
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
"""
from flask import Flask, request
app = Flask(__name__)


def isprime(luku):
    if luku < 2:
        return False
    for i in range(2, luku):
        if luku % i == 0:
            return False
    return True


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    return {
        "Number": luku,
        "isPrime": isprime(luku)
    }


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

