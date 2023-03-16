"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä,
joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
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
        self.hissit[numero-1].siirry_kerrokseen(kohde)
        return

t = Talo(1, 7, 5)
t.aja_hissia(2, 3)

