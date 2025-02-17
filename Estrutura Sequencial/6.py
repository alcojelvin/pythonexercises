import math

while True:
    try:
        radius = float(input("Qual o valor do raio do círculo? "))
        break
    except ValueError:
        print("Informação inválida")

area = math.pi * radius * 2

print(f"A área do raio {radius} é {area:.2f}")