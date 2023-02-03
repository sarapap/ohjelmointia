"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
kunnes saadaan nopan maksimisilmäluku,joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random
def arvo(määrä):
    number = random.randint(1, määrä)
    return number

määrä = int(input("Anna maksimisilmäluku: "))
result = 0
while result != määrä:
    result = arvo(määrä)
    print(result)