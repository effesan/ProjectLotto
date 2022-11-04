#generare 5 numeri da 1 a 90 casualmente
import random
primo = secondo = terzo = quarto = quinto = 0

#generate a List of 90 numbers from 1 to 90
def extraction():
    return random.randrange(1, 90)

#Sequence of extractions 
primo = extraction()
secondo = extraction()
if secondo != primo:
    terzo = extraction()
if terzo != secondo & terzo != primo:
    quarto = extraction()
if quarto != terzo & quarto != secondo & quarto != primo:
    quinto = extraction()    


print('Extracts: ', primo, ' ,', secondo, ' ,', terzo, ' ,', quarto, ' ,', quinto, ' .')