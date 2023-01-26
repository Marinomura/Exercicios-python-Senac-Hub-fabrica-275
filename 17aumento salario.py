#salario até R$ 280,00 (incluido): aumento de 20"
#entre r$280 e R$ 700: aumento de 14%
#entre R$ 700 e R$ 1500: aumento de 10%
#de 1500 em diante 5%
#após o aumento ser realizado, informe na tela:
#o salario antes do reajuste; o percentual de aumento aplicado;o valor do aumento;o novo salário,após o aumento

salario = float(input("Digite o salario do colaborador "))
au1 = (salario*0.2)+salario
au2 = (salario*0.15)+salario
au3 = (salario*0.1)+salario
au4 = (salario*0.05)+salario

if salario <=280:
    print(f"{salario} Salario antes do reajuste {au1} recebeu aumento de 20%")
elif salario >280 and salario <=700:
    print(f"{salario} Salario antes do reajute {au2} recebeu aumento de 15%")
elif salario >700 and salario <=1500:
    print(f"{salario} O salario antes do rajuste {au3} recebeu aumento de 10%")
elif salario >=1500:
    print(f"{salario}Sálario antes do reajuste {au4} recebeu aumento de 5%")
