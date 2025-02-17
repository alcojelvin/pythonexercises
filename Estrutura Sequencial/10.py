while True:
    try:
        c = float(input("Quantos graus celcius estão fazendo? "))
        break
    except ValueError:
        print("Informação inválida")

f = (c * 9/5) + 32

print(f"Em fahrenheit, {c:.0f} C são {f:.0f} F")