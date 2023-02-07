# Máquina de café​

#Uma máquina de vender café funciona da seguinte forma: o usuário seleciona um tipo de café, 
# insere algumas notas ou moedas na máquina e, se a quantia paga for suficiente para pagar o face desejado,
# a máquina enche um copo descartável com o tipo de café selecionado e dá o troco em moedas. 
# Faça um programa para imitar esse comportamento: o usuário informa qual é o tipo de café desejado e o valor pago, 
# e o seu programa deve dizer qual deve ser o valor do troco e quantas moedas são necessárias para pagar esse troco.
# Considere a existência de moedas com os seguintes valores: R$ 1.00, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01.A tabela de preços é dada abaixo:​

#Tipos de café             Preço
#Café normal                R$1.05
#Café expresso              R$ 1.52
#Capuccino                  R$ 2.17
#Mocaccino                  R$ 2.36

print('''Escolha seu café:\n
1 - normal    - R$1,05 
2 - expresso  - R$1,52 
3 - capuccino - R$2,17 
4 - mocaccino - R$2,36 ''')
print(30 * '*')
cafe = int(input('Escolha seu café: '))
valor=0
if cafe >=1 and cafe<=4:
    valor = float(input('Com qual valor você ira pagar: R$ '))
    match cafe:
        case 1:
         valor_cafe = 1.05

        case 2:
            valor_cafe = 1.52

        case 3:
            valor_cafe = 2.17

        case 4:
            valor_cafe = 2.36

    troco = valor - valor_cafe

    if valor >= valor_cafe:
        num = valor - valor_cafe

        humreal = num // 1.0
        num = num - (humreal * 1.0)

        cinquenta = num // 0.5
        num = num - (cinquenta * 0.5)

        vinteCinco = num // 0.25
        num = num - (vinteCinco * 0.25)

        dez = num // 0.10
        num = num - (dez * 0.10)

        cinco = num // 0.05
        num = num - (cinco * 0.05)

        hum = num // 0.01
        
        
    
    else:
        print('Por favor escolha uma das opções na tela!')
    print(f'O valor do troco é de R${troco}')
    print(f'Moedas de R$1 real = {humreal} ')
    print(f'Moedas de R$0,50 centavos = {cinquenta}')
    print(f'Moedas de R$0,25 centavos = {vinteCinco}')
    print(f'Moedas de R$0,10 centavos = {dez}')
    print(f'Moedas de R$0,05 centavos = {cinco}')
    print(f'Moedas de R$0,01 centavos = {hum}')
else:
    
        print('Por favor escolha uma das opções na tela!')
