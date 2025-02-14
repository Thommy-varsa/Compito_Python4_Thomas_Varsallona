prezzo = float(input("Inserisci il prezzo del biglietto: "))
numero = int(input("Inserisci il numero di biglietti acquistati: "))
# Calcoliamo i biglietti omaggio
biglietti_pagati = numero - (numero // 20)  # Ogni 20 biglietti acquistati, uno è omaggio
totale = biglietti_pagati * prezzo
print("Il totale da pagare è:", totale)