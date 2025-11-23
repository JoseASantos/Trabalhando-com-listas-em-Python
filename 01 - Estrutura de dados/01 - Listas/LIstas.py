#Criando listas
#sintaxe: lista = [elemento1, elemento2, elemento3]
#Exemplo 1
frutas = ["laranja","maca","uva"]
print(frutas)

#frutas = []
#print(frutas)  #Acessando o primeiro elemento da lista

#Exemplo 2

letras = list("python")
print(letras)   

#Exemplo 3
numeros = list(range(10))
print(numeros)

#Exemplo 4
carros = ["Ferrari","F8", 4200000, 2020, 2900, "São Paulo", True]
print(carros)

#Acesso direto
#utilizando indices
#sintaxe: lista[indice]
frutas[0]  #Acessando o primeiro elemento da lista
frutas[1]  #Acessando o segundo elemento da lista

#indices negativos
#sintaxe: lista[-indice]
frutas[-1]  #Acessando o ultimo elemento da lista
frutas[-2]  #Acessando o penultimo elemento da lista

#Listas aninhadas
#criar estruturas mais complexas, bidimensionais
#sintaxe: lista = [[elemento1, elemento2], [elemento3, elemento4]]
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

print(matriz[0])    #Acessando a primeira linha
print(matriz[0][1]) #Acessando o segundo elemento da primeira linha 
print(matriz[2][0]) #Acessando o primeiro elemento da terceira linha
print(matriz[1][2]) #Acessando o terceiro elemento da segunda linha 
print(matriz[-1][-1]) #Acessando o ultimo elemento da ultima linha

#Fatiamento de listas (slicing)
#sintaxe: lista[inicio:fim:passo]
#exemplo 1

lista =["p","y","t","h","o","n"]
print(lista[2:])  #Acessando do indice 2 até o final
print(lista[:3])  #Acessando do inicio até o indice 2
print(lista[1:4]) #Acessando do indice 1 até o indice 3
print(lista[0:3:2]) #Acessando do indice 0 até o indice 2, pulando de 2 em 2
print(lista[::]) #Acessando todos os elementos da lista
print(lista[::-1])#Acessando todos os elementos em ordem reversa

#Iteração em listas com for
#sintaxe: for elemento in lista:
#exemplo 1
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

#exemplo 2 enumerate
#sintaxe: for indice, elemento in enumerate(lista):
for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")

#Compreensão de listas
#sintaxe: nova_lista = [expressao for item in lista if condicao]
#exemplo 
#sintaxe tradicional

numeros = [1, 2, 3, 4, 5]
pares =[]
for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
print(pares)

#exemplo 2
#sintaxe com list comprehension
numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 ==0]
print(pares)

#exemplo 3
#modificando 

numeros = [1, 2, 3, 4, 5]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

#Metodos da classe List

#Exemplo 1 append
#sintaxe: lista.append(elemento)
lista = []
lista.append(1)  #Adiciona o elemento 1 ao final da lista
lista.append("python")  #Adiciona o elemento "python" ao final da lista
lista.append([40, 30, 20])  #Adiciona a lista [40,30,20] ao final da lista

print(lista)

#Exemplo 2 clear
#sintaxe: lista.clear()

#lista.clear()  #Remove todos os elementos da lista
print(lista)

#Exemplo 3 copy
#sintaxe: nova_lista = lista.copy()

l2 = lista.copy()

print(lista)

print(id(l2), id(lista))  #Verificando se sao objetos diferentes

l2[0] = 2

print(lista)
print(l2)

#Exemplo 4 count
#sintaxe: lista.count(elemento)

cores = ["azul", "verde", "amarelo", "azul", "vermelho", "azul"]
cores.count("azul")  #Conta quantas vezes o elemento "azul" aparece na lista
cores.count("verde") #Conta quantas vezes o elemento "verde" aparece na lista
cores.count("vermelho") #Conta quantas vezes o elemento "vermelho" aparece na 

#exemplo 5 
#sintaxe: lista.extend(iteravel)
linguagens = ["python", "java", "c++"]

print(linguagens)

linguagens.extend(["javascript", "ruby"])  #Adiciona os elementos da lista ao final da lista linguagens
print(linguagens)

#exemplo 6 index
#sintaxe: lista.index(elemento)

print(linguagens.index("java"))  #Retorna o indice do elemento "java"
print(linguagens.index("python")) #Retorna o indice do elemento "python"

#exemplo 7 pop
#sintaxe: lista.pop(indice)
linguagens.pop()  #Remove e retorna o ultimo elemento da lista
print(linguagens)
linguagens.pop(0)  #Remove e retorna o elemento do indice 0
print(linguagens)

#exemplo 8 remove
#sintaxe: lista.remove(elemento)
linguagens.remove("c++")  #Remove a primeira ocorrencia do elemento "c++"
print(linguagens)

#exemplo 9 reverse
#sintaxe: lista.reverse()
linguagens.reverse()  #Inverte a ordem dos elementos da lista
print(linguagens)

#exemplo 10 sort
#sintaxe: lista.sort() 
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()  #Ordena os elementos da lista em ordem crescente
print(numeros)
numeros.sort(reverse=True)  #Ordena os elementos da lista em ordem decrescente
print(numeros)  
numeros.sort(key=lambda x: len(x))  #Ordena os elementos da lista pelo tamanho
print(numeros)
numeros.sort(key = lambda x:len(x), reverse=True)  #Ordena os elementos da lista pelo tamanho em ordem decrescente
print(numeros)
#avaliação

