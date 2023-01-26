#Ler diversos números inteiros e exibir quantas vezes o número 50 foi  informado. O valor 0 é o código de fim de entrada. ​
num = int(input('Digite um número: '))
num50=0
while num != 0 :
        num = int(input('Digite um número: '))
        if num ==50:
            num50=num50+1
print (f'A quantidade de números 50 foram digitados: {num50}')