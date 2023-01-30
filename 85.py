#Escrever um algoritmo para ler a quantidade de horas/aula de duas professoras e o valor por hora recebido por cada um.
# Mostrar na tela qual dos professores tem salário total maior.​
prof1=float(input('Digite a quantidade de horas aula da professora 1: '))
prof2=float(input('Digite a quantidade de horas aula da professora 2: '))
vl_prof1=float(input('Digite o valor da hora/aula da professora 1:R$ '))
vl_prof2=float(input('Digite o valor da hora/aula da professora 2:R$ '))
vl_hora_aula1=prof1*vl_prof1
print(f'O valor recebido é de: R$ {vl_hora_aula1:.2f}')
vl_hora_aula2=prof2*vl_prof2
print(f'O valor recebido é de: R$ {vl_hora_aula2:.2f}')
if vl_hora_aula1>vl_hora_aula2:
    print(f'A professora 1 tem o sálario de R$ {vl_hora_aula1} que é maior que da professora 2, que tem o sálario de R$: {vl_hora_aula2}.')    
else:
    print(f'A professora 2 tem o sálario maior que a professora 1.')