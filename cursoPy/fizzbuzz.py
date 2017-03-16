valorNumero = int(input("Digite um numero inteiro: " ))

div3 = valorNumero // 3
div5 = valorNumero // 5

restoDiv3 = valorNumero % 3
restoDiv5 = valorNumero % 5
 

if ((restoDiv3 == 0) and (restoDiv5 == 0)):
   print("FizzBuzz")
else:
   print(valorNumero)
