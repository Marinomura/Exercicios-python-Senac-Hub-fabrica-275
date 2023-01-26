alunos=['maria', ' josé', 'mario',' tomaz', 'ana', 'marcia', 'paulo', 'silvio']
print (alunos)
print('*'*50)
for al in range(0,len(alunos)): #len é para ler dentro da lista informada qdo não se sabe a posição
    print (f'Os alunos da Fabrica são: {alunos}')
print('*'*50)
    
for al in range(0,len(alunos)): #len é para ler dentro da lista informada qdo não se sabe a posição
    print (f'Os alunos da Fabrica são: {al}') #vai ler as posições da lista
print('*'*50)    
for al in range(0,len(alunos)): #len é para ler dentro da lista informada qdo não se sabe a posição
    print (f'Os alunos da Fabrica são: {alunos[al]}') #aqui lê um por um na lista. al é uma váriavel de aluno
print('*'*50)
for al in range(0,len(alunos)): #len é para ler dentro da lista informada qdo não se sabe a posição
    print (f'Os alunos da Fabrica são: {alunos[al]} e esão na posição {al} da tupla') #aqui lê a posição na lista
print('*'*50)
alunos=['maria', ' josé', 'mario',' tomaz', 'ana', 'marcia', 'paulo', 'silvio']
print('Detras pra frente')
for al in range(-1, -9, -1):
  print (f'Os alunos da Fabrica são {alunos[al]}')
  print('*'*50 )