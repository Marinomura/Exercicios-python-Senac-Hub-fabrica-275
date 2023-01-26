#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h= float(input('Altura: '))

peso_idealH = (72.7*h) - 58
peso_idealM = (62.1*h) - 44.7

print(f'Altura : {h:.2f} Peso ideal: {peso_idealM:.2f}')
print(f'Altura : {h:.2f} Peso ideal: {peso_idealH:.2f}')


