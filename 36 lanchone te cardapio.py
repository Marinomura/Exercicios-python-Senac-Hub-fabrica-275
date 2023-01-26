#O cardápio da lanchonete Burgão é o seguinte:
#ESPECIFICAÇÃO CÓDIGO PREÇO
#Cachorro Quente       100           R$ 11,20 ​
#Ovo Simples           101           R$   8,30 ​
#Bauru com Ovo         102           R$ 11,50 ​
#Hambúrguer            103           R$ 16,20 ​
#Refrigerante          201           R$ 6,00 ​
#Suco                  202           R$ 7,50 ​
#Água Mineral          203           R$ 4,70 ​
#Escreva um algoritmo que leia o código de um sanduíche e de uma bebida,
# e mostre o valor a pagar pelo cliente. Assuma as entradas corretas:

total=0
print ('Faça sua escolha no Cardápio: ')
print('\nCachorro Quente: 100'
      '\nOvo Simples:     101'
      '\nBauru com Ovo:   102'
      '\nHambúrguer:      103'
      '\nRefrigerante:    201'
      '\nSuco:            202'
      '\nÁgua Mineral:    203')

codsand = input('Digite o codigo do sanduiche: ')

codbeb =input('Digite o codigo da bebida: ')
match(codsand):
      case '100':
       total = total+ 11.2
      case '101':
       total=total +8.3
      case '102':
       total=total+11.5
      case '103':
       total=total+16.20

match(codbeb):
 case '201':
     total = total + 6.0
 case '202':
    total = total +7.50
 case '203':
    total = total + 4.7

print(f"O valor total a pagar é de R${total}")
