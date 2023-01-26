"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla
sort-metodille argumentiksi reverse=True.
"""
luku = input("Anna luku (tyhjä lopettaa): ")
lista = []
while luku != "":
    luvut = int(luku)
    lista.append(luvut)
    luku = input("Anna luku (tyhjä lopettaa): ")

lista.sort()
lista.reverse()

suurin = lista[:5]
print("Viisi suurinta suuruusjärjestyksessä suurimmasta alkaen: ")
print(suurin)



