#Escreva um algoritmo que leia um vetor com 10 posições de números inteiros.
#Em seguida receba um novo valor do usuário e verifique se este valor se encontra no vetor.​
lista=[]
for n in range (0,10):
    num=int(input('Digite 10 posições de números inteiros: '))
    lista.append(num)
print (lista)
novo=int(input("Digite um novo número para verificar se existe na lista: "))   
if novo in lista:
    print('Sim está na lista')
    print (novo)
else: 
    print ('Não existe na lista!!')