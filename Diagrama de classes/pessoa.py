#pessoa  tem os atributos:nome,idade e altura. teremos como método chamado 'imprimir
#os valores dos atributos da pessoa na tela(criar no minimo 2 objetos)
class pessoa ():
    def __init__(self) :
        self.idade = int (input ('Digite a sua idade: '))
        self.nome = input ('Digite o seu nome: ').upper()
        self.altura= input ('Digite sua altura em centímetros: ')
        
    def exibir (self):
        print(self.idade, self.nome, self.altura)
    
    
pessoa1=pessoa()
pessoa1.exibir()
pessoa_mala=pessoa()
pessoa_mala.exibir()