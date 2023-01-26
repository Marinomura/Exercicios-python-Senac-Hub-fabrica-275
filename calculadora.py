from re import match

n1 = float (input())
n2 = float (input())

print('............')
print('......opções de calculadora...')
print('.....soma = + .....')
print('.....subtração +-....')
print('.....multiplicação = *....')
print('....divisão = /...')
print('...............')

op = input("Digite a operação: ")

match(op):
    case '+':
        soma =n1+n2
        print(f'{n1}+{n2} = {soma}')

    case '-':
        sub = n1-n2
        print(f'{n1}-{n2}= {sub}')

    case '*':
        multi = n1*n2
        print(f'{n1}*{n2}= {multi}')

    case '/' :
        div = n1/n2
        print(f'{n1}/{n2} = {div}')