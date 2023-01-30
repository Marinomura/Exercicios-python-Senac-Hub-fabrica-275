#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.​
listaNotas = []
media = 0
print ('Informe as 4 notas')
for i in range(0,4):
    notas=float(input('Nota :'))
    listaNotas.append (notas)
media += listaNotas[i]
print (listaNotas) 
soma=sum(listaNotas)
print (soma/4)