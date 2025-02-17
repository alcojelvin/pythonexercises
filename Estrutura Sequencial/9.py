while True:
    try:
        f = float(input("Quantos graus F estão fazendo? "))
        break
    except ValueError:
        print("Informação inválida")

c = 5 * ((f-32) / 9)

print(f"Em celcius, {f:.0f} F são {c:.0f} C")