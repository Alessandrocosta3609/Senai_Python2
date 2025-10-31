 # Dicionarios

# pessoa = {
#     "nome" : "Alessandro",
#     "idade": 25 ,
#     "altura": 1.66
    
    
# }
# print(pessoa)
# print(pessoa["nome"])
# print(pessoa["idade"])
# #print(pessoa["peso"])
# print(pessoa.get("peso"))


# # Adicionar nova chave
# pessoa["peso"] = 72.5

# print(pessoa)

# # Alterar Chave

# pessoa["peso"] = 72.0

# print(pessoa)

# # Removendo itens

# pessoa.pop("nome")
# print(pessoa)

# pessoa["nome"] = "Alessandro"



# Iterando

# aluno = {}
# aluno["nome"] = "Maria"
# aluno["media"]= 9.5
# aluno["turma"] = "3ºA"

# # items ----> retorna pares ( chaves , valor)
# # keys -----> retorna somente as chaves
# # values ---> retorna somente os valores

# print(aluno)
# for chave,valor in aluno.items():
#     print(chave,valor)

# for chave in aluno.keys():
#     print(chave)

# for valor in aluno.values():
#     print(valor)

alunos = [
    {"nome": "João" , "nota" : 8},
    {"nome": "Maria" , "nota" : 7},
    {"nome": "Lucas" , "nota" : 3},
]
print(alunos)
for aluno in alunos:
    print(aluno["nome"],"tirou",aluno["nota"])





pessoa = {
    "nome" : "Alessandro",
    "idade": 52 ,
    "altura": 1.66,
    }

if "idade" in pessoa :
    print("Existe")
else :
    print("Não Tem")

    # Limpar Dicionario

pessoa.clear()
print(pessoa)

produtos = {
    "mouse" :  40.00,
    "Teclado": 125.98,
    "Monitor": 899.90,
    "Gabinete": 255.00,
    "Headset": 789.90,
    "gpu"    : 5376.00,
    "cpu"    : 1890.90,

}


while True :
    consulta = input("Informe o produto (0 para sair) :")
    if consulta == "0" :
        break
    if consulta in produtos:
        print(f"Produto {consulta} custa {produtos[consulta]}")
    else :
        print(f"Produto {consulta} não encontrado !")