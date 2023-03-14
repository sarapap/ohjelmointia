"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

- Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
- Tämä tehdään kutsumalla kiihdytä-metodia.
- Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
import random
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

kerrat = 0
autot = []
while kerrat < 10:
    numero = 1
    huippunopeus = random.randint(100, 200)
    auto = Auto({f"ABC-{numero}"}, huippunopeus)
    autot.append(auto)
    numero += 1
    kerrat += 1

for auto in autot:
    while auto.matka <= 10000:
        auto.kulje(1)
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)

for auto in autot:
    print(auto)



