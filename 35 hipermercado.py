#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:​
#                    Até 5 Kg              Acima de 5 Kg​
#File Duplo      R$ 34,90 por Kg          R$ 35,80 por Kg​
#Alcatra         R$ 44,90 por Kg          R$ 46,80 por Kg​
#Picanha         R$ 66,90 por Kg          R$ 67,80 por Kg​
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.​


print ('Hoje estamos com uma promoção impredivel\n 1 Filé Duplo\n 2 Alcatra\n 3 Picanha ')
tipo = int(input ("Qual será a carne hoje: "))

if tipo ==1 :
    tipo =  ("Filé Duplo")
if tipo ==2:
    tipo = ("Alcatra")
if tipo == 3:
    tipo = ('Picanha')

qtdade =float(input('Quantos quilos ?'))
resposta = int(input('A compra é realizada com cartão tabajara? 1 p/ SIM - 2 p/ NÃO: '))
file = 34.90
file5 = 35.80
alcatra = 44.90
alcatra5 = 46.80
picanha = 66.90
picanha5= 67.80

if qtdade <=5:
 preco=qtdade*file
else:
    preco = qtdade*file5

if qtdade <=5:
   preco = qtdade*alcatra
else:
   preco= qtdade*alcatra5
    
if qtdade <=5:
   preco= qtdade*picanha
else:
   preco= qtdade*picanha5
   
if resposta == 1:
    r = 'SIM'     
    desconto = (preco * 0.05)
    total = preco - desconto
else:
    r = "NAO"
    total = preco  

print("\n***************************CUPOM FISCAL**************************************")
print(f"* Carne.......................................................... {tipo}")
print(f"* Quantidade.....................................................{qtdade:.2f}KG")
print(f"* Preço......................................................... R$:{preco:.2f}")
print("* Cartao Tabajara................................................ %s " %r)
print(f"* Total com desconto............................................ R$:{total:.2f}")