#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.​
nome= input('Digite o Nome do usuário ')
senha= input('Digite a senha do usuário ')
while nome ==senha:
    print('SENHA INVÁLIDA!! \n A senha deve ser diferente do usuario')
    senha=input('Digite a senha novamente\n ')