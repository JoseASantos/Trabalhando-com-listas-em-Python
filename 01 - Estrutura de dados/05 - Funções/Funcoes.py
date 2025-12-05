#FUNÇÕES
#O QUE SÃO?
#Blodo de código identicado com nome e pode receber uma lista de parametros, e que podem retornar ou não valores.
#Exemplo
def exibir_mensagem():
    print("Olá Mundo")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"seja bem vindo {nome}!")

exibir_mensagem()

exibir_mensagem2(nome = "Guilherme")

exibir_mensagem_3()

exibir_mensagem_3("Cheppie")

#Retornando Valores
# utilizando return
#retorna "none" por padrão
#diferente de outras linguagens pode retornar mais de um valor
#exemplo

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1

    return antecessor, sucessor

def func_3():
    print ("Olá mundo!")

print(calcular_total([10,20,34])) #64
print(retorna_antecessor_e_sucessor(10)) #9,11
print(func_3())#none

#ARGUMENTOS NOMEADOS

#EXEMPLO
def salvar_carro(marca, modelo, ano, placa):
    #salvar carro no banco
    print("Carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","Palio", 1999,"ABc-1234")
salvar_carro(marca= "Fiat", modelo = "Palio", ano= 1999, placa="ABC-1234")

#Args e kwargs
#definição (*args e **kwargs), recebe valores como tupla e dicionário respectivamente
#Exemplo
def exibir_proema(data_extenso, *args, **kwargs):
    texto ="\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_proema("04/12/2025","zen of Python","beautiful is better than ugly.", autor = "Tim peter", ano = 1999)






