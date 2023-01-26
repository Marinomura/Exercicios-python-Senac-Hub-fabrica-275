#Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano.
#Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias. ​
dia=int(input('Digite uma data: '))
mes=int(input('Digite o mês desejado: '))
mes_comp=30
ano=365
#if mes < 1 and mes > 12:  Queria colocar pra dar erro se diferente e não rodou
#else:
# print ('INVALIDO')
print('Quantos dias se passam desde o inicio do ano? ')
calc_dia= dia
calc_mes = mes*30
print (calc_dia + (calc_mes))
print ('\n')
print ('Passaram-se ',(calc_dia + (calc_mes)), 'dias desde o inicio do ano')
