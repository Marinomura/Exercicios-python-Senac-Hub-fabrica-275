listaNotas = []
notasAluno = []

print ('Digite as Notas dos Alunos: ')
for i in range(2):
  media = 0
  notasAluno = []
  print ('Aluno: 0' + str(i + 1))

  for j in range(4):
    notasAluno.append(float(input('Nota 0' + str(j+1) + ': ')))
    media += notasAluno[j]
  media = media/4
    
  #print(f'media: {media:.2f}')
  listaNotas.append(media)

print(f'Médias: {media:.2f}')
print (listaNotas) #assim armazena as médias