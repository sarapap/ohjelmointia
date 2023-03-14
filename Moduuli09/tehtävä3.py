"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran
kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
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

    def kulje(self, tunnit):
        self.matka += self.t_nopeus * tunnit

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.r_tunnus}, huippunopeus on {auto.h_nopeus} km/h, tämänhetkinen nopeus on {auto.t_nopeus} km/h ja kuljettu matka on {auto.matka} km.")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton nopeus on {auto.t_nopeus} km/h")

auto.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto.t_nopeus} km/h.")