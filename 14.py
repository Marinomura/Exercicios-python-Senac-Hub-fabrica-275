#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
# Após, calcule e escreva o saldo atual (saldo atual = saldo - débito + crédito). 
# Também teste se saldo atual for maior ou igual a zero.
# Em seguida escreva a mensagem 'Saldo Positivo', senão, escrever a mensagem 'Saldo Negativo' .​
nºconta = input("Digite o numero da conta: ")
saldo = float(input("Digite saldo: R$ "))
debito = float(input("Digite o valor débito: R$ "))
credito = float(input("Digite o valor crédito: R$ "))
Saldoatual = saldo-debito+credito
print = (f' Saldo =', {Saldoatual:.2f})
if Saldoatual <=0:
    print("O saldo atual é Negativo")
else:
    print("O saldo é Positivo")
