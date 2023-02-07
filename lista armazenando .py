medias_alunos=[]
alunos_acima_media=0
for aluno in range (10):
    soma_notas=0
    for nota in range (4):
        print('Digite a ', nota+1, 'ª nota do ', aluno+1, 'º aluno', sep='')
        soma_notas += float(input())
    medias_alunos.append(soma_notas/4)
    if medias_alunos[aluno] >=7:
        alunos_acima_media += 1
print ('Média dos alunos: ', medias_alunos)
print ("Número de alunos acima da média: "), alunos_acima_media