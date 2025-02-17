while True:
    try:
        num1 = int(input("Informe o primeiro número: "))
        break
    except ValueError:
        print("Preciso seja um número inteiro")
while True:
    try:
        num2 = int(input("Inforrme o segundo número: "))
        break
    except ValueError: 
        print("Voce não entendeu ainda?")

print (f"A soma dos valores informados é {num1 + num2}")