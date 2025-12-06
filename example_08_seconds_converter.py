# konvertor_casu.py

def sekundy_na_hms(sekundy: int):
    if sekundy < 0:
        raise ValueError("Počet sekund nemůže být záporný.")
    hodiny = sekundy // 3600
    zbytek = sekundy % 3600
    minuty = zbytek // 60
    sekundy = zbytek % 60
    return hodiny, minuty, sekundy

try:
    s = int(input("Zadej počet sekund: "))
    h, m, s2 = sekundy_na_hms(s)
    print(f"{h:02d}:{m:02d}:{s2:02d}")
except ValueError as e:
    print("Chyba:", e)
