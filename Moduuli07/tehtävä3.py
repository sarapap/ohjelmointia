"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
"""
def lisaa_asema():
    tunnus = input("Anna ICAO-koodi:")
    nimi = input("Anna nimi: ")
    lentoasemat[tunnus] = nimi
    return
def hae_asema():
    tunnus = input("Anna ICAO-koodi: ")
    nimi = lentoasemat[tunnus]
    print(nimi)
    return

lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema", "LHBP" : "Budapest Airport", "EKCH" : "Copenhagen Airport"}

toiminto = -1
while toiminto != 3:
    print("1 = lisää lentoasema")
    print("2 = hae uusi")
    print("3 = lopeta")

    toiminto = int(input("valitse toiminto: "))

    if toiminto == 1:
        lisaa_asema()
    elif toiminto == 2:
        hae_asema()

print("Kiitos, näkemiin.")