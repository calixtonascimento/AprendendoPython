# Escreva um programa que resolva uma equação de segundo grau.

# Desnecessário caso, na linha 20, seja usado: raiz_delta = delta**(1/2)
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

if delta < 0:  # Nenhuma raiz real
    print("Não existe raiz quadrada de número negativo")

elif delta == 0:  # Uma raiz real
    x = (-b)/(2*a)

    print("x = ", x)

elif delta > 0:  # Duas raízes reais
    # Pode ser substituído por: raiz_delta = delta**(1/2)
    raiz_delta = math.sqrt(delta)

    x1 = (-b + raiz_delta)/(2*a)
    x2 = (-b - raiz_delta)/(2*a)

    print("x1 = ", x1)
    print("x2 = ", x2)
