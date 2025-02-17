while True:
    try:
        weight = float(input("Informe o peso dos peixes pescados: "))
        break
    except ValueError:
        print("Informação inválida")

weight_limit = 50

if weight > weight_limit:
    additional_weight = weight - 50
    fine = additional_weight * 4.00
    print(f"O peso adicional é de {additional_weight} KG, que implica em uma multa de R$ {fine:.2f}")
else:
    print(f"Considerando que {weight} KG está de acordo com o peso limite estabelecido pelo regulamento de pesca do Estado de São Paulo, não haverá multa")
