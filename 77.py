#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
#Imprima as consoantes.​
caract=[]
vogais=["a","e","i","o","u"]
contvogal = 0
x = 1
while x <= 10:
    entrada = input("Caractere %d: " %x)
    x += 1
    caract.append(entrada)
    if entrada in vogais:
        contvogal += 1
print ("Consoantes: ",(len(caract))-contvogal)
