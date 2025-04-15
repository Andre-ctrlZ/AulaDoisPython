#Estrutura conidiconal em Python ☆*: .｡. o(≧▽≦)o .｡.:*☆

idade = int (input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")

#Valor numero positivo ou negativp

numero = int (input("Digite sua numero: "))
if numero > 0:
    print(f"Número {numero} é positivo")
elif numero < 0:
    print(f"Numero {numero} é negativo")
else:
    print("Número é zero")

#Verificar se o número é par ou impar
mumero = int (input("Digite o primeiro numero: "))
if numero % 2 == 0:
    print ("O numero é par!")
else:
    print ("O numero é impar!")
