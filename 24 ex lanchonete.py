# A lanchonete GostoSoft vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer.
# Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas,
# faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.

qtidade_fazer=int(input("Digite a quantidade de sanduiche a fazer: "))
print('\n')
presunto=50
queijo=2*50
hamburguer=100

presunto_kg = presunto/1000*qtidade_fazer
queijo_kg = queijo/1000*qtidade_fazer
hamburguer_kg = hamburguer/1000*qtidade_fazer

print('Quantidade a comprar de presunto kg',presunto_kg)
print("Quantiddade a comprar de quejo kg",queijo_kg)
print("Quantidade comprar de hamburguer kg",hamburguer_kg)






