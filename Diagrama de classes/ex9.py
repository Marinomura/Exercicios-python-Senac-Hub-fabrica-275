#crie uma função que recebe uma lista de numeros como parametro e
# retorne uma lista com apenas numeros menores que 10
def num(lista):
    numero = []
    for num in lista:
        if num <= 10:
            numero.append (num)
    return print (numero)
num([1,2,3,6,8,12,15,19,22])
