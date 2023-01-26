Nome = input ("Aluno")
Disciplina = input ( "Nome da Disciplina")
Nota1 = int(input("Nota Primeira prova"))
Nota2 = int(input("Nota Segunda prova"))
Nota3 = int(input("Nota terceira prova"))
Media = (Nota1+Nota2+Nota3)/3

print("Aluno:\n",Nome)
print("Disciplina: \n",Disciplina)
print("Prova 1: \n", Nota1)
print("Prova 2:\n", Nota2)
print("Prova 3 : \n", Nota3)
print("Media do Aluno: \n", Media)

# agora com todas as informações na mesma linha

if(Media > 6):
    print(f"As notas foram: {Nota1}, {Nota2}, {Nota3} Media do "f"aluno {Nome} foi {Media:.1f}, foi o suficiente para passar.")

else:
    print(f"As notas foram: {Nota1}, {Nota2} e {Nota3} Media "f"do aluno {Nome} foi {Media:.1f}, Não foi o suficiente para passar.")