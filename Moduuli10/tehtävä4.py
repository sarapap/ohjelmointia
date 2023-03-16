"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina
kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on
ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina
tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta
tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
"""
import random
from prettytable import PrettyTable
class Auto:
    def __init__(self, r_tunnus, h_nopeus):
        self.r_tunnus = r_tunnus
        self.h_nopeus = h_nopeus
        self.t_nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        if muutos < 0:
            if self.t_nopeus + muutos >= 0:
                self.t_nopeus += muutos
            else:
                self.t_nopeus = 0
        elif muutos > 0:
            if self.t_nopeus + muutos <= self.h_nopeus:
                self.t_nopeus += muutos
            else:
                self.t_nopeus = self.h_nopeus

    def kulje(self, tunnit):
        self.matka += self.t_nopeus * tunnit

    def tiedot(self):
        return [self.r_tunnus, self.h_nopeus, self.t_nopeus, self.matka]
class Kilpailu:
    def __init__(self, nimi, maara, autot):
        self.nimi = nimi
        self.pituus = maara
        self.autot = []

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)
    def tulosta_tilanne(self):
        taulukko = PrettyTable()
        taulukko.field_names = ["Rekisteritunnus", "Huippunopeus", "Tämänhetkinen nopeus", "Kuljettu matka (km)"]
        for auto in self.autot:
            taulukko.add_row(auto.tiedot())
        print(taulukko)

    def kilpailu_ohi(self):
        kilpailu_ohi = False
        while kilpailu_ohi:
            if self.matka >= 10000:
                kilpailu_ohi = True


autot = []
kilpailu = Kilpailu("Suuri Romuralli", 8000, autot)
for i in range(10):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = "ABC" + str(i+1)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu.tunti_kuluu()
kilpailu.tulosta_tilanne()
kilpailu.kilpailu_ohi()



