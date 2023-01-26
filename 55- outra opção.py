#Ler 20 números e exibir qual foi o menor e o maior informados.​
#contar numeros digitados

num = int(input('Digite um numero: '))
menor=num
maior = num
cont=0
for i in range(1,20):
    cont +=1
    num= int(input('Digite ourro numero:'))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print (f'O menor número digitado foi: {menor}')
print (f'O menor número digitado foi: {maior}')
print (f'Foram digitados : {cont}')        
