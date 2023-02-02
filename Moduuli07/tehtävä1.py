"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
että joulukuu on ensimmäinen talvikuukausi.
"""
vuodenajat = ("kevät", "kesä", "syksy", "talvi")
numero = int(input("Anna kuukauden numero: "))
if numero == 1 or numero == 2 or numero == 12:
    vuodenaika = vuodenajat[3]
elif numero >= 3 and numero <= 5:
    vuodenaika = vuodenajat[0]
elif numero >= 6 and numero <= 8:
    vuodenaika = vuodenajat[1]
else:
    vuodenaika = vuodenajat[2]
print(vuodenaika)