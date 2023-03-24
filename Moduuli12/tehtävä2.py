"""
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi.
Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
"""
import requests

paikkakunta = input("Anna paikkakunta: ")

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + paikkakunta + "&units=metric&lang=fi&appid=e45c83f47ddff50fc5bc40aa44d6ebe9"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        tila = json_vastaus.get('weather')
        kuvaus = tila[0]['description']
        aste = json_vastaus.get('main')
        asteet = aste['temp']
        print(f"Säätila kohteessa: {kuvaus}, lämpötila {asteet}°C")
except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")



