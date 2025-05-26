#Manipulando arquivos em python
#Gravando um arquivo

arquivo = open("BOOSTIO.txt", "w")
for linha in range(1, 101):
    arquivo.write(f'VAMO ESCULACHAR!\n')
arquivo.close()

#ler os dados de um arquivo:
arquivo = open("BOOSTIO.txt", "r")
for linha in arquivo.readlines():
    linha = linha.strip()
    print(linha)
arquivo.close()

with open("dados.txt", "w") as arquivo:
    arquivo.write("Vamos escapar")