# dic1 = {
# "nome" : " Alessandro",
# "idade" : 52
# }
# dic2 = dic1.copy()
# # Assim é uma cópia distinta 
# print(dic1)
# print(dic2)



# dic1 = {
# "nome" : " Alessandro",
# "idade" : 52
# }
# dic2 = dic1
# # Assim é um espelho de uma para o outro , se alterar 1 reflete no outro
# dic2["idade"] = 40
# print(dic1)
# print(dic2)



# dic1 = {
# "nome" : " Alessandro",
# "idade" : 52
# }
# dic2 = dic1.copy()
# # Assim cria uma cópia , mas q  uando alteramos o dic2 , o dic 1 permanece igual
# dic2["idade"] = 40
# print(dic1)
# print(dic2)



# Adicionando dicionário dentro de dicionário
# dados1 = {"nome" : "Alessandro ", "idade": 25}
# dados2 = {"cidade":"São Paulo","profissão" :"Engenheiro"}
# #print(dados1+dados2) Assim dá erro , não deixa concatenar
# dados1.update(dados2)
# #O correto é assim para concatenar
# print(dados1)

# #Tamanho do dicionário
# print(len(dados1))
# print(dados1["nome"])

# # Dicionario Aninhado

# pessoa = {
#     "nome":"Alessandro",
#     "idade": 52 ,
#     "endereco":{
#         "logradouro":"Rua Lourenco Candido",
#         "numero":212,
#         "Bairro":"Jardim Arize",
#         "cidade": " São Paulo",
#     }
# }
# print(pessoa["endereco"]["logradouro"])


# pessoas = {
#      "pessoa1": {"nome":"Alessandro","idade":52,"altura":1.66},
#      "pessoa2": {"nome":"Kelly","idade":48,"altura":1.52},
#      "pessoa3": {"nome":"Matheus","idade":18,"altura":1.70},
#      "pessoa4": {"nome":"Luiza","idade":12,"altura":1.66},

# }
# print(pessoas["pessoa3"]["idade"])


# #Acrescentando Valores em tipos de dados Diferentes


# aluno ={

#     "nome":"João",
#     "notas": {"Matematica":5,"Portugues":10,"Geografia":7},
#     "materias":["Matematica", "Portugues", "Geografia"]
# }
# print(aluno["nome"])
# print(aluno["notas"]["Portugues"])
# print(aluno["materias"][2])

# aluno["notas"]["Ingles"]=9

# aluno["materias"].append("Ingles")

# print(aluno)

# Criar um Sistema do Zero


# aluno ={}
# aluno["nome"] = input("Digite o nome : " )
# aluno["media"] = float(input("Digite o media : ") )
# if aluno["media"] >= 7 :
#     aluno["status"] = "Aprovado"
# elif aluno['media'] >= 5:
#     aluno["status"] = " Recuperação"
# else :
#     aluno["status"] = "Reprovado"
# print(aluno)


# for c,v in aluno.items():
#     print(c,":",v)




produtos = {
    "celular": 1500.00,
    "teclado": 125.98,
    "monitor": 899.90,
    "gabinete": 255.00,
    "headset": 789.90,
    "gpu": 5376.00,
    "cpu": 1890.90,
}

while True:
    consulta = input("Informe o produto (0 para sair): ").lower()
    if consulta == "0":
        break

    if consulta in produtos:
        print(f"Produto '{consulta}' custa R$ {produtos[consulta]:.2f}")
    else:
        print("Produto não encontrado!")
        cadastro = input("Deseja cadastrar esse produto? (sim/não): ").lower()
        if cadastro == "sim":
            nome_produto = consulta 
            valor_produto = float(input("Digite o valor do produto: R$ "))
            produtos[nome_produto] = valor_produto
            print(f"Produto '{nome_produto}' cadastrado com sucesso por R$ {valor_produto:.2f}!\n")

print("\n=== Lista Atualizada de Produtos ===")
for nome, preco in produtos.items():
    print(f"{nome.capitalize()} -> R$ {preco:.2f}")


