"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
helikopterikenttiä on 15 kappaletta jne.
"""

import mysql.connector
def maakoodi(koodi):
    sql = "SELECT type, count(*) FROM airport"
    sql += " WHERE iso_country in("
    sql += " SELECT iso_country from country"
    sql += " WHERE iso_country='" + koodi + "')"
    sql += " GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    return

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'sarapython',
        password = 'python1',
        autocommit = True
        )

koodi = input("Anna maakoodi: ")
maakoodi(koodi)