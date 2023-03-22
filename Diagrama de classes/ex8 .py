#crie uma função que recebe uma lista de numeros como parametro e retorne o numero de ocorrencia
#de um determinado numeros da lista
def qtdade_ocorrencia (lista, num):
    contador = 0
    for  n  in lista:
        if n == num:
            contador +=1
    return print (contador)
    
qtdade_ocorrencia ([2,5,6,7,2,7,2,7],7)
            
    