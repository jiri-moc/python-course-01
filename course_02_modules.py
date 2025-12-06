"""
VÝUKOVÝ SKRIPT - MODULY A IMPORT V PYTHONU

Tento skript slouží k vysvětlení:

1) Co je modul a proč modularizovat kód
2) Jak používat existující (standardní) moduly pomocí import
3) Jak navrhovat vlastní moduly (vlastní .py soubory)
4) Různé způsoby importu (import modul, from modul import, alias)
5) Jak oddělit „spustitelný skript“ od „modulu“ pomocí __name__ == "__main__"

POZNÁMKA PRO UČITELE:
- Skript můžete pouštět postupně po blocích.
- Ukázky vlastních modulů jsou uvedeny v komentářích jako návrh rozdělení
  do více souborů (např. soubor kalkulacka.py a soubor main.py).
- Doporučuji během výuky reálně vytvořit tyto soubory s třídou a společně
  je se studenty používat.
"""

# ============================================================
# 1) CO JE MODUL - ZÁKLADNÍ POJEM
# ============================================================

# POZNÁMKA PRO UČITELE:
# Modul = samostatný soubor s Python kódem (např. kalkulacka.py),
# který může obsahovat proměnné, funkce, třídy atd.
# Díky modulům:
# - rozdělujeme kód do logických celků,
# - můžeme opakovaně používat stejné funkce v různých projektech,
# - kód je přehlednější a lépe se udržuje.
#
# Zde nejprve ukážeme použití standardních modulů (math, random),
# protože je žáci mají k dispozici okamžitě.

print("=== 1) Co je modul - ukázka na standardních modulech ===")

import math  # importujeme standardní modul math (součást Pythonu)
import random  # modul pro generování náhodných čísel

# Využití modulu math
cislo = 16
odmocnina = math.sqrt(cislo)  # funkce sqrt z modulu math

print(f"Odmocnina z {cislo} je {odmocnina}")

# Využití modulu random
nahodne_cislo = random.randint(1, 10)  # náhodné celé číslo 1-10
print("Náhodné číslo z intervalu 1-10:", nahodne_cislo)

print()  # prázdný řádek pro přehlednost


# ============================================================
# 2) PROČ MODULARIZOVAT KÓD - MOTIVACE
# ============================================================

# POZNÁMKA PRO UČITELE:
# Můžete se studenty probrat následující scénář:
# - máme „velký“ program (např. hra nebo evidence studentů),
# - v jednom souboru by bylo stovky řádků, těžko se v tom orientuje,
# - proto si rozdělíme kód:
#   - modul pro práci s výpočty,
#   - modul pro práci se soubory,
#   - modul pro uživatelské rozhraní (menu).
#
# Níže je jednoduchý příklad, jak by taková modularizace mohla vypadat.
# V reálném projektu by soubory byly fyzicky oddělené .py soubory.

print("=== 2) Proč modularizovat - koncept rozdělení kódu do souborů ===")

print("Představ si, že máme modul 'kalkulacka.py' a hlavní soubor 'main.py'.")
print("V tomto skriptu to jen ukážeme v komentářích.")

"""
PŘÍKLAD - SOUBOR: kalkulacka.py
===============================

# kalkulacka.py

def secti(a, b):
    return a + b

def odecti(a, b):
    return a - b

def vynasob(a, b):
    return a * b

def vydel(a, b):
    if b == 0:
        raise ValueError("Nulou nelze dělit!")
    return a / b
"""

"""
PŘÍKLAD - SOUBOR: main.py
=========================

# main.py

import kalkulacka  # importujeme vlastní modul

a = 10
b = 5

print("Součet:", kalkulacka.secti(a, b))
print("Rozdíl:", kalkulacka.odecti(a, b))
"""


# ============================================================
# 3) ZÁKLADNÍ ZPŮSOBY IMPORTU
# ============================================================

# POZNÁMKA PRO UČITELE:
# Vysvětlete základní formy importu:
#
# 1) import modul
#    - používáme modul.funkce(...)
# 2) from modul import funkce
#    - voláme přímo funkce(...)
# 3) import modul as alias
#    - zkrácený název, často u dlouhých jmen (např. import numpy as np)
#
# Zápis "from modul import *" je vhodné jen výjimečně (nepřehledné názvy).

print("=== 3) Způsoby importu - praktické ukázky ===")

# 1) import modul - ukázka s math (už importováno výše)
print("Použití 'import math': sqrt =", math.sqrt(25))

# 2) from modul import funkce
from math import ceil, floor  # naimportujeme jen dvě konkrétní funkce

x = 3.7
print("Použití 'from math import ceil, floor':")
print("ceil(3.7) =", ceil(x))    # zaokrouhlení nahoru
print("floor(3.7) =", floor(x))  # zaokrouhlení dolů

# 3) import modul as alias
import random as rnd  # alias "rnd" místo "random"

print("Použití 'import random as rnd':", rnd.randint(1, 5))

print()

# POZNÁMKA PRO UČITELE:
# Nechte studenty:
# - nahradit alias „rnd“ jiným,
# - přidat další importy (např. from random import choice),
# - vysvětlit, proč aliasy u velkých knihoven zjednodušují práci.


# ============================================================
# 4) VYTVOŘENÍ A POUŽITÍ VLASTNÍHO MODULU - SIMULOVANÝ PŘÍKLAD
# ============================================================

# POZNÁMKA PRO UČITELE:
# V této části ukážeme kompletní příklad:
# - modul text_utils.py s funkcemi pro práci s textem,
# - hlavní skript, který modul používá.
#
# V tomto jednom souboru to jen komentujeme, aby studenti viděli
# strukturu. Doporučuji S TŘÍDOU skutečně vytvořit text_utils.py
# a main_text.py a kód si vyzkoušet.

print("=== 4) Tvorba vlastního modulu - koncept text_utils.py + main_text.py ===")

"""
PŘÍKLAD - SOUBOR: text_utils.py
===============================

# text_utils.py

def pocet_slov(text):
    \"\"\"Vrátí počet slov v textu.\"\"\"
    slova = text.split()
    return len(slova)

def nejdelsi_slovo(text):
    \"\"\"Vrátí nejdelší slovo v textu (pokud je text prázdný, vrátí prázdný řetězec).\"\"\"
    slova = text.split()
    if not slova:
        return ""
    return max(slova, key=len)
"""

"""
PŘÍKLAD - SOUBOR: main_text.py
==============================

# main_text.py

import text_utils  # importujeme vlastní modul

text = "Python je skvělý programovací jazyk"

print("Text:", text)
print("Počet slov:", text_utils.pocet_slov(text))
print("Nejdelší slovo:", text_utils.nejdelsi_slovo(text))
"""

print("Tento skript sám tyto soubory nevytváří.")
print("Slouží jako vzor, jak si rozdělit kód do modulů.")
print()


# ============================================================
# 5) __name__ == "__main__" - MODUL vs. SPUSTITELNÝ SKRIPT
# ============================================================

# POZNÁMKA PRO UČITELE:
# Když Python spouští soubor:
# - pokud je soubor spuštěn přímo (python soubor.py), nastaví se __name__ = "__main__"
# - pokud je soubor importován jako modul, __name__ = "název_modulu"
#
# Díky tomu můžeme:
# - mít v souboru funkce, které chceme importovat,
# - a zároveň testovací / demonstrační kód, který se spustí jen při přímém spuštění.
#
# Toto je dobrá praxe pro psaní modulů.

print("=== 5) __name__ == '__main__' - vysvětlení ===")


def ukazka_funkce():
    """Jednoduchá funkce pro demonstraci __name__ == '__main__'."""
    print("Funkce ukazka_funkce byla zavolána.")


# Tato část se spustí jen, když soubor spustíme přímo,
# ale NE když jej importujeme jako modul do jiného skriptu.
if __name__ == "__main__":
    print("Tento blok běží, protože skript je spuštěn přímo.")
    ukazka_funkce()
else:
    # Když by tento soubor byl importován jako modul,
    # studenti mohou vidět, že se tento print NEprovede,
    # protože __name__ pak bude např. 'moje_moduly'
    print("Skript je importován jako modul, blok __main__ se nespouští.")


# POZNÁMKA PRO UČITELE:
# Doporučené cvičení:
# 1) Nechat studenty vytvořit vlastní modul (třeba kalkulacka.py) + hlavní skript.
# 2) Přidat do modulu testovací blok s __name__ == "__main__"
#    a ukázat rozdíl mezi přímým spuštěním a importem.
# 3) Nechat studenty refaktorovat existující „velký“ skript, rozdělit jej
#    do dvou či tří modulů (např. logika hry, vstup/výstup, práce s daty).

# ============================================================
# KONEC SKRIPTU
# ============================================================

print("=== Konec výukového skriptu pro MODULY a IMPORT ===")
