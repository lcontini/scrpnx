num = int(input("Digite um numero inteiro positivo "))

primo = True
div = 2

while div < num and primo:
    if num % div == 0:
         primo = False
    div += 1

if primo and num != 1:
    print("primo")
else:
    print("não primo")



