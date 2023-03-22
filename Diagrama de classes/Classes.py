class teste ():
    def __init__(self) -> None:
        self.idade = int (input ('Digite a sua idade: '))
        self.sexo = input ('Digite o seu sexo: ')
    def exibir (self):
        print(self.idade, self.sexo)
    def cerificar_adeq(self):
        if self.idade >17 and self.sexo =="F":
            print ('Tá dentro!!!')
        else:
            print ('Tá fora!!!')
pessoa=teste()
