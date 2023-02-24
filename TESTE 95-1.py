# Abre o arquivo para leitura
arquivo = open('Usuário ex 95.txt', 'r')

# Coloca todas as linhas em memoria
linhas = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

usuarios = []
espacos = []
total = 0
for l in linhas:
    linha = l.split()
    usuarios.append(linha[0])
    espacos.append(int(linha[1]))
total = sum(espacos)

# Abre o arquivo para escrita
arquivoRelatorio = open('relatorio.txt', 'w')
arquivoRelatorio.write(
    'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
arquivoRelatorio.write(
    '------------------------------------------------------------------------')
arquivoRelatorio.write('\nNr.  Usuario        Espaco utilizado     %% do uso')

for i in range(0, len(usuarios)):
    espacoMB = espacos[i] / (1024.0 * 1024.0)
    percentualUso = espacos[i] / total
    arquivoRelatorio.write('\n%d - %s - %.2f MB - %.2f%%' %
                       (i + 1, usuarios[i], espacoMB, percentualUso * 100.0))

arquivoRelatorio.write('\nEspaco total ocupado: %.2f MB' %
                   (total / (1024.0 * 1024.0)))
arquivoRelatorio.write('\nEspaco medio ocupado: %.2f MB' %
                   (total / len(usuarios) / (1024.0 * 1024.0)))
# Fecha o arquivo
arquivoRelatorio.close()
