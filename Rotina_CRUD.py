#Create
with open ("dados.txt", "w") as arquivo:
    arquivo.write("a\n")

#Read
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

#Update
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

#faz a modificação
with open("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() == "a":
            arquivo.write("b\n")
        else:
            arquivo.write(linha)


#Delete

with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
