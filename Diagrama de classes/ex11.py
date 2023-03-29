# CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E 
# RETORNE A MÉDIA DOS NÚMEROS.
#numpy.median()

def calc_media(lista):
    media =0
    for i in lista:
      media = sum(lista)/len (numero)
    return media
numero=[2,2,2,3,3,3,]
print (calc_media (numero))