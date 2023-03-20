#crie uma função que recebe uma lista de numeros como parametro e retorne o maior numero da lista

def maior_numero(lista):
  maior =lista [0]
  for num in lista:
    if num > maior:
      maior =num
  return  print(maior)
maior_numero ([2,3,4,5,6])