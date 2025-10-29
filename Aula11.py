# frutas = ["Berinjela",'Pimentão','Pepino','Chuchu',"Tomate"]
# procurar = input("Digite a Fruta : ").strip().capitalize()
# print(procurar)
# if procurar in frutas:
#     print("Está na Posição :", frutas.index(procurar))
# else:
#     print("Esta fruta não está na lista !")    

    #strip remove os espaços
    #capitalize coloca a 1a letra maiuscula


# numero = []
# print(numero)

# numero.append (1)
# numero.append (2)
# numero.append (3)
# numero.append (4)
# numero.append (5)
# print(numero)


# #Usando Loop

# numero = []
# for i in range (1,101):
#     numero.append(i)
# print(numero)

# # Usando while

# numero = []
# count = 0
# while count<100 :
#     count += 1
#     numero.append(count)
# print(numero)


# nomes = []
# cont = 0
# while cont<5:
#     cont += 1
#     total =input("Digite o nome da pessoa :")
   


# pessoas = []  

# while len(pessoas) < 5:
#     nome = input("Digite o nome da pessoa : ").strip()
#     pessoas.append(nome)

# print("\nLista de pessoas:")
# for i in pessoas:
#     print(i)

# lista =[]
# for i in range (1,11):
#     lista.append(i)
# lista.reverse()
# print(lista)


# Adicionando numero inteiro fornecido pelo usuario

 
# numeros = []
# while True :
#     num = int(input("Digite um numero (ou 0 para sair):"))
#     if num == 0:
#         break
#     numeros.append(num)
# print(numeros)


# extend adiciona varios valores de uma vez
# marcas = ["Fiat","Renault","Ford","Toyota"]

# novos = ["JAC","BYD","Chevrolet"]

# print(marcas)


# #Para adicionar os novos na lista
# marcas = ["Fiat","Renault","Ford","Toyota"]

# novos = ["JAC","BYD","Chevrolet"]

# marcas.extend(novos)
# print(marcas)

lista = []
for i in range(3):
    lista.append(i)
    lista.append(i + 10)
    

print(lista)