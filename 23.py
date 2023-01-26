#A granja TecFrango possui um controle automatizado de cada frango da sua produção.
# No pé direito do frango há um anel com um chip de identificação, no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir.#
# Sabendo que o anel com chip custa R$ 4,00 e o anel de alimento custa R$ 3,50,
# faça um algoritmo para calcular o gasto total da granja (com base na quantidade de frangos digitada pelo usuário) para marcar todos os seus frangos.

qtdade_frango = int(input("Digite a quantidade de frango a serem marcados: "))

#anelchip = float(input("Digite o valor do anel com chip: R$ "))
#anelalim = float (input("Digite o valor do anel de alimentação: R$ "))
pe_dir=1*4
pe_esq=2*3.5


custo_anel_por_frango = pe_dir+pe_esq
print(f"O Custo da granja é de : R$ {custo_anel_por_frango:.2f} por frango ")
print(f'O custo da granja é de :R$ {custo_anel_por_frango*qtdade_frango:.2f}')