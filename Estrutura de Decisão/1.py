while True:
    try:
        a = float(input("Informe o primeiro número: "))
        break
    except ValueError:
        print("Informação inválida")

while True:
    try:
        b = float(input("Informe o segundo número: "))
        break
    except ValueError:
        print("Informação inválida")

if a > b:
    print(f"{a} é maior que {b}")
elif b > a:
    print(f"{b} é maior que {a}")
else:
    print("Os dois valores são iguais")