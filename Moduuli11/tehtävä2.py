"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
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



class Sahkoauto(Auto):
    def __init__(self, r_tunnus, h_nopeus, kapasiteetti):
        self.kapasiteetti = kapasiteetti
        super().__init__(r_tunnus, h_nopeus)


class Polttomoottoriauto(Auto):
    def __init__(self, r_tunnus, h_nopeus, tankki):
        self.tankki = tankki
        super().__init__(r_tunnus, h_nopeus)


s_auto = Sahkoauto("ABC-15", 180, "52.5 kWh")
p_auto = Polttomoottoriauto("ACD-123", 165, "32.3 l")

s_auto.kiihdyta(random.randint(50, 165))
p_auto.kiihdyta(random.randint(50, 165))
s_auto.kulje(3)
p_auto.kulje(3)

# km * tunnit
sähköauto = s_auto.t_nopeus * s_auto.matka
print(f"Kolmen tunnin jälkeen sähköauto on ajanut {sähköauto} km nopeudella {s_auto.t_nopeus} km/h.")
polttomoottoriauto = p_auto.t_nopeus * p_auto.matka
print(f"Kolmen tunnin jälkeen polttomoottoriauto on ajanut {polttomoottoriauto} km nopeudella {p_auto.t_nopeus} km/h.")


