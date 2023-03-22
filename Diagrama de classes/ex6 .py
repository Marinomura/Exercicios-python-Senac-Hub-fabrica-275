#crie uma função que recebe uma lista de string como parametro e retorna a string mais longa
def string_longa(lista):
    mais_longa=lista [0]
    for i in lista:
        if len(i) > len (mais_longa):
            mais_longa=i
    return mais_longa