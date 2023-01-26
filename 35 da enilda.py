print('Hoje estamos com uma promoção impredivel\n 1 File\n 2 Alcatra\n 3 Picanha ')
tipo = int(input("Digite qual será a carne hoje: "))
qtdade = float(input('Quantos quilos ?'))

if tipo == 1:
    carne = "Filé"
    file = 34.90
    file5 = 35.80
    if qtdade <=5:
        preco = qtdade * file
    else:
        preco = qtdade * file5


elif tipo == 2:
    carne = "Alcatra"
    alcatra = 44.90
    alcatra5 = 46.80
    if qtdade <=5:
        preco = qtdade * alcatra
    else:
        preco = qtdade * alcatra5
    total = preco

elif tipo == 3:
    carne = "Picanha"
    picanha = 66.90
    picanha5 = 67.80
    if qtdade <= 5:
        preco = qtdade * picanha
    else:
        preco = qtdade * picanha5
    total = preco
else:
    print ('Código inválido!')
resposta = int(input('A compra é realizada com cartão tabajara? 1 p/ SIM - 2 p/ NÃO: '))
if resposta == 1:
    r = 'SIM'
    desconto = (preco * 0.05)
    total = preco - desconto

elif resposta==2:
    r = "NAO"
    total = preco

print("\n***************************CUPOM FISCAL**************************************")
print(f"* Carne.......................................................... {carne}")
print(f"* Quantidade.....................................................{qtdade:.2f}Kg")
print(f"* Preço......................................................... R$:{total:.2f}")
print(f"* Cartao Tabajara................................................ {r}")
if resposta ==1:
    print(f"* Total com desconto............................................ R$:{total:.2f}")