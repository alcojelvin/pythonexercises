while True:
    try:
        lado = float(input("Informe o valor do lado do quadrado: "))
        break
    except ValueError:
        print("Informação inválida")

area = lado ** 2

print (f"O dobro do valor da área do quadro é {area * 2}")