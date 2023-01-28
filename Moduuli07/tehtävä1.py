"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
että joulukuu on ensimmäinen talvikuukausi.
"""
kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "syyskyy", "lokakuu", "marraskuu", "joulukuu")
numero = int(input("Anna kuukauden numero: "))
vuodenaika = kuukaudet[numero-1]
print(f"{numero}. kuukausi on {vuodenaika}.")



