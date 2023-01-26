#Faça um algoritmo que receba o preço de um produto, #
# calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

valor_prod=float(input("Digite o valor do produto: "))
valor_desconto=(valor_prod*0.10)
novo_preço=valor_prod-valor_desconto
print(f"O Valor do produto com desconto é {novo_preço:.2f}")
