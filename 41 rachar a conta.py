# Três amigos, Joceyr, Thiago e Alexandre. decidiram rachar igualmente a conta de um bar. 
# Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, 
# mas faça com que Joceyr e Thiago não paguem centavos.
# Ex: uma conta de R$101,53 resulta em R$33,00 para Joceyr, R$33,00 para Thiago e R$35,53 para Alexandre.
conta=float(input('Digite o valor total da conta a pagar: '))
pessoas=3
conta_div=conta % pessoas
total=(conta / pessoas)
cont_int=conta//pessoas
#print ('O valor da conta é R$:',conta)
print ('Joceyr e Thiago pagarão cada um: R$ ', cont_int)
pagante_int=cont_int+conta_div
print (f'Alexandre deverá pagar: R$ {pagante_int:.2f} ')
