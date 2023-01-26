#Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição:
# Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso contrário o lucro será de 30%.
# Sabendo disso, faça um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

vproduto = float(input("Digite o valor de aquisição do produto: R$ "))
menor_50 = 0.45
maior_50 = 0.30

if menor_50 <=50:
    menorq50 = menor_50*vproduto
    print(f'O valor de venda é de R$ {menorq50+vproduto:.2f}')

elif maior_50 >=50:
     maiorq50 = maior_50*vproduto
     print(f'O valor de venda é de R$ {maiorq50+vproduto:.2f}')
