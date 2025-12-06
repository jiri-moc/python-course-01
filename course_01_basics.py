"""
VÝUKOVÝ SKRIPT - ZÁKLADY PROGRAMOVÁNÍ V PYTHONU

Tento skript je určen pro výuku studentů, kteří začínají s programováním.
Obsahově pokrývá:

1) Algoritmus - pojem, krokový postup
2) Zápis algoritmu v Pythonu
3) Proměnné a datové typy
4) Podmínky - if / elif / else
5) Cykly - for, break, continue
6) Funkce - definice pomocí def, volání a referencování funkcí

POZNÁMKA PRO UČITELE:
- Skript je koncipován tak, aby se dal projít shora dolů během výkladu.
- V jednotlivých sekcích jsou komentáře pro učitele označené
  "POZNÁMKA PRO UČITELE", můžete je při výkladu zdůraznit nebo doplnit.
- Doporučení: Při výuce pouštějte jen části skriptu a nechte studenty
  některé věci doplnit / upravit.
"""

# ============================================================
# 1) ALGORITMUS - POJEM A KROKOVÝ POSTUP
# ============================================================

# POZNÁMKA PRO UČITELE:
# Algoritmus = přesný, konečný, srozumitelný postup, jak vyřešit problém.
# Můžete použít analogii s kuchařským receptem (jasné kroky v pořadí).
# Níže je příklad algoritmu na výpočet průměru tří čísel.

# Nejprve algoritmus slovně (v komentáři):
# 1. Zeptej se uživatele na první číslo.
# 2. Zeptej se uživatele na druhé číslo.
# 3. Zeptej se uživatele na třetí číslo.
# 4. Sečti všechny tři hodnoty.
# 5. Součet vyděl počtem hodnot (3).
# 6. Výsledek zobraz uživateli.

print("=== 1) Algoritmus - příklad: výpočet průměru tří čísel ===")

# Zde stejný algoritmus zapsaný v Pythonu:
a = 10  # pro jednoduchost používáme přímo čísla, později lze nahradit input()
b = 20
c = 30

soucet = a + b + c
prumer = soucet / 3

print("Čísla:", a, b, c)
print("Součet:", soucet)
print("Průměr:", prumer)
print()  # prázdný řádek pro přehlednost


# ============================================================
# 2) ZÁPIS ALGORITMU V PYTHONU - STRUKTURA PROGRAMU
# ============================================================

# POZNÁMKA PRO UČITELE:
# Vysvětlete, že program je jen "přeložený algoritmus" do formálního jazyka.
# Důležité je pořadí příkazů a jejich správná syntaxe (zápis).

print("=== 2) Zápis algoritmu v Pythonu - jednoduchý postup ===")

# Příklad algoritmu: Zjistit, zda je člověk plnoletý.

# Algoritmus slovně:
# 1. Zeptej se na věk.
# 2. Pokud je věk >= 18, vypiš 'Jsi plnoletý.'
# 3. Jinak vypiš 'Ještě nejsi plnoletý.'

vek = 17  # zde je pro ukázku pevně daná hodnota

if vek >= 18:
    print("Jsi plnoletý.")
else:
    print("Ještě nejsi plnoletý.")

print()


# ============================================================
# 3) PROMĚNNÉ A ZÁKLADNÍ DATOVÉ TYPY
# ============================================================

# POZNÁMKA PRO UČITELE:
# Proměnná = pojmenované "místo v paměti", kde držíme hodnotu.
# V Pythonu není nutné dopředu psát typ, ale typ existuje (int, float, str, bool, ...).
# Ukázka základních typů a práce s nimi.

print("=== 3) Proměnné a datové typy ===")

# Celé číslo (int)
vek = 25
print("Věk (int):", vek, "| typ:", type(vek))

# Desetinné číslo (float)
teplota = 22.5
print("Teplota (float):", teplota, "| typ:", type(teplota))

# Řetězec (string, str)
jmeno = "Anna"
print("Jméno (str):", jmeno, "| typ:", type(jmeno))

# Logická hodnota (bool)
plnolety = True
print("Plnoletý (bool):", plnolety, "| typ:", type(plnolety))

# Seznam (list) - kolekce hodnot v hranatých závorkách
znamky = [1, 2, 1, 3]
print("Známky (list):", znamky, "| typ:", type(znamky))

# Slovník (dict) - páry klíč: hodnota ve složených závorkách
student = {
    "jmeno": "Petr",
    "vek": 19,
    "prumer": 1.7
}
print("Student (dict):", student, "| typ:", type(student))

print()

# POZNÁMKA PRO UČITELE:
# Můžete nechat studenty:
# - přidávat nové proměnné,
# - měnit hodnoty,
# - zkoušet funkci type() na různé objekty.


# ============================================================
# 4) PODMÍNKY - IF / ELIF / ELSE
# ============================================================

# POZNÁMKA PRO UČITELE:
# Struktura:
# if podmínka:
#     blok kódu
# elif jiná_podmínka:
#     blok kódu
# else:
#     blok kódu
#
# Zdůrazněte odsazení (4 mezery nebo tab), Python na něm závisí.

print("=== 4) Podmínky - if / elif / else ===")

cislo = 0

if cislo > 0:
    print("Číslo je kladné.")
elif cislo < 0:
    print("Číslo je záporné.")
else:
    print("Číslo je nula.")

# Další příklad: klasifikace známky.
znamka = 2

if znamka == 1:
    print("Výborný.")
elif znamka == 2:
    print("Chvalitebný.")
elif znamka == 3:
    print("Dobrý.")
elif znamka == 4:
    print("Dostatečný.")
elif znamka == 5:
    print("Nedostatečný.")
else:
    print("Neplatná známka.")

print()

# POZNÁMKA PRO UČITELE:
# Můžete se studenty diskutovat:
# - jak se liší '==' (porovnání) a '=' (přiřazení),
# - jak zapsat složitější podmínky: and, or, not.


# ============================================================
# 5) CYKLY - FOR, BREAK, CONTINUE
# ============================================================

# POZNÁMKA PRO UČITELE:
# Cyklus = opakování nějaké části kódu.
# for se hodí, když předem víme, kolikrát iterujeme (nebo jdeme přes kolekci).
# break = předčasně ukončí cyklus,
# continue = přeskočí zbytek aktuální iterace a pokračuje další.

print("=== 5) Cykly - for, break, continue ===")

print("Příklad: výpis čísel od 1 do 5:")

for i in range(1, 6):  # range(1,6) generuje 1,2,3,4,5
    print(i)

print()

# Příklad s break:
print("Příklad: hledání prvního čísla většího než 10:")

cisla = [3, 7, 10, 11, 15, 2]

for c in cisla:
    if c > 10:
        print("Našel jsem číslo větší než 10:", c)
        break  # skončíme, dál už nehledáme

print()

# Příklad s continue:
print("Příklad: tisk jen sudých čísel od 1 do 10:")

for x in range(1, 11):
    if x % 2 != 0:  # pokud je x liché
        continue    # přeskoč zbytek a běž na další číslo
    print("Sudé číslo:", x)

print()

# POZNÁMKA PRO UČITELE:
# Nechte studenty:
# - změnit rozsah range(),
# - zkusit odstranění/break/continue a pozorovat změnu chování.


# ============================================================
# 6) FUNKCE - DEF, PARAMETRY, NÁVRATOVÁ HODNOTA, REFERENCE
# ============================================================

# POZNÁMKA PRO UČITELE:
# Funkce = pojmenovaný blok kódu, který můžeme opakovaně použít.
# def jmeno_funkce(parametry):
#     tělo funkce
#     return hodnota
#
# Ukažte:
# - volání funkce (jmeno_funkce()),
# - parametry,
# - návratovou hodnotu,
# - že funkce je také "hodnota" (lze ji uložit do proměnné).

print("=== 6) Funkce - definice a volání ===")


def secti(a, b):
    """Vrátí součet dvou čísel a + b."""
    return a + b


def pozdrav(jmeno):
    """Vypíše pozdrav pro dané jméno."""
    print("Ahoj,", jmeno)


# Volání funkcí:
vysledek = secti(5, 7)
print("Výsledek funkce secti(5, 7):", vysledek)

pozdrav("Marie")

print()


# Příklad funkce, která vypočítá průměr seznamu čísel:
def prumer_cisel(cisla):
    """Vrátí průměr všech čísel v seznamu cisla."""
    if not cisla:
        return 0  # ochrana před dělením nulou
    return sum(cisla) / len(cisla)


znamky = [1, 2, 2, 1, 3]
print("Známky:", znamky)
print("Průměr známek:", prumer_cisel(znamky))

print()


# FUNKCE JAKO HODNOTY - REFERENCOVÁNÍ FUNKCE
# POZNÁMKA PRO UČITELE:
# Ukázat, že funkci můžeme uložit do proměnné a zavolat přes ni - studentskou řečí:
# "funkce je taky 'věc v proměnné'".

def vynasob_dvema(x):
    return x * 2


def aplikuj_na_seznam(funkce, data):
    """Aplikuje funkci 'funkce' na každý prvek seznamu 'data' a vrátí nový seznam."""
    vysledky = []
    for prvek in data:
        vysledky.append(funkce(prvek))
    return vysledky


cisla = [1, 2, 3, 4]

# Zde předáváme funkci vynasob_dvema jako parametr (bez závorek!)
vysledek = aplikuj_na_seznam(vynasob_dvema, cisla)

print("Původní seznam:", cisla)
print("Po aplikaci funkce vynasob_dvema:", vysledek)

print()

# POZNÁMKA PRO UČITELE:
# Tady lze ukázat:
# - rozdíl mezi vynasob_dvema (reference na funkci) vs. vynasob_dvema(5) (výsledek volání),
# - základní princip funkcionálního programování (funkce jako argument).


# ============================================================
# KONEC SKRIPTU
# ============================================================

print("=== Konec výukového skriptu ===")

# POZNÁMKA PRO UČITELE:
# Návrhy na cvičení:
# 1) Nechat studenty napsat vlastní funkci na výpočet obvodu obdélníku.
# 2) Nechat je upravit příklady s podmínkami (např. více kategorií věku).
# 3) Nechat je doplnit vlastní cyklus, který hledá největší číslo v seznamu.
