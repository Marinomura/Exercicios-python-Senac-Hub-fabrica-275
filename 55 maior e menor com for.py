#Ler 20 números e exibir qual foi o menor e o maior informados.​
num = int(input('Digite um numero: '))
menor=num
maior = num
for i in range(1,20):
    num= int(input('Digite ourro numero:'))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print (f'O menor número digitado foi: {menor}')
print (f'O menor número digitado foi: {maior}')
