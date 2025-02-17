def invalid_information():
    return "Informação inválida"

while True:
    try:
        numInt1 = int(input("Informe o primeiro núnmero inteiro: "))
        break
    except ValueError:
        print(invalid_information())

while True: 
    try:
        numInt2 = int(input("Informe o segundo número inteiro: "))
        break
    except ValueError:
        print(invalid_information())

while True:
    try:
        numReal = float(input("Informe um número real: "))
        break
    except ValueError:
        print(invalid_information())

a = ( numInt1 * 2 ) + ( numInt2 / 2 )

b = ( numInt1 * 3 ) + numReal

c = numReal ** 3

print(f"O produto do dobro do primeiro número com metade do segundo é {a}.\nA soma do triplo do primeiro número com o terceiro é {b}.\nO terceiro número elevado ao cubo é {c}.")