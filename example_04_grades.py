znamky = {}

def vypocet_prumeru(zlist):
    return sum(zlist) / len(zlist) if zlist else 0

while True:
    print("\n1 = Přidat známku")
    print("2 = Zobrazit průměry")
    print("3 = Konec")

    volba = input("Vyber: ")

    if volba == "1":
        jmeno = input("Jméno studenta: ")
        try:
            znamka = float(input("Známka 1–5: "))
        except ValueError:
            print("Chyba: musí být číslo.")
            continue

        if jmeno not in znamky:
            znamky[jmeno] = []

        znamky[jmeno].append(znamka)
        print("Uloženo.")

    elif volba == "2":
        for student, z in znamky.items():
            prumer = vypocet_prumeru(z)
            print(f"{student}: {z} → průměr {prumer:.2f}")

    elif volba == "3":
        break
    else:
        print("Neplatná volba.")
