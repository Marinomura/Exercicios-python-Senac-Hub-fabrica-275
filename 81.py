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
medico = {"nome":"" ,"crm":"" ,"cel_md":"" ,"especialidade":"" }
maes = {'nome':'','endereço':'','telefone':'','dt_nasc':'','prontuario':''}
bebes = {'nome':'','SEXO':'','dt_nasc':'','peso_nasc':'','tamanho':'','nome da mãe':'','médico responsavél':'','prontuário':''}
mostar={}
#cadastrar = int(input("\nSISTEMA DE CADASTRO (por favor digite a opção desejada): \n     1 para MÉDICOS \n     2 para MÃES \n     3 para BEBÊS \n     4 para exibir dados \n     0 para SAIR \n Opção escolhida: "))
print("\n"*2)
cadastrar=1
while cadastrar != 0:
    cadastrar = int(input("\nSISTEMA DE CADASTRO (por favor digite a opção desejada): \n     1 para MÉDICOS \n     2 para MÃES \n     3 para BEBÊS \n     4 para exibir dados \n     0 para SAIR \n Opção escolhida: "))

    if cadastrar == 1:
        print("\n CADASTRO DO MÉDICO\n","-"*18,"\n")
        nome_md =(input("Digite o nome do médico: ")).upper()
        medico["nome"] = nome_md
        num_crm = int(input("Digite o número do CRM: "))
        medico["num"] = num_crm
        cel_md = int(input("Digite o número do celular: "))
        medico["cel_md"] = cel_md
        especialidade = str(input("Digite a especialidade do médico: "))
        medico["especialidade"] = especialidade
        print("\n")
        
    elif cadastrar == 2:
        print("\n CADASTRO DA MÃE\n","-"*15,"\n")
        nome_mae=input('Digite o nome da mãe: ').upper()
        maes['nome']=nome_mae
        end_maes=input('Digite o endereço da mãe do bebê: ')
        maes['endereço']=end_maes
        tel_mae=input('Digite o número telefônico da mãe: ')
        maes['telefone']=tel_mae
        dn_mae=input('Digite a data de nascimento da mãe: ')
        maes['dt_nasc']=dn_mae
        pront=str(input('Digite o número do prontuário médico: '))
        maes['prontuario']=pront
       
        print("\n")
    elif cadastrar == 3:
        print("\n CADASTRO DO BEBÊ\n","-"*16,"\n")
        nomebebe=input('Digite o nome do bebê: ').upper()
        bebes['nome']=nomebebe
        genero=input('Digite o sexo do bebê: \n F para FEMININO \n M para MASCULINO: ').upper()
        bebes['SEXO']=genero
        print('\n')
        dn_bebe=str(input("Digite a Data de nascimento do bebê: "))
        bebes['dt_nasc']=dn_bebe
        peso_bebe=float(input('Digite o peso do bebê em gramas: '))
        bebes['peso_nasc']=peso_bebe
        tamanho_bebe=float(input('Digite o tamanho do bebê em cm: '))
        bebes['tamanho']=tamanho_bebe
        pront=str(input('Digite o número do prontuário médico: '))
        bebes['prontuário']=pront
        print("\n")
    elif cadastrar== 4:
        print('\n')
        print('Prontuário nº: ',bebes["prontuário"])
        print('Nome: ',bebes["nome"])
        if bebes["SEXO"] == "M":
            print("SEXO: Masculino")
        else:
            print("SEXO: Feminino")
        print("Nome da mãe: ",maes["nome"])
        print('Nasceu em: ',bebes["dt_nasc"])
        print('Medindo: ',bebes["tamanho"], 'centímetros')
        print('Pesando: ',bebes["peso_nasc"], 'gramas')
        print('-'*10)
        imprimir=input('Deseja imprimir a Pulseira Identificadora do Recém Nascido? ').upper()
        if imprimir=='S':
            print('Aguarde a impressão.')
        else:
            break
        