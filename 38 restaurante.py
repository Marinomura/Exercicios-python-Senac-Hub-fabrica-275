#O restaurante a quilo Sabor em Quilo cobra R$59,00 por cada quilo de refeição.
 #Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
 #Assuma que a balança já desconte o peso do prato.​

preco_kg =59.0
peso = float(input(' Informe o peso do prato montado: '))
vl_pg = peso * preco_kg
print (f'Valor a pagar é de R$: {vl_pg: .2f}')
