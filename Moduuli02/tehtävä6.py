"""
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""
import random

random_number1 = random.randint(0,9)
random_number2 = random.randint(0,9)
random_number3 = random.randint(0,9)
koodi1 = str(random_number1) + str(random_number2) + str(random_number3)
print(f"Ensimmäisen numerolukon koodi: {koodi1}")

random_number4 = random.randint(1,6)
random_number5 = random.randint(1,6)
random_number6 = random.randint(1,6)
random_number7 = random.randint(1,6)
koodi2 = str(random_number4) + str(random_number5) + str(random_number6) + str(random_number7)
print(f"Toisen numerolukon koodi: {koodi2}")