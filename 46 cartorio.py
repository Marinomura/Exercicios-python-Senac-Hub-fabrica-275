#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos)
nome= input('Digite o nome: ')
sexo= input ('Digite o sexo, F para feminino ou M para masculino: ').upper()
ecivil=input('Digite o estado civil, C para Casado ou S pra Solteiro: ').upper()
if sexo == 'F' and ecivil== 'C':
    print ('Quanto tempo está casada? ')
    