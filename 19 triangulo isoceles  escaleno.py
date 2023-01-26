
#triangulo = base*altura
#isoceles =base*altura diferentes
#escaleno =base*altura valores diferentes

ladoA= input("Digite a altura do lado A: ")
ladoB = input("Digite a altura do lado B: ")
ladoC = input("Digite a medida do lado C: ")

if ladoA == ladoB == ladoC:
    print("É um equilatero")

elif ladoA ==ladoB !=ladoC:
    print ("É um isoceles")

elif ladoA !=ladoB !=ladoC:
    print("É um escaleno")