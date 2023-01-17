"""
Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.
"""

leiviska = float(input("Anna leiviskat: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

massa = (leiviska * 20) + naula
massa_2 = (massa * 32) + luoti

xg = int(xg)
xkg = int(kg)

xg = round({massa_2} * 13.3)
xkg = round({xg} // 1000)

print(f"Massa nykymittojen mukaan: ")
print(f"{xkg} kilogrammaa ja {xg} grammaa.")