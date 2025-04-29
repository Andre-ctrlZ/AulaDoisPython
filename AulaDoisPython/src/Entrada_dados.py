x = 1
while x<=10:
    print(x)
    x=x+1

#Tabuada adição
numero = int(input('Digite um numero: '))
x=1
while x <=10:
    print(numero+x)
    x=x+1

#Tabuada com acumulação
n=1
soma=0
while n<=10:
    x = int(input('Digite um numero: '))
    soma=soma+x
    n=n+1
    print(soma)

#Interrupção de repetição
x=1
while x<=10:
    if x==5:
        break
    print(x)
    x=x+1

#Lista
lista=[1,2,3,4,5]
for i in lista:
    print(i)

#imprimindo char
for char in "ragnarok":
    print(char)