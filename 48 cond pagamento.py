#Elabore um algoritmo que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento.
# Utilize os códigos da tabela a seguir para ler qual condição de pagamento escolhida e efetuar o cálculo adequado. ​

#Código Condição de pagamento: ​

#1 - À vista em dinheiro ou pix, recebe 10% de desconto;​

#2 -  À vista no cartão de crédito, recebe 5% de desconto ​

#3 - Em duas vezes, preço normal de etiqueta sem juros ​

#4 - Em três vezes, preço normal de etiqueta mais juros de 10% ​

desc=0.10
desc1=0.05
juros=0.10
x_pag=3
x_pag2=2
valor_prod= float(input('Digite o valor do produto: R$ '))
f_pagamento=input('Digite a forma de pagamento: \n 1 - para dinheiro ou pix\n 2 - à vista no cartão de crédito\n 3 - pagamento 2 vezes sem juros\n 4 - pagamento em 3x com juros\n  ')
if f_pagamento =='1':
    pagamento=valor_prod-(valor_prod*desc)
    print (f'O valor da compra é de :R$ {pagamento} com desconto de 10%. ')
elif f_pagamento =='2':
    pagamento=valor_prod-(valor_prod*desc1)
    print (f'O valor da compra é de :R$ {pagamento} com descontp de 5%.')
elif f_pagamento =='3':
    pagamento=valor_prod
    print (f'O valor da compra é de :R$ {pagamento} em 2 vezes sem juros.')
elif f_pagamento =='4':
    pagamento=(valor_prod + (valor_prod*juros))
    print (f'O valor da compra é de :R$ {pagamento} em 3 vezes com juros de 10%. ')
else:
    print ('OPÇÃO INVÁLIDA')
    