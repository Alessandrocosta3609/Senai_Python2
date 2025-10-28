# cidades = ["São Paulo ","Itu","Santo André","Osasco","São Paulo"]

# cidades[1]= "Caracas Picuibas"
# print(cidades)

# # Para adicionar valores no final da lista use o append

# cidades.append ("Barueri")
# print(cidades)

# #Para adicionar no inicio da lista use o insert
# cidades.insert(0,"Jundiaí")
# print(cidades)
# print(len(cidades))

# #para remover elementos , use  o remove

# cidades.remove("Jundiaí")
# print(cidades)

# # Para remover o ultimo elemento de uma lista , use o pop
# cidades.pop()
# print(cidades)
# print(len(cidades))

# # Para ordenar alfabético  ou numérico use o sort

# cidades.sort()
# print(cidades)

# # Para fazer o reverso  use o reverse
# cidades.reverse()
# print(cidades)

# cidades.append("São Paulo")

# #Para saber quantas vezes um item se repete numa lista use o count
# print(cidades.count("São Paulo"))

# #Para deletar posição especifica use o del
# del cidades[5]
# print(len(cidades))
# print(cidades)


# Pesquisar um registro numa lista

# localizar = input("Digite um nome para pesquisar :" )
# if localizar in cidades:
#     print(" Existe na lista")
# else :
#     print( "Não existe ")

# # Percorrendo a lista e imprimir cada uma em uma linha ( Iterar )
# for cidade in cidades:
#     print(cidade)


# # Para Somar
# numeros = [1,2,3,4,5]
# print(sum(numeros))




# # Lista dentro de lista

# notas = [[8,7,9],[10,5,3],[2,4,8]]
# print(notas)
# print(notas[2])
# print(notas[1][2])



# Aninhar Bairros com a Região
bairros = [["Brasilandia","Pirituba","Jaraguá"] ,
["Tiradentes","Guaianazes","São Matheus"],
["Grajau","Jd Miriam","Capãp Redondo"],
["Lapa","Leopoldina","Vila Lobos"]]
regioes = ["Zona Norte","Zona Leste","Zona Sul","Zona Oeste"]

print(bairros)
for i in range(len(bairros)):
    print(f"{regioes[i]}: {bairros[i]}")


compra = [10.2,3.25,16.3,["tomate","sabonete","arroz"]]
print(compra)
produtos = compra[3]
print(produtos)
total = compra[0] + compra [1] + compra[2]
print(total)

letra = ["a","b","c"]
num = [1,2,3]
concat = [letra + num]
print(concat)

tudo = (letra , num)
print(tudo)
print(type(tudo))

tudo = [letra , num]
print(tudo)
print(type(tudo))

print(f"Letras :{tudo[0]}")
print(f"Números :{tudo[1]}")



#Descobrir Posição do elemento em uma lista :Utilize o método index
frutas = ["Berinjela","Pimentão","Pepino","Chuchu","Tomate"]
procurar = input("Digite a Fruta que deseja procurar :")

if procurar in frutas :
    print("Está na posição :" , frutas.index(procurar))
else :
    print("Esta fruta não esta na lista !")
