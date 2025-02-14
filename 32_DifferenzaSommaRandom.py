import random
numero1=random.randint(0,10)
numero2=random.randint(0,10)
prodotto=numero1*numero2
if prodotto > 20:
    risultato= abs(numero1-numero2)
else:
    risultato=numero1+numero2
print("numero1:",numero1)
print("numero2:",numero2)
print("risultato",risultato)
print("prodotto:",prodotto)