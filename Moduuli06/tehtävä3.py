"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""
def litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

määrä = 0
while määrä >= 0:
    määrä = float(input("Anna gallonamäärä: "))
    if määrä > 0:
        result = litroiksi(määrä)
        print(result)

