# A fábrica de refrigerantes Gui-Cola vende seu produto em três formatos:​

#Lata de 350 ml; Garrafa de 600 ml; Garrafa de 2 litros.​

#Se um comerciante compra uma determinada quantidade de cada formato,
# faça um algoritmo para calcular quantos litros de refrigerante ele comprou.​
n=0
lata=0.350
garrafa_media=0.600
garrafa_grande=2
#compra=int(input('Quais produtos precisa? '))
#qtidade=int(input('Qual a quantidade dos produtos?'))
qt_lata = int(input('Qual a quantidade de refrigerante lata precisa? '))
qt_media = int(input('Qual a quantidade de garrafas de 600ml precisa? ' ))
qt_grande = int(input('Qual a quantidade de garrafas de 2 litros precisa? '))
total_compra=((qt_lata*lata)+(qt_media * garrafa_media)+(qt_grande*garrafa_grande))
print (f'O total de litros comprado é de : {total_compra:.2f} litros')