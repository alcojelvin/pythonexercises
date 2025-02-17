while True:
    try:
        metros = float(input("Informe o valor em metros para conversão: "))
        break
    except ValueError:
        print("Inforrmação inválida")
    
centimetros = metros * 100

print(f"{metros} são {int(centimetros)} centímetros")