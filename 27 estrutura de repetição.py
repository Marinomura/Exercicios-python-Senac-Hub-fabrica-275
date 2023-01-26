#O departamento de Educação Física deseja informatizar este setor e colocou à disposição os seguintes dados de 50 alunos:

#Matrícula, sexo (M, F), altura (cm) e status físico (1–bom, 2–regular, 3–ruim)

#Estes dados deverão ser lidos através de uma unidade de entrada qualquer.

#Calcular e imprimir:

#a) A quantidade de alunos do sexo feminino com altura superior a 170 cm.

#b) A % de alunos do sexo masculino (em relação ao total de alunos do sexo masculino) cujo status físico seja bom.

#matricula = input('Digite a matricula do aluno: ')
#qtdade_aluno = 5

alunos = 0
totalM=0
totalH=0
bons=0
porc=0
while alunos <5:
    alunos = alunos + 1
    sexo = input('Digite se F para Mulher ou M para Homem :')
    altura = float(input('Digite a altura: '))
    status_fisico = input('Digite a condição fisica, se: 1=bom ou 2=regular ou 3=ruim: ')

    if(sexo == 'F' and altura > 1.7):
        totalM=totalM +1
    else:
        totalH=totalH +1
    if(sexo == "H" and status_fisico == 1):
        bons = bons +1
        porc +bons * 100/ totalH


print('Total de mulheres altas :', totalM)
print('Porcentagem de homens bons', porc)
