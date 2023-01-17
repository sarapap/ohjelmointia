"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""
kuha_alamittainen = float(input("Anna kuhan pituus: "))
if kuha_alamittainen < 37:
    puuttuvat = 37 - kuha_alamittainen
    print(f"Kuha on {puuttuvat} cm liian lyhyt, laske kuha takaisin järveen.")
