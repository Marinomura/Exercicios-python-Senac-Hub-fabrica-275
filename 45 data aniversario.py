# Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
#a) a idade dessa pessoa em anos; 
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em dias; 
# d) a idade dessa pessoa em semanas. 
anoM=12
anoD=365
ano_S=52

ano_nasc=int(input('Qual o ano de nascimento? '))
ano_atual= int(input('Qual o ano corrente? '))
idade = (ano_atual-ano_nasc)
print ('A idade em anos é : ',idade)
print (f'A idade em meses é : {idade*anoM} meses')
print (f'A idade em dias é :  {idade*anoD} dias')
print (f'A idade em semana é : {idade*ano_S} semanas')