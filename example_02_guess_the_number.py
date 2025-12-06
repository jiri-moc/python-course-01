import random

tajne = random.randint(1, 100)
pokusy = 0

print("Hádej číslo od 1 do 100.")

while True:
    try:
        tip = int(input("Tvůj tip: "))
    except ValueError:
        print("Musíš zadat číslo.")
        continue

    pokusy += 1

    if tip < tajne:
        print("Moc malé.")
    elif tip > tajne:
        print("Moc velké.")
    else:
        print(f"Správně! Uhodl jsi za {pokusy} pokusů.")
        break
