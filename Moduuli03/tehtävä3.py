"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

"""
sukupuoli = input("Anna käyttäjän biologinen sukupuoli (N/M): ")
arvo = int(input("Anna käyttäjän hemoglobiiniarvo: "))

if sukupuoli == "N":
    if arvo > 175:
        print(f"Hemoglobiiniarvosi on korkea")
    elif arvo >= 117:
        print(f"Hemoglobiiniarvosi on normaali")
    else:
        print(f"Hemoglobiiniarvosi on alhainen")

if sukupuoli == "M":
    if arvo > 195:
        print(f"Hemoglobiiniarvosi on korkea")
    elif arvo >= 134:
        print(f"Hemoglobiiniarvosi on normaali")
    else:
        print(f"Hemoglobiiniarvosi on alhainen")
