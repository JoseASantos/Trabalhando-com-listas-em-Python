#Dicionario
#Criação e acesso
#conjunto não ordenado de pares chave:valor
#sintaxe: dicionario = {chave1: valor1, chave2: valor2}
#exemplo

pessoa = {"nome": "Guilherme", "idade":28, "telefone": "3333-1234"} #declarações equivalentes

#pessoa = dict(nome = "Guilherme", idade = 28) #declarações equivalentes

pessoa ["telefone"] = "3333-1234"

#exemplo acessando e inserindo

pessoa["nome"]
pessoa["idade"]
pessoa["telefone"]

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "9988-1781"

print(pessoa)

#Dicionarios aninhados
#Exemplo

contatos ={
    "guilherme@gmail.com":{"nome":"Guilherme","telefone": "3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna","telefone":"3443-2121"}
}

telefone = contatos ["giovanna@gmail.com"]["telefone"]
print(telefone)

#iterar dicitionarios
#forma mais comum é utilizando for
#Exemplo

for chave in contatos:
    print(chave, contatos[chave])



#Metodos da classe dict
#.clear()
#Apaga valores do dicionario

#.copy()
#copia valores do dicionario

#.fromkeys()
#cria chaves

#.get()
#

#.itens()

#.keys()

#.pop

#.popitem

#.setdefault

#.update

#


