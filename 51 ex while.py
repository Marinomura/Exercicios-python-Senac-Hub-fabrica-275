#Ler diversos números e exibir qual foi a soma. O valor -999 é o código de fim da entrada

num = int(input("digite um número: "))
soma = 0
while num != -999:
    soma = soma+num    
    num = int(input('digite um número: '))
    
print (soma)
