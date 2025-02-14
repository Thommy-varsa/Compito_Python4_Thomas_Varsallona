litri = float(input("Inserisci il numero di litri di benzina: "))
prezzo_per_litro = 1.76
totale = litri * prezzo_per_litro
if totale > 60:
    totale *= 0.95
print(f"Il totale da pagare è: {totale:.2f}€")