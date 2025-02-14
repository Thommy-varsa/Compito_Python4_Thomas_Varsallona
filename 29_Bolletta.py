# Input
consumo = float(input("Inserisci il consumo di gas in metri cubi: "))
# Quota fissa
quota_fissa = 20
# Calcolare il costo in base al consumo
if consumo <= 500:
    totale = quota_fissa + consumo * 0.575
else:
    primi_500 = 500 * 0.575
    eccedente = (consumo - 500) * 0.783
    totale = quota_fissa + primi_500 + eccedente
# Stampa del risultato
print(f"Il totale della bolletta è:",totale)