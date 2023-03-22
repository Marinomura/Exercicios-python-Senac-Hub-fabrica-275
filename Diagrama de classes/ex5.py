#crie uma função que recebe uma lista de palavras como parametro,
#e retorne uma lista com palavas que comecem com a letra A
def palavras_com_A (x):
    p=[]
    for A in x:
        if A in p:
            p.append(A)
    return p
print('lista dos nomes ', p)