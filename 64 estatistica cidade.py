# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:​

#Código da cidade;​

#Número de veículos de passeio (em 1999);​

#Número de acidentes de trânsito com vítimas (em 1999). ​

#Deseja-se saber:​

#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;​

#Qual a média de veículos nas cinco cidades juntas;​

#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.​

cod=int(input('Digite o Código da Cidade:'))
veiculos = float(input('Digite a quantidade de veículos de passeio: '))
acidente= float(input('Digite o número de acidentes de trânsito com vítimas: '))
codcidadeMenor = codcidadeMaior = cod
maior = menor = acidente
soma = soma_acidente = cont=0
soma = veiculos
for c in range(0,2):
    
    cod= int(input("Digite  o código da cidade: "))
    veiculos= float(input('Digite a quantidade de veículo de passeio: '))
    acidente =float(input('Digite o número de acidentes de trânsito com vítimas: '))
    soma += veiculos
    
    if acidente>maior:
        maior = acidente
        codcidadeMaior= cod
        
    if acidente<menor:
        menor=acidente
        codcidadeMenor=cod
    
    if veiculos<= 2000:
        soma_acidente += acidente
        cont += 1
        
print(f'O código da cidade com menor indice de acidente é {codcidadeMenor} com {menor} acidentes.')
print(f'O código da cidade co maior indice de acidentes é {codcidadeMaior} com {maior} acidentes.')
print(f'A média dos véiculos das cinco cidades é: {soma/5}')
print(f'A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é {soma_acidente/cont:.2f}')