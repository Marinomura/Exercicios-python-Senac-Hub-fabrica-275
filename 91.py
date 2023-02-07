#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:​

#Encerre o programa com uma mensagem;​
nota=0
valores=[]
while nota !=-1:
    nota = float(input("Digite um valor ou -1 para encerrar: "))
    if nota!= -1:
        valores.append (nota)
#Mostre a quantidade de valores que foram lidos
print ("A quantidade de valores que foram lidos é: ", len(valores))
print('\n')
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;​
print ("Valores em ordem informados um ao lado do outro é: ", valores)
print('\n')
print ("Valores na ordem inversa à que foram informados, um abaixo do outro")
for indice in range (len(valores)-1,-1,-1):
    print(valores[indice])
print('\n')
#Calcule e mostre a soma dos valores;
print ("A soma dos valores é :", sum(valores))
num=0
for nota in valores:
    num =+ nota
    print(num)
    
#Calcule e mostre a média dos valores
media=num/ len(valores)
print('A média dos valores: ', media)
#Calcule e mostre a quantidade de valores acima da média calculada;
v_acima=0
for nota in valores:
    if nota > media:
        v_acima += 1
print('Os valores acima da média: ',v_acima)
#Calcule e mostre a quantidade de valores abaixo de sete;
print('Os valores abaixo de 7 é:', end='' )

abaixo_7=0
for nots  in valores:
    if nota < 7:
        abaixo_7 +=1
print (abaixo_7)

print('ACABOU')