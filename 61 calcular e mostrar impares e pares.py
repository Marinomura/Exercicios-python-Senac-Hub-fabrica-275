#Faça um programa que peça 10 números inteiros, calcule e mostre 
# a quantidade de números pares e a quantidade de números impares.​

par=0
impar =0
for cont in range (0,11):
    num = int(input("Digite um número: "))
    if num %2==0:
        par = par+1
    else:
        impar=impar+1
print(f'A quantidade de números pares digitados foram de {par}')
print(f'A quantidade de números ímpares digitados foram de {impar}')