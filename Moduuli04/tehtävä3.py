"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
pienin = 0
suurin = 0
while True:
    luku = input("Anna luku: ")
    if luku == "":
        print(f"Pienin luku {pienin} ja suurin luku {suurin}.")
        break
    else:
        luku = int(luku)
        if luku < pienin:
            pienin = luku
        elif luku > suurin:
            suurin = luku
