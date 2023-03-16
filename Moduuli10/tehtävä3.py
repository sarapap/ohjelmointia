"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen.
Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
"""
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylos(self):
        self.kerros = self.kerros + 1
        return

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        return

    def siirry_kerrokseen(self, kohde):
        while kohde > self.kerros:
            self.kerros_ylos()
        while kohde < self.kerros:
            self.kerros_alas()
        print(f"Hissi on kerroksessa {self.kerros}")
        return

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(lukumaara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)
    def aja_hissia(self, numero, kohde):
        self.hissit[numero].siirry_kerrokseen(kohde)
        return

    def palohalytys(self):
        for i in range(len(self.hissit)):
            self.aja_hissia(i, self.alin_kerros)
        return

t = Talo(1, 7, 5)
t.aja_hissia(2, 5)
t.palohalytys()

