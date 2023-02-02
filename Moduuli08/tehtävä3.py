"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.
"""
import mysql.connector
from geopy import distance
def lentokenttä(koodi):
    sql = "SELECT longitude_deg, latitude_deg  FROM airport"
    sql += " WHERE ident='" + koodi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'sarapython',
        password = 'python1',
        autocommit = True
        )

koodi1 = input("Anna ICAO-koodi: ")
koodi2 = input("Anna toinen ICAO-koodi: ")

lentokenttä1 = lentokenttä(koodi1)
lentokenttä2 = lentokenttä(koodi2)

print(f"Lentokenttien välinen etäisyys on: {distance.distance(lentokenttä1, lentokenttä2).kilometers} km")
