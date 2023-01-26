#desconto 3% sindicato
#11% FGTS mas não é descontado
#salario liquido é o Bruto menos descontos
#hora trabalhada e quantidade de horas trabalhadas
#desconto de IR verificação
#salario= input("Digite o salario: ")
#fgts - calcular e mostrar o valor


hora_trab =float(input("Digite a valor da hora trabalhada: "))
qdade_hora_trab =float(input("Digite a quantidade de horas trabalhadas: "))
sbruto= hora_trab*qdade_hora_trab
fgts=(sbruto*0.11)
inss = (sbruto*0.10)
csind = 0.03*sbruto


if sbruto <=900:
    faixa1 = 900  # isento
    print(f"Se o Salario Bruto é R$ {faixa1} é isento de IR" )

    print (f"Valor do Sindicato R$ {csind:.2f}: ")
    print(f"INSS R$ {inss:.2f}:  ")
    print(f"Valor depositado de FGTS R$ {fgts:.2f}\n ")
    salarioliq =(sbruto - csind -inss)
    print(f"O salario liquido é R$ {salarioliq:.2f}:" )

elif sbruto >900 and sbruto<=1500:
    faixa2 = (sbruto * 0.05)
    print(f"Salario bruto R$ {sbruto:.2f}: ")
    print(f"Valor do Sindicato R$ {csind:.2f}:")
    print(f"IR R$ {faixa2:.2f}: ")
    print(f"INSS R$ {inss:.2f}: ")
    print(f"Valor depositado do FGTS R$ {fgts:.2f}\n")
    salarioliq = (sbruto - csind - inss)
    print(f"O salario liquido é R$ {salarioliq:.2f}:")

elif sbruto >1500 and sbruto <=2500:
    faixa3 = (sbruto * 0.1)
    print(f"Salario bruto R$ {sbruto:.2f}: ")
    print(f"Valor do Sindicato R$ {csind:.2f}:")
    print(f"IR R$ {faixa3:.2f}: ")
    print(f"INSS R$ {inss:.2f}:")
    print(f"Valor depositado do FGTS R$ {fgts:.2f}\n ")
    salarioliq = (sbruto - csind - inss)
    print(f"O salario liquido é R$ {salarioliq:.2f}: ")

elif sbruto  >=2500:
    faixa4 = (sbruto * 0.2)
    print(f"Salario bruto R$ {sbruto:.2f}:  ")
    print(f"Valor do Sindicato R$ {csind:.2f}:")
    print(f"IR R$ {faixa4:.2f}:  ")
    print(f"INSS R$ {inss:.2f}:  ")
    print(f"Valor depositado do FGTS R$ {fgts:.2f}\n ")
    salarioliq = (sbruto - csind - inss)
    print(f"O salario liquido é R$ {salarioliq}: ")
