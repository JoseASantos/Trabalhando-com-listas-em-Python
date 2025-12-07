print("\n Digite o Peso(t):")
peso = float(input())
print("\n Digite o preço por Tonelada:")
preco_por_tonelada = float(input())
valor_total = 0
valor_final = 0
#opcao_tipo_Cliente = 0
print("\n Tipo de Cliente:")
tipo_cliente = input()
if (tipo_cliente == "Novo cliente"):
    valor_total = peso * preco_por_tonelada
    print(valor_total)

elif(tipo_cliente == "Cliente fidelizado"):
    valor_total = peso * preco_por_tonelada
    desconto = 5/100
    valor_final = valor_total * (1 - desconto)
    print(f"{valor_final:.2f}")

elif(tipo_cliente == "Cliente premium"):
    valor_total = peso * preco_por_tonelada
    desconto = 10/100
    valor_final = valor_total *(1- desconto)
    print(f"{valor_final:.2f}")

else:
    print("Cliente especificado invalido")
    