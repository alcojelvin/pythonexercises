def return_error():
    return "Não foi informado um número"

while True:
    try:
        num1 = float(input("Informe a primeira nota bimestral: "))
        break
    except ValueError:
        print(return_error())

while True:
    try:
        num2 = float(input("Informe a segunda nota bimestral: "))
        break
    except ValueError:
        print(return_error())

while True:
    try:
        num3 = float(input("Informe a terceira nota bimestral: "))
        break
    except ValueError:
        print(return_error())

while True:
    try:
        num4 = float(input("Informe a quarta nota bimestral: "))
        break
    except ValueError:
        print(return_error())

print(f"A média das notas é: {(num1 + num2 + num3 + num4) / 4}")
