"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.
"""
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

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.r_tunnus}, huippunopeus on {auto.h_nopeus} km/h, tämänhetkinen nopeus on {auto.t_nopeus} km/h ja kuljettu matka on {auto.matka} km.")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton nopeus on {auto.t_nopeus} km/h")

auto.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto.t_nopeus} km/h.")