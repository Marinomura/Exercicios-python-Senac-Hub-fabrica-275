consumo = int(input("Informe qual foi o consumo de água em m³: "))
#consumo2 = consumo
total = 0
while consumo > 30:
  total = total + 11.08
  consumo -= 1
while  20 < consumo <= 30:
  total = total + 6.55
  consumo -= 1
while 15 < consumo <= 20:
  total = total + 6.49
  consumo -= 1
while 10 < consumo <= 15:
  total = total + 6.46
  consumo -= 1
while 5 < consumo <= 10:
  total = total + 1.16
  consumo -= 1
if consumo <= 5:
  total = total + 37.47

print(f"O consumo de {consumo}m³ de água gerou uma fatura no valor de:\nR${total:.2f} referente à água.\n"
f"R${total*0.8:.2f} referente ao esgoto.\nTotalizando R${total+total*0.8:.2f}.")
