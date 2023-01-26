cont = 1
soma = 0

while cont !=0:
    num = int(input('Digite um numero: '))
    soma = soma + num
    cont = cont +1


    opcao = input('Digite y para sim e n não:')
    if opcao == 'N' or opcao == 'n':
        cont = 0
    else:
        cont=1

print('O resultado é ' ,soma)