nome = input("Digitar o nome")
idade = int(input("Digite a idade"))
if idade <=2:
    print("{} está com {} e pela idade é considerado um bebê".format(nome,idade))
if idade ==3 and idade <=11:
    print("{} está com {} e pela idade é considerado uma criança".format(nome,idade))
if idade ==12 and idade <=21:
    print("{} está com {} e pela idade é considerado um jovem". format(nome,idade))
if idade ==22 and idade <=64:
    print("{}está com {} e pela idade é considerado um adulto".format(nome,idade))
if idade ==65 and idade<=100:
    print("{} está com {} e pela idade é considerado um idoso".format(nome,idade))
if idade >101:
    print("{} está com {} e pela idade é considerado um velhinho".format(nome,idade))
