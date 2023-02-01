#Considere os cenários de problemas a serem resolvidos:​
#1- Um berçário deseja informatizar suas operações.​
#Quando um bebê nasce, algumas informações são armazenadas sobre ele, tais como:
# nome, data do nascimento, peso do nascimento, altura, a mãe deste bebê e o médico que fez seu parto.
# Para as mães, o berçário também deseja manter um controle, guardando informações como: nome, endereço, telefone e data de nascimento. 
# Para os médicos, é importante saber: CRM, nome, telefone celular e especialidade.​

#Para resolver o cenário 1 faça:​
#A) Levantamento de requisitos (funcionais e não funcionais);​
#B) Diagramas UML (Caso de Uso);​
#C) Documento com levantamento de requisitos e diagramas UML;​
#D) Algoritmo em python.​
#E) Apresentação da atividade (Em slides)​
#F) Ao finalizar a atividade coloque na pasta compartilhada no Microsoft Teams (crie uma pasta com a descrição “AtivAva1DevAlg” dentro de ambas as pastas dos membros da dupla).
#bebe=float(input('Digite os dados do bebê: \n Nome: \n Data de nascimento: \n Peso no nascimento: \n Tamanho em centímetros: \n Nome da mãe: \n Nome do médico responsável pelo parto: \n'))
#print (bebe)
nomebebe=input('Digite o nome do bebê: ')
print(nomebebe)
dn_bebe=str(input("Digite a Data de nascimento do bebê: "))
print(f'Nasceu em: {dn_bebe}')
peso_bebe=float(input('Digite o peso do bebê em gramas: '))
print(f'Peso de nascimento é de:  {peso_bebe} gramas')
tamanho_bebe=float(input('Digite o tamanho do bebê em cm: '))
nome_mae=input('Digite o nome da mãe: ')
endereco=input('Digite o endereço da mãe do bebê: ')
tel_mae=input('Digite o número telefônico da mãe: ')
dn_mae=input('Digite a data de nascimento da mãe: ')
medico=input('Digite o nome do médico responsável pelo parto: ')
crm=input('Digite o número CRM do médico: ')
cel_med=input('Digite o número celular do médico: ')
espec_M=input('Digite a especialidade médica: ')

