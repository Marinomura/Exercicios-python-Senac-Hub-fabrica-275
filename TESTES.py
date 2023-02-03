import time

salario = float(input('Digite o salário: '))
financiamento = float(input('Digite o valor do financiamento desejado: '))

valorBase = salario * 5
print('PROCESSANDO...')
time.sleep(1)

if financiamento <= valorBase:
    print('Financiamento Concedido!!')

else:
    print('Financiamento Negado!!')

print('Obrigado por nos consultar!')
