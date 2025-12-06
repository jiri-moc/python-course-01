# generator_hesel.py

import random
import string

def vygeneruj_heslo(delka=12):
    if delka < 4:
        raise ValueError("Délka hesla musí být minimálně 4 znaky.")

    male = string.ascii_lowercase
    velke = string.ascii_uppercase
    cislice = string.digits
    special = "!@#$%^&*()-_=+"

    # Zajistíme, že heslo bude obsahovat aspoň jeden znak z každé skupiny
    heslo_znaky = [
        random.choice(male),
        random.choice(velke),
        random.choice(cislice),
        random.choice(special),
    ]

    vsechny_znaky = male + velke + cislice + special

    while len(heslo_znaky) < delka:
        heslo_znaky.append(random.choice(vsechny_znaky))

    random.shuffle(heslo_znaky)
    return "".join(heslo_znaky)

try:
    delka = int(input("Zadej délku hesla: "))
    heslo = vygeneruj_heslo(delka)
    print("Vygenerované heslo:", heslo)
except ValueError as e:
    print("Chyba:", e)
