import math

coverage_per_liter = 6
liters_per_can = 18
price_per_can = 80
liters_per_gallon = 3.6
price_per_gallon = 25
easy = 0.10

while True:
    try:
        area = float(input("Informe o tamanho da área a ser pintada em metro quadrado: "))
        break
    except ValueError:
        print("Informação inválida")

liters_needed = (area / coverage_per_liter) * (1 + easy)


cans_needed = math.ceil(liters_needed / liters_per_can)
price_can = cans_needed * price_per_can

gallons_needed = math.ceil(liters_needed / liters_per_gallon)
price_gallon = gallons_needed * price_per_gallon

mixed_cans = math.floor(liters_needed / liters_per_can)
remaining = liters_needed - (mixed_cans * liters_per_can)
mixed_gallons = math.ceil(remaining / liters_per_gallon)
mixed_price = (mixed_cans * price_per_can) + (mixed_gallons * price_per_gallon)

print(f"\nSituação 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas necessárias: {cans_needed}")
print(f"Preço total: R$ {price_can:.2f}")

print(f"\nSituação 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões necessários: {gallons_needed}")
print(f"Preço total: R$ {price_gallon:.2f}")

print(f"\nSituação 3: Misturar latas e galões (menor desperdício)")
print(f"Quantidade de latas necessárias: {mixed_cans}")
print(f"Quantidade de galões necessários: {mixed_gallons}")
print(f"Preço total: R$ {mixed_price:.2f}")
