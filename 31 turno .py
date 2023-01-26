# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite M para Maturino, V para Vespertino e N pra Noturno?: ').upper()

#M = ('Bom Dia!')
#V = ('Boa Tarde!')
#N = ('Boa Noite!')

if turno == 'M':
 print(' Bom Dia! ')
elif turno == 'N':
 print('Boa noite! ')
elif turno== 'V':
 print("Boa tarde! ")
else:
    print("VALOR INVÁLIDO!!")

