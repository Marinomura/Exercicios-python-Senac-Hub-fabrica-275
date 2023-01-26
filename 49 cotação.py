#Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). 
#O programa deve solicitar o valor da cotação do dólar.​

dolar=float(input('Qual o valor da cotação em Dólar ? '))
converte=float(input('Quanto deseja comprar em Real ? '))
total=converte/dolar
print (f'O valor da conversão é de: R$ {total:.2f} ')