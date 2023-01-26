#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
#operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")
operacao = int(input('1 - Soma\n2 - Subtração\n3- Multiplicação\n4 - Divisião\n'))

if operacao == 1:
        resultado= n1 + n2
elif operacao == 2:
        resultado = n1 - n2
elif operacao == 3:
        resultado = n1*n2
elif operacao == 4:
        resultado = n1 / n2
else:
        print('Operação inválida')
        exit()
    
print('Resultado = ', resultado)
    
if resultado % 2 == 0:
        print('É número é par')
else:
        print('É número é impar')
if resultado >=0:
        print ('É um número positivo')
else:
        print ('É um número negativo')
if resultado == int: #está dando erro aqui. ele restorna como float
        print ('É um número inteiro')
else:  
        print ('É um número decimal')        