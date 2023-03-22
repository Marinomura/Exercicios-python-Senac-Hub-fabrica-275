#crie uma função que recebe uma lista de numeros como parametro
# e retorne uma lista com apenas os numeros impares
def impares (lista):
    impar = []
    for num in lista:
        if num%2 !=0:
            impar.append (num)
    return print (impar)
impares ([1,2,3,6,8,12,15,19,22])

