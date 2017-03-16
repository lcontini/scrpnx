import math

def delta(a, b, c):
       return b ** 2 - 4 * a * c


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


if delta(a, b, c) == 0:
   raiz1 = (-b + math.sqrt(delta(a, b, c))) // (2 * a)
   print("a raiz desta equação é", raiz1)
else:
   if (delta(a, b, c) < 0):
       print("esta equação não possui raízes reais")
   else:
      raiz1 = (-b + math.sqrt(delta(a, b, c))) // (2 * a)
      raiz2 = (-b - math.sqrt(delta(a, b, c))) // (2 * a)
      raizList = [raiz1, raiz2]
      raizList.sort()
      print("as raízes da equação são", raizList[0],"e", raizList[1])


