#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.​
listaNumerosReais = []
print ('Informe os 10 numeros reais')
for i in range(0,10):
  lista=float(input('Numero: '))
  listaNumerosReais.append (lista)
listaNumerosReais.reverse()
print (listaNumerosReais) 