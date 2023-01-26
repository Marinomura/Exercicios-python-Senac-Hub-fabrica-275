#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande,
# cada uma sendo vendida respectivamente por R$10,00, R$12,00 e R$15,00.
# Faça um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda,
# o algoritmo informe qual o valor total da compra.

qtdade_p=int(input("Digite a quantidade de camisetas P: "))
qtdade_m=int(input('Digite a quantidade de camisetas M: '))
qtdade_g=int(input('Digite a quantidade de camisetas G: '))

cam_p=10
cam_m=12
cam_g=15

print('\n')

print(f"O valor total da venda é de R$: {qtdade_p*cam_p+qtdade_m*cam_m+qtdade_g*cam_g:.2f} ")