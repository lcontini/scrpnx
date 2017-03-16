numeroSalvo = numero = int(input("Digite um numero: "))

anterior = numero % 10
numero = numero // 10;

numerosIguais = False
valor = 0

while numero > 0 and not numerosIguais:
      atual = numero % 10
      if atual == anterior:
         numerosIguais = True
      else:
         valor += 1
      anterior = atual
      numero = numero // 10

if numerosIguais:
   print("sim")
else:
   print("não")
