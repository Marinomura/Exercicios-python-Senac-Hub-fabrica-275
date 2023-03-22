#crie uma função que recebe uma lista de palavras como parametro,
#e retorne uma lista com palavas que comecem com a letra A
def palavras_com_A (x):
    p=[]
    for A in x:
        if A[0] =='a' or A [0] =='A':
            p.append(A)
            print (p)
    return p
