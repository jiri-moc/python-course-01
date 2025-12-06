def je_palindrom(slovo):
    sl = slovo.lower()
    return sl == sl[::-1]

text = input("Zadej text: ").strip()

slova = text.split()
pocet = len(slova)

nejdelsi = max(slova, key=len) if slova else ""

palindromy = [s for s in slova if je_palindrom(s)]

print(f"Počet slov: {pocet}")
print(f"Nejdelší slovo: {nejdelsi}")
print("Palindromy:", palindromy)
