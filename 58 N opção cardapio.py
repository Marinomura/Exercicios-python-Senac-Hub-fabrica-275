#Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante para uma pessoa
# (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. Ex: Bife acebolado R$15,00; Lasanha R$25,00).​
#A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário,
# “Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. Se o usuário aceitar, 
# mostrar o valor final (valor do prato + 10%), 
# caso contrário, mostrar o valor final (somente o valor do prato).​
lasanha=15
parmegiana=25
bife_cavalo=25
macarrao=15
risoto=25
salmao_risoto=50
txservico= 0.10

pedido=input('Qual prato deseja hoje? \n 1-Lasanha\n 2-Parmegiana\n 3-Bife à Cavalo\n 4-Macarrão\n 5-Risoto\n'
              ' 6-Risoto com Salmão\n ')
if pedido=='1':
    pedido=lasanha
    print (f'Seu prato custa:R$ {lasanha:.2f}. Deseja pagar taxa de serviço?')
    sim=pedido+(pedido*txservico)
    nao=pedido
    if sim:
        print(f'Seu prato custa: R$ {sim:.2f}' )
    else:
        print (f'Seu prato custa: R$ {lasanha:.2f}.' )
elif pedido=='2':
    pedido=parmegiana
    print (f'Seu prato custa: R$ {parmegiana:.2f}. Deseja pagar taxa de serviço?')
    sim=pedido+(pedido*txservico)
    nao=pedido
    if sim:
        print(f'Seu prato custa: R$ {sim:.2f}' )
    else:
        print (f'Seu prato custa: R$ {parmegiana:.2f}.' )
elif pedido=='3':
    pedido=bife_cavalo
    print (f'Seu prato custa: R$ {bife_cavalo:.2f} Deseja pagar taxa de serviço?')
    sim=pedido+(pedido*txservico)
    nao=pedido
    if sim:
        print(f'Seu prato custa: R$ {sim:.2f}' )
    else:
        print (f'Seu prato custa: R$ {bife_cavalo:.2f}.' )
elif pedido=='4':
    pedido=macarrao
    print (f'Seu prato custa: R$ {macarrao:.2f}. Deseja pagar taxa de serviço?')
    sim=pedido+(pedido*txservico)
    nao=pedido
    if sim:
        print(f'Seu prato custa: R$ {sim:.2f}' )
    else:
        print (f'Seu prato custa: R$ {macarrao:.2f}.' )
elif pedido=='5':
    pedido=risoto
    print (f'Seu prato custa: R$ {risoto:.2f}. Deseja pagar taxa de serviço?')
    sim=pedido+(pedido*txservico)
    nao=pedido
    if sim:
        print(f'Seu prato custa: R$ {sim:.2f}' )
    else:
        print (f'Seu prato custa: R$ {risoto:.2f}.' )
elif pedido=='6':
    pedido=salmao_risoto
    print (f'Seu prato custa: R$ {salmao_risoto:.2f}. Deseja pagar taxa de serviço?' )
    sim=pedido+(pedido*txservico)
    nao=pedido
    if sim:
        print(f'Seu prato custa: R$ {sim:.2f}' )
    else:
        print (f'Seu prato custa: R$ {salmao_risoto:.2f}.' )
