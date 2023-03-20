from classes02 import *

class programex2:
    if __name__ == '__main__':
        pessoa1 = Pessoa()
        pessoa2 = Pessoa()
        print('Dados da primeira pessoa: ')
        pessoa1.nome = input('Nome da pessoa 1: ')
        pessoa1.salario = int(input('Salário da pessoa 1:'))

        print('Dados da segunda pessoa: ')
        pessoa2.nome = input('Nome da pessoa 2: ')
        pessoa2.salario = int(input('salário da pessoa 2:'))
        media=((pessoa2.salario+pessoa1.salario)/2)
        print ('A média de saláro é de: ' (media))