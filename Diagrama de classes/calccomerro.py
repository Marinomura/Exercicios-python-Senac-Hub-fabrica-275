class calc ():
    def __init__(self):
        
        self.operacao = input("Digite a operacao desejada (soma, sub, mult, div): ")
        self.numero1 = int(input("Digite o primeiro número: "))
        self.numero2 = int(input("Digite o segundo número: "))

    def operacao(self):
        if self.operacao == "soma":
	        resultado = int(self.numero1) + int(self.numero2)
        if self.operacao == "sub":
        	resultado = int(self.numero1) - int(self.numero2)
        if self.operacao == "mult":
        	resultado = int(self.numero1) * int(self.numero2)
        if self.operacao == "div":
        	resultado = int(self.numero1) / int(self.numero2)
        else:
            resultado = resultado
    
        print ("O resultado da operação é: " ,resultado)

n1=calc()
n1.operacao()