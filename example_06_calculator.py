# kalkulacka_menu.py

def secti(a, b):
    return a + b

def odecti(a, b):
    return a - b

def vynasob(a, b):
    return a * b

def vydel(a, b):
    if b == 0:
        raise ValueError("Nulou nelze dělit.")
    return a / b

while True:
    print("\n=== KALKULAČKA ===")
    print("1) Sčítání")
    print("2) Odčítání")
    print("3) Násobení")
    print("4) Dělení")
    print("5) Konec")

    volba = input("Vyber možnost: ")

    if volba == "5":
        print("Konec programu.")
        break

    if volba not in {"1", "2", "3", "4"}:
        print("Neplatná volba.")
        continue

    try:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
    except ValueError:
        print("Chyba: musíš zadat číslo.")
        continue

    try:
        if volba == "1":
            vysledek = secti(a, b)
        elif volba == "2":
            vysledek = odecti(a, b)
        elif volba == "3":
            vysledek = vynasob(a, b)
        else:
            vysledek = vydel(a, b)

        print("Výsledek:", vysledek)
    except ValueError as e:
        print("Chyba:", e)
