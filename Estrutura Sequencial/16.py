coverage_per_liter = 3
liters_per_can = 18
price_per_can = 80

area = float(input("Informe o tamanho da área a ser pintada em metro quadrado: "))

liters_required = area / coverage_per_liter

import math
cans_needed = math.ceil(liters_required / liters_per_can)

total_price =  price_per_can * cans_needed

print(f"Quantidade de latas necessárias: {cans_needed}\nValor total da compra: R$ {total_price:.2f}")