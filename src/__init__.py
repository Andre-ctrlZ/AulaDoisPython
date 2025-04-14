#Entrada de dados *^____^* (•ˋ _ ˊ•)

nome = input("Insira um nome: ")
idade = int (input("Insira sua idade: "))
peso = float(input("Insira o peso: "))
print (f"{nome} tem {idade} anos e pesa {peso:.1f} kilos")

#Variavel dentro da entrada de dados

nome = input ("Insira um nome: ")
idade = int (input(f"Insira a idade de {nome}: "))
print (f"{nome} tem {idade} anos")