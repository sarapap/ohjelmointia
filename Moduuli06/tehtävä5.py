"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""
def funktio(lista):
    lista_2 = []
    for alkio in lista:
        if alkio % 2 == 0:
            lista_2.append(alkio)
    return lista_2

testi_lista = [1, 18, 23, 2, 4]
print(funktio(testi_lista))
print(testi_lista)