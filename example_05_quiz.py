import json
import os

def nacti_otazky(soubor):
    if not os.path.exists(soubor):
        print("Soubor s otázkami neexistuje.")
        return []

    try:
        with open(soubor, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Chyba: poškozený JSON.")
        return []

def uloz_skore(jmeno, skore, soubor="score.json"):
    data = []
    if os.path.exists(soubor):
        try:
            with open(soubor, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            pass

    data.append({"name": jmeno, "score": skore})

    with open(soubor, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def spust_quiz():
    otazky = nacti_otazky("questions.json")
    if not otazky:
        return

    skore = 0

    for o in otazky:
        odp = input(o["q"] + " ")
        if odp.strip().lower() == o["a"].lower():
            print("Správně.")
            skore += 1
        else:
            print(f"Špatně. Správně: {o['a']}")

    print(f"Získal jsi {skore} bodů.")

    jmeno = input("Zadej své jméno pro uložení výsledku: ")
    uloz_skore(jmeno, skore)

spust_quiz()
