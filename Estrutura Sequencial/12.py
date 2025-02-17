while True:
    try:
        height = float(input("Informe a áltura do indivíduo: "))
        break
    except ValueError:
        print("Informação inválida")

imc = ( 72.7 * height) - 58

print(f"O peso ideal do indivíduo seria {imc:.1f}")