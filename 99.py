#- Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.​
v1=[]
v2=[]
v3=[]
for posicao in range (10):
    v1.append (input("Digite o elemento "  +str(posicao+1) + 'ª posição do primeiro vetor: '))
for posicao in range (10):
    v2.append(input("Digite o elemento "  +str(posicao+1)+  "ª posição do segundo vetor: "))
for posicao3 in range (10):
    v3.append(v1[posicao3])
    v3.append(v2[posicao3])
print (v3)