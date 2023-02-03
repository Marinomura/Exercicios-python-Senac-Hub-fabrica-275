#Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.​
medias = []
mediasMaior = 0

for a in range (10):
    media = 0
    for x in range(4):
        media += float(input(f'Digite a nota {x+1} do aluno {a+1} : '))
    print('\n')
    media = media/4
    medias.append (media)
print(f'A quantidade de alunos com média maior que 7 é: {mediasMaior}')
