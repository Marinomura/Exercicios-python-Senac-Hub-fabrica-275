#A padaria Super Pão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pãozinho custa R$ 1,00 e a broa custa R$ 3,50. 
#Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). 
#Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados. ​

pao=1
broa=3.5
poupar=0.1

qtdade_pao= int(input('Digite a quantidade de pães vendidos:'))
qtidade_broa=int(input('Digite a quantidade de broa vendida:'))
qtidade_total_venda= qtidade_broa+qtdade_pao
print (f'A quantide de produtos vendidas é de: {qtidade_total_venda:.2f} unidades')

valor_total_pao=qtdade_pao*pao
valor_total_broa=qtidade_broa*broa
valor_total_venda=valor_total_broa+valor_total_pao
print (f'O valor total de produtos vendidos é de R$: {valor_total_venda:.2f}')

valor_poupar=(valor_total_pao+valor_total_broa)*0.1
print (f'O valor a ser poupado é de R$: {valor_poupar:.2f}')
