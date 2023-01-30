#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:​

#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida​
#1       0​
#3       10​
#6       15​
#9       20​
#12      25​


#Exemplo de saída do programa:​

#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela​
#R$ 1.000,00     0               1                       R$  1.000,00​
#R$ 1.100,00     100             3                       R$    366,00​
#R$ 1.150,00     150             6                       R$    191,67​

vl_divida=float(input('Informe o valor da dívida: R$ '))
qtdade_parcelas=int(input('Digite a quantidade de parcelas '))
vl_juros1=0
vl_juros3=0.10
vl_juros6=0.15
vl_juros9=0.2
vl_juros12=0.25
vl_parcela=vl_divida/qtdade_parcelas 
