#Faça um algoritmo que calcule e mostre a tabuada de um número digitado pelo usuário. ​
# é o mesmo exercicio que o 60?!

num = int(input('Digite qual tabuada você deseja: '))
print('*'*20, 'TABUADA DO',num, "*"*20)
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')