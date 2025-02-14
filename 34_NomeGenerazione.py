anno_nascita = int(input("Inserisci il tuo anno di nascita: "))
if anno_nascita < 1946:
    print("Prima dei Boomer")
elif 1946 <= anno_nascita <= 1964:
    print("Boomer")
elif 1965 <= anno_nascita <= 1980:
    print("Generazione X")
elif 1981 <= anno_nascita <= 2000:
    print("Generazione Y (Millennials)")
else:
    print("Generazione Z")