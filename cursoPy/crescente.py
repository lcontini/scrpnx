numeros1 = int(input("Digite o primeiro numeros inteiro: "))
numeros2 = int(input("Digite o segundo numeros inteiro: "))
numeros3 = int(input("Digite o terceiro numeros inteiro: "))

numerosList = numeros1, numeros2, numeros3
#numerosList.sort()

if numerosList[0] < numeros2 and numerosList[1] < numeros3:
   print("crescente")
else:
   #if numerosList[0] > numeros2 and numerosList[1] > numeros3:
   print("não está em ordem crescente")

