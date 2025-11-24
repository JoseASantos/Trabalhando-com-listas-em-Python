#Tuplas
#Funcionamento da estrutura e onde utilizar
#Criando Tuplas
#tuplas são imutáveis lista é mutavel
#Exemplo 1
frutas = (" laranja", "pera", "uva") #tupla de strings

letras = tuple("python") #tupla de caracteres

numeros = tuple([1, 2, 3, 4, 5]) #tupla de números a partir de uma lista

pais = ("Brasil",) #tupla com um único elemento

#acessando diretamente o elemento da tupla
print(frutas[0]) #saída: laranja
print(letras[2]) #saída: t
print(numeros[4]) #saída: 5
print(pais[0]) #saída: Brasil

#Exemplo 2 indices negativos
print(frutas[-1]) #saída: uva
print(letras[-3]) #saída: h
print(numeros[-5]) #saída: 1
print(pais[-1]) #saída: Brasil

#Exemplo 3 tuplas aninhadas

matriz = (
    (1, "a", 3),
    ("b", 5, 6),
    (7, 8, "c"),
)
#Acessando elementos em tuplas aninhadas
print(matriz[0][1]) #saída: a
print(matriz[2][2]) #saída: c
print(matriz[1][0]) #saída: b
print(matriz[2][0]) #saída: 7

#Exemplo 4 fatiamento de tuplas sintaxe: tupla[inicio:fim:passo]

tupla =("p", "y", "t", "h", "o", "n",)
print(tupla[1:5]) #saída: ('y', 't', 'h', 'o')
print(tupla[:4]) #saída: ('p', 'y', 't', 'h')
print(tupla[3:]) #saída: ('h', 'o', 'n')
print(tupla[::2]) #saída: ('p', 't', 'o')
print(tupla[1::2]) #saída: ('y', 'h', 'n')
print(tupla[::-1]) #saída: ('n', 'o', 'h', 't', 'y', 'p')

#Métodos de tuplas
#count()
#Retorna o número de ocorrências de um elemento na tupla
tupla = (1, 2, 3, 2, 4, 2, 5)
ocorrencias = tupla.count(2)

#index()
#Retorna o índice da primeira ocorrência de um elemento na tupla
tupla = ("a", "b", "c", "d", "b")
indice = tupla.index("b")

#len()
#Retorna o número de elementos na tupla
tupla = (10, 20, 30, 40, 50)
tamanho = len(tupla)

