import pytest

from result import numero1
from result import numero2
from result import operacao

if operacao == '+':
    print(numero1, " + ",  numero2, " = ", numero1 + numero2)
    

elif operacao == '-':
    print(numero1, " - ",  numero2, " = ", numero1 - numero2)
 
elif operacao == '*':
    print(nuemro1, " * ", numero2, " = ", numero1 * numero2)

elif operacao == '/':
    print(numero1, " / ", numero, " = ", numero1 / numero2)

else:
    print("Operador não foi encontrado .... ")


