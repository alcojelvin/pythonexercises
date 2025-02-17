while True:
    number = input("Informe um número: ")

    try:
        result = float(number)
        print (f"O número informado foi: {result}")
        break
    except ValueError:
        print (f"Não foi fornecido um número")
