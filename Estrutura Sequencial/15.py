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
ir = salarie * 0.11
inss = salarie * 0.08
union = salarie * 0.05
remnant = salarie - inss - union

print(f"+ Salário Bruto : R$ {salarie:.2f}\n- IR (11%) : R$ {ir:.2f}\n- INSS (8%) : R$ {inss:.2f}\n- Sindicato (5%) : R$ {union:.2f}\n= Salário Líquido : R$ {remnant:.2f}")
