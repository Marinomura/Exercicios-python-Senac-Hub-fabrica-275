#João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas.
# Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta.
# Faça um algoritmo que calcule e mostre quanto restará do salário do João
salario=1200
c1=200
c2=120
juros=0.2
total=(c1+(c1*juros))+(c1+(c2*juros))
print (f'O valor total das contas é R$: {total:.2f}')
resto=salario-total
print(f'João ficará com: R$ {resto:.2f} de seu salario.')