""""
Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
"""
# kanta * korkeus = a * b

a = int(input("Anna suorakulmion kanta: "))
b = int(input("Anna suorakulmion korkeus: "))
area = a * b
print(f"Suorakulmion pinta-ala on {area} neliömetriä.")
piiri = a + a + b + b
print(f"Suorakulmion piiri on {piiri}.")

