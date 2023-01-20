"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
"""
import random
random_number = random.randint(1,10)
numero = int(input("Anna numero: "))
while numero != random_number:
    if numero == random_number:
        print("Oikein")
    elif numero < random_number:
        print("Liian pieni arvaus")
    elif numero > random_number:
        print("Liian suuri arvaus")
    numero = int(input("Anna numero: "))