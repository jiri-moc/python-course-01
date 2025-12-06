# generator_jmen.py

import random

KRESTNI = ["Jan", "Petr", "Jakub", "Lucie", "Anna", "Eva"]
PRIJMENI = ["Novák", "Svoboda", "Dvořák", "Procházka", "Horák", "Kučera"]

def vygeneruj_jmeno():
    return random.choice(KRESTNI) + " " + random.choice(PRIJMENI)

try:
    pocet = int(input("Kolik jmen vygenerovat? "))
except ValueError:
    print("Neplatný vstup, generuji 5 jmen.")
    pocet = 5

for _ in range(pocet):
    print(vygeneruj_jmeno())
