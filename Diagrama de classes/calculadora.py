#uma classe para representar um calculadora que realiza as operaçoes basicas 
#(adição,subtração, multiplicação e divisão), criar no minimo 2 objetos

class calc ():
    def __init__(self):
        
        self.numero1 = int(input("Digite o primeiro número: "))
        self.numero2 = int(input("Digite o segundo número: "))

    def soma(self):
        r = self.numero1 + self.numero2
        print (" O resultado é: " , r)
    def sub (self):
        r=self.numero1 -self.numero2
        print (" O resultado é: " , r)
    def mult (self):
        r=self.numero1*self.numero2
        print (" O resultado é: " , r)
    def div (self):
        r=self.numero1/self.numero2
        print (" O resultado é: " , r)

n1=calc()
n1.soma()
n1.sub()
n1.mult()
n1.div()