#Dani tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar.
# Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais.
# Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real.
# Não havendo moeda de um tipo, a quantidade respectiva é zero. ​

print("\nDigite as quantidades de moedas guardadas:\n")
n01=int(input("Quantas moedas de $0,01: "))
n05 =int(input("Quantas moedas de $0,05: "))
n10= int(input("Quantas moedas de $0,10: "))
n25=int(input("Quantas moedas de $0,25: "))
n50 = int(input("Quantas moedas de $0,50: "))
n1= int(input("Quantas moedas de $1,00: "))
total=((n01*0.01)+(n10*0.10)+(n05*0.05)+(n25*0.25)+(n50*0.50)+(n1*1))
print (f'{total:.2f}')
