#Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.​
num = float(input('Digite um número: '))
menor = num
maior=num
soma=0
while num != -999:
    soma = soma+num
    if num > maior:
        maior = num
    elif num <menor:
        menor = num
    num = float(input('Digite um número: '))
        
print(f'A soma dos números digitados foi {soma:.0f}, o menor número digitado foi {menor:.0f}'
      f' o maior número digitado {maior:.0f}')