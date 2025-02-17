while True:
    try:
        hour_wage = float(input("Qual o valor recebido por hora em R$? "))
        break
    except ValueError:
        print("Informação inválida")

while True:
    try:
        work_days = float(input("Número de horas trabalhadas? "))
        break
    except ValueError:
        print("Informação inválida")

salarie = hour_wage * work_days

print(f"O seu salário será de R$ {salarie:.2f}")