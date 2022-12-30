import os
frutas = ['Maracuja', 'Laranja', 'Melancia', 'Morango', 'Banana']
cores = ['Azul', 'Preta', 'Vermelha', 'Verde', 'Amarelo']
linguagens = ['Python', 'C', 'Java', 'Html', 'CSS']

with open('frutas.txt', 'w', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)
    
with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)

with open('top_5_linguagens.txt', 'w', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']
for arquivo in arquivos:
    with open(arquivo, 'w') as arquivo:
        pass
