"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain
samassa järjestyksessä kuin ne syötettiin.
käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
"""
lista = []
for luku in range(5):
    kaupungit = input("Kirjoita kaupungin nimi: ")
    lista.append(kaupungit)
for kaupungit in lista:
    print(kaupungit)