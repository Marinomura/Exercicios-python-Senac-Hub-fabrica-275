#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
# Você deve fazer um programa que receba o nome do ginasta
# e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média,
# conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:​

#https://www.alura.com.br/artigos/listas-no-python

#Atleta: Aparecido Parente​
#Nota: 9.9​
#Nota: 7.5​
#Nota: 9.5​
#Nota: 8.5​
#Nota: 9.0​
#Nota: 8.5​
#Nota: 9.7​
# Resultado final:​
#Atleta: Aparecido Parente​
#Melhor nota: 9.9​
#Pior nota: 7.5​
#Média: 9,04​

atleta=input('Digite o nome do atleta: ')
nota=[]
for n in range (0,7):
    notas=float(input('Digite as notas do jurado: '))
    nota.append (notas)
print(nota)

#for nota in notas: para tirar as piores notas, neste exemplo tira as notas zero
 #   if nota == 0:
  #      notas.remove(nota)
#print(notas)
#notas_validas = [nota for nota in notas if nota > 0]
#print(notas_validas)
#media_valida = sum(notas_validas) / len(notas_validas)
#print(media_valida)