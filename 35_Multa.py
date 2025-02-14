velocita_rilevata = float(input("Inserisci la velocità rilevata (km/h): "))
limite_velocita = float(input("Inserisci il limite di velocità (km/h): "))
differenza = velocita_rilevata - limite_velocita
if differenza > 60:
    multa = 500
elif 40 < differenza <= 60:
    multa = 370
elif 10 < differenza <= 40:
    multa = 148
elif 0 < differenza <= 10:
    multa = 36
else:
    multa = 0  
if multa > 0:
    print(f"La multa da pagare è: {multa}€")
else:
    print("Nessuna multa, velocità entro il limite.")