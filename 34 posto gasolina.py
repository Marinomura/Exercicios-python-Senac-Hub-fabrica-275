#Um  posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litro = float(input ('Quantos litros vai abastecer? '))
combustivel = input('Digite A para alcool ou G para gasolina: ').upper()
preco = 0
gasolina = 2.50
alcool = 1.90

if litro <=20 and combustivel == 'A':
    combustivel = 'alcool'
    print('O valor a ser pago é de R$:', (alcool*0.03)+(alcool*litro))
elif litro >=20 and combustivel == 'A':
    combustivel='alcool'
    print(' O valor a ser pago é de R$: ',(alcool*0.05)+(alcool*litro))

if litro <=20 and combustivel == 'G':
    combustivel='gasolina'
    print (' O valor a ser pago é de R$:', (gasolina*0.03)+(gasolina*litro))
elif litro >=20 and combustivel == 'G':
    combustivel='gasolina'
    print(' O valor a ser pago é de R$: ',(gasolina*0.05)+(gasolina*litro))
    
print (combustivel)
