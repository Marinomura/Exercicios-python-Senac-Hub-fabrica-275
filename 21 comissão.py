#Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas.
# #Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre o valor da comissão e o salário final do funcionário.

sal_fixo = float(input("Digite o sálario fixo do funcionário: "))
vendas = float(input("Digite o valor das vendas do funcionáario: "))
comissao = (0.04*vendas)
sal_var = sal_fixo+comissao
print(f"salario fixo {sal_fixo:.2f}")
print(f"valor das vendas {vendas:.2f}")
print(f"valor da comissão {comissao:.2f}")
print(f"salario final {sal_var:.2f}")


