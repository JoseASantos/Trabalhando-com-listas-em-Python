#Conjuntos
#estrutura de dados set
#Uma coleção de objetos únicos e não ordenados
#Criando Conjuntos
#sintaxe: set(iterável)
#Exemplo 1

numeros = set([1,2,3,1,3,4]) #conjunto de números a partir de uma lista com elementos duplicados
print(numeros) #saída: {1, 2, 3, 4}

letras = set("banana") #conjunto de caracteres a partir de uma string com letras repetidas
print(letras) #saída: {'b', 'a', 'n'}

linguagens = {"python", "java", "c++", "python"} #conjunto de strings com elemento duplicado
print(linguagens) #saída: {'c++', 'java', 'python'}

#Acessando os dados em um conjunto
#Conjuntos não suportam indexação ou fatiamento.
#Necessário converter para lista ou tupla
#sintaxe: lista = list(conjunto) ou tupla = tuple(conjunto)
#Exemplo
numero = {1,2,3,4,4,3,2,1}
#print(numeros[0]) #Gera um erro, pois conjuntos não suportam indexação

numero =list(numero) #converte o conjunto para uma lista
print(numero[0]) #saída: 1 (ou outro número, a ordem não é garantida)

#Iterar conjuntos
#pecorrer dados de um conjunto com for e enumerate
#sintaxe: for elemento in conjunto:
#Exemplo

carros = {"fusca", "gol", "celta"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}") #saída: 0: gol 1: celta 2: fusca (a ordem pode variar)

#Métodos da classe set
#union() retorna a união de dois conjuntos
#exemplo

conjunto_a = {1,2,3}
conjunto_b = {3,4,5}
uniao = conjunto_a.union(conjunto_b)
print(uniao) #saída: {1, 2, 3, 4, 5}

#.intersection() retorna a interseção de dois conjuntos
#exemplo
print(conjunto_a.intersection(conjunto_b)) #saída: {3}

#.difference() retorna a diferença entres dois conjuntos
#exemplo
print(conjunto_a.difference(conjunto_b)) #saída: {1, 2}
print(conjunto_b.difference(conjunto_a)) #saída: {4, 5}

#.symmetric_difference() retorna a diferença simétrica entre dois conjuntos
#exemplo
print(conjunto_a.symmetric_difference(conjunto_b)) #saída: {1, 2, 4, 5}

#.issubset() verifica se um conjunto é subconjunto de outro
#exemplo
print(conjunto_a.issubset(conjunto_b)) #saída: False
print(conjunto_b.issubset(conjunto_a)) #saída: False

#.isuperset() verifica se um conjunto é superconjunto de outro
print(conjunto_a.issuperset(conjunto_b)) #saída: False
print(conjunto_b.issuperset(conjunto_a)) #saída: False

#.isdisjoint() verifica se dois conjuntos são disjuntos (não possuem elementos em comum)
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}
print(conjunto_a.isdisjoint(conjunto_b)) #saída: True
print(conjunto_a.isdisjoint(conjunto_c)) #saída: False

#.add() adiciona um elemento ao conjunto

conjunto = {1,23} #cria um conjunto com os elementos 1 e 23
conjunto.add(25) #adiciona o elemento 25 ao conjunto
conjunto.add(23) #adiciona o elemento 23 ao conjunto (não terá efeito, pois 23 já está presente)
print(conjunto) #saída: {1, 23, 25}

#.discard() remove um elemento do conjunto, se estiver presente
conjunto.discard(23) #remove o elemento 23 do conjunto
print(conjunto) #saída: {1, 25}
conjunto.discard(100) #tenta remover o elemento 100 (não gera erro, pois 100 não está presente)

#.pop() remove e retorna um elemento arbitrário do conjunto

conjunto = {1, 2, 3, 4, 5}
elemento_removido = conjunto.pop()
print(f"Elemento removido: {elemento_removido}") #saída: Elemento removido: 1 (ou outro número, a ordem não é garantida)

#.remover() remove um elemento específico do conjunto, gera erro se o elemento não estiver presente
print(conjunto.remove(3)) #remove o elemento 3 do conjunto
print(conjunto) #saída: {2, 4, 5}
#print(conjunto.remove(10)) #gera um erro, pois 10 não está presente no conjunto

#.len() retorna o número de elementos no conjunto
conjunto = {10, 20, 30, 40, 50}
tamanho = len(conjunto)
print(tamanho) #saída: 5

#.in() verifica se um elemento está presente no conjunto
conjunto = {"maçã", "banana", "laranja"}
print("banana" in conjunto) #saída: True
print("uva" in conjunto) #saída: False
#.clear() remove todos os elementos do conjunto
conjunto.clear()   
print(conjunto) #saída: set()