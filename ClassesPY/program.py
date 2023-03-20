from Pessoa import *


class Program:
    if __name__ == '__main__':
        pessoa1 = Pessoa()
        pessoa2 = Pessoa()
        print('Dados da primeira pessoa: ')
        pessoa1.nome = input('Nome da pessoa 1: ')
        pessoa1.idade = int(input('Idade da pessoa 1:'))

        print('Dados da segunda pessoa: ')
        pessoa2.nome = input('Nome da pessoa 2: ')
        pessoa2.idade = int(input('Idade da pessoa 2:'))
        if (pessoa1.idade > pessoa2.idade):
            print('A pessoa mais velha é :', pessoa1.nome)
        else:
            print('A pessoa mais velha é :', pessoa2.nome)
