#crie uma função que recebe uma lista de numeros como parametro 
# e retorne uma lista com apenas numeros pares
def pares (lista):
    par = []
    for num in lista:
        if num%2 == 0:
            par.append (num)
    return print (par)
pares ([1,2,3,6,8,12,15,19,22])
