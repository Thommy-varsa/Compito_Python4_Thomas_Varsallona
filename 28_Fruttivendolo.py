prezzo_kg = float(input("Inserisci il prezzo per kg di pesche: "))
kg_acquistati = float(input("Inserisci quanti kg di pesche vuoi acquistare: "))
# Calcolare il totale senza sconto
totale = prezzo_kg * kg_acquistati
# Applicare lo sconto se il totale supera i 10 euro
if totale > 10:
    totale *= 0.80  # Applichiamo il 20% di sconto
print(f"Il totale da pagare è: {totale:.2f} euro")