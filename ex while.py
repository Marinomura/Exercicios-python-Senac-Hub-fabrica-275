#Faça o mesmo que o exercício anterior, porém, ao invés de ler 10 números,
#o programa deverá ler e somar números até que o valor digitado seja zero ( 0 ).

cont = 1
soma = 0
final = 0

while cont !=0 :
    num = int(input(' Digite um numero: '))
    soma = soma + num
    cont = num + final

print(' Resultado:',soma)