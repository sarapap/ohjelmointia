"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""
import mysql.connector
def asema(koodi):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + koodi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(f"Lentokentän nimi on {i[0]} ja ICAO-koodi on {i[1]}.")
    return

# Pääohjelma
yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'sarapython',
        password = 'python1',
        autocommit = True
        )

koodi = input("Anna ICAO-koodi: ")
asema(koodi)