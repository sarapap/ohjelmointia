"""
Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
Käyttäjälle on näytettävä pelkkä vitsin teksti.
"""
import requests
import json

hakusana = input("Anna hakusana: ")

pyyntö = "https://api.chucknorris.io/jokes/search?query=" + hakusana
vastaus = requests.get(pyyntö).json()
print(json.dumps(vastaus, indent=2))

