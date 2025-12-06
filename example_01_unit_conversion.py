def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def km_to_mi(km):
    return km * 0.621371

def mi_to_km(mi):
    return mi / 0.621371

print("PŘEVODNÍK JEDNOTEK")
print("1 = °C → °F")
print("2 = °F → °C")
print("3 = km → mi")
print("4 = mi → km")

volba = input("Vyber možnost: ")

try:
    if volba == "1":
        c = float(input("Zadej °C: "))
        print(f"{c} °C = {c_to_f(c):.2f} °F")
    elif volba == "2":
        f = float(input("Zadej °F: "))
        print(f"{f} °F = {f_to_c(f):.2f} °C")
    elif volba == "3":
        km = float(input("Zadej kilometry: "))
        print(f"{km} km = {km_to_mi(km):.2f} mi")
    elif volba == "4":
        mi = float(input("Zadej míle: "))
        print(f"{mi} mi = {mi_to_km(mi):.2f} km")
    else:
        print("Neplatná volba.")
except ValueError:
    print("Chyba: zadaná hodnota není číslo.")
