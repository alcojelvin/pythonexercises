while True:
    try: 
        height_input = input("Informe a altura do indivíduo: ").strip()

        if "." in height_input:
            height = float(height_input)
        else:
            height = float(height_input) / 100
        break
    except ValueError:
        print("Informação inválida")

while True:
    gender = input("Qual o genero do indíviduo (F/M): ").strip().lower()

    if gender == "f" or gender == "m":
        break
    else:
        print("Informação inválida")

if gender == "f":
    fimc = ( 62.1* height) - 44.7
    print(f"O peso ideal do indivíduo é {fimc:.1f}")
elif gender == "m":
    mimc = ( 72.7 * height ) - 58
    print(f"O peso ideal do indivíduo é {mimc:.1f}")
    