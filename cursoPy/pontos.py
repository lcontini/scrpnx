import math

valorx1 = int(input("Digite o valor do primeiro numero inteiro: "))
valorx2 = int(input("Digite o valor do segundo numero inteiro: "))
valory1 = int(input("Digite o valor do terceiro numero inteiro: "))
valory2 = int(input("Digite o valor do quarto numero inteiro: "))

#distancia = ((valorx1 + valorx2) ** 2) + ((valory1 + valory2) **2)
distancia = (valorx1 + valorx2) - (valory1 + valory2)

if (distancia >= 10):
   print("Longe")
else:
   if (distancia < 10):
       print ("Perto")

