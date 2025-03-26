s=float (input("Digite o valor do salário atual: R$ "))
pa=float(input("Digite a porcentagem de aumento (%): "))
va=s*(pa/ 100)
ns=s+va
print(f"Valor do aumento: R$ {va: 2f}")
print(f"Novo salário: R$ {ns: .2f}")