# Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela.
# Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.​
lista = []

for n in range (0,5):
    num=int(input('Digite 5 números inteiros: '))
    lista.append(num)
print (lista)
soma=sum(lista)   
print (f'A soma dos valores digitados é de: {soma}')
if soma in lista:
    print (f'O valor da soma é:, {soma}')
for x  in range (0,len(lista)):
    print (lista[x])