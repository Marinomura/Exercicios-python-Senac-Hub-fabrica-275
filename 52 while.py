#Ler diversos números e exibir quantos foram digitados. O valor -1 é código de  fim de entrada. ​
num = int(input(' Digite um número: '))
contador=0
while num != -1:
    contador = contador+1
    num = int(input('Digite um número: '))
print(contador)