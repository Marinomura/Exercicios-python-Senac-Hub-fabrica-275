#Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido.
# Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, 
# o algoritmo deverá escrever “Financiamento Concedido"; senão, ele deverá escrever "Financiamento Negado".
# Independente de conceder ou não o financiamento, o algoritmo escreverá depois a frase "Obrigado por nos consultar."​

import time

salario = float(input('Digite o salário: R$  '))
financiamento = float(input('Digite o valor do financiamento desejado: R$ '))
base = salario * 5
print ("Analisando.....")
time.sleep (1)
if financiamento <= base:
    print('Financiamento Concedido!!')
else:
    print('Financiamento Negado!!')
print('Obrigado por nos consultar!')