"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

"""
vuosiluku = int(input("Anna vuosiluku: "))
if vuosiluku % 4 == 0:
    if vuosiluku % 100 == 0 and vuosiluku % 400 != 0:
        print(f"Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

# Jos vuosi on jaollinen 400:lla, niin vuosi on karkausvuosi.
# Muuten jos vuosi on jaollinen 100:lla, vuosi ei ole karkausvuosi.
# Muuten jos vuosi on jaollinen 4:llä, niin vuosi on karkausvuosi

