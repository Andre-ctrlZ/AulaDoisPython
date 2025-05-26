z = [5, 4, 6]
print (z)
print(z[2], z[1], z[0])

#Calcular média com lista
notas = [6, 7, 8, 9]
soma = 0
x = 0
while x < len(notas):  # Corrigido para usar o comprimento da lista
    soma += notas[x]
    x += 1
media = soma / len(notas)  # A média é calculada com o tamanho da lista
print(f"A média é {media}")

#Percorrer lista com len(), len obtem o tamanho da lista
lista=[6, 7, 8, 9]
y = 0
while x < len(lista):
    print(lista[y])
    y += 1

#Adicionar elementos a lista.
lista.append(10)
print(lista)

letras = ['a', 'b', 'c']
print(letras)
letras.append('d')
print(letras)

lista =[1,2,3,4,5]
print(lista)
lista.remove(5)#remover elemento
print(lista)
lista.pop(3)#remover por posição no indice
print(lista)
del lista[0]
print(lista)

lista=[1,2,3,4,5]
numero= int (input("Digite um numero: "))
if numero in lista:
    print(f"O numero {numero} está na lista")
else:
    print("O numero não está na lista")

lista = [1,2,3,4,5,6]
for item in lista:
    print(item)