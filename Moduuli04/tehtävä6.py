# arvotaan arvoja -1 ja 1 välillä
# arvot x ja y (x, y)
# epäyhtälö = x^2+y^2 < 1 (ympyrän sisällä jos epäyhtälö toteutuu)
import random
N = 100000
määrä = 0
n = 0
while määrä < N:
    määrä = määrä + 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"saatu piste {x}, {y}")
    # onko piste ympyrän sisällä
    if x**2+y**2 < 1:
        print("Piste on sisällä.")
        n = n + 1
print(f"Pisteitä arvottu yhteensä {määrä}, joista {n} kappaletta on ympyrän sisällä")
# lasketaan piin likiarvo
likiarvo = 4 * n / N
print(likiarvo)
