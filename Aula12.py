# # Tuplas são semelhantes as Listas , porém não podem ser alteradas , são imutáveis .
# #  Porém podem ser feitas conversões de dados .

# paises = "Brasil","Paraguai","Uruguai","Mexico"
# print(type(paises))

# for pais in paises:
#     print(pais)


# lista_carros = ["Gol","Corolla","Ranger","Kadett","Fusca","Clio"]
# tupla_carros = tuple(lista_carros)

# print(f"Lista Carros : {lista_carros}")

# lista = ["Vermelho","Azul","Amarelo","Laranja"]

# lista.append("Verde")
# lista[0] = "Preto"
# print(lista)

# tupla = ("Vermelho","Azul","Amarelo","Laranja")
# print(type(tupla))
# print(tupla[2:4])
# # tupla[0] = "Preto"  Não é possivel alterar elementos como fazemos em listas .

# tupla = ("Alessandro",)
# print(tupla)
# print(type(tupla))

# tupla = ("Alessandro")
# print(tupla)
# print(type(tupla))



# num = 10,20,30,40,50
# print(num)
# print(type(num))
# print(num[3])
# print(num[-1])
# print(num[1:4])

# tupla = ("Vermelho","Azul","Amarelo","Laranja")
# print(type(tupla))
# for i in tupla:
    
#     print (i , end=",")


# Verificar se um elemento esta numa tupla 

# tupla = ("Vermelho","Azul","Amarelo","Laranja")
# cor = input("Digite a cor para ver se está na lista : ").capitalize()
# if cor in tupla :
#     print(f"Sim , {cor} está na lista !")
# else :
#     print(f"Não , {cor} não está na lista ! ")


# tupla1 = (1,2,3)
# tupla2 = (4,5,6)
# concat = tupla1 +tupla2
# print(concat)

# #Desenpacotamento
# tuplaCarros = ("Uno","Ranger","Golf")
# carro3,carro1,carro2= tuplaCarros
# print(carro3)
# print(carro1)
# print(carro2)
# print(type(carro3))


# pessoa = ("Alessandro" , 52 , 1.85 ,72.5 )
# nome,idade,altura,peso = pessoa

# print(nome)
# print(idade)
# print(altura)
# print(type(peso))



# Desempacotamento em Sequencia

# tuplaCarros =("Uno","Ranger","Golf","Tucson","Elantra","Fiesta")
# carro1 , *carros= tuplaCarros
# print(carro1)
# print(*carros)

# tuplaCarros =("Uno","Ranger","Golf","Tucson","Elantra","Fiesta")
# *carros,carro1 , carro2= tuplaCarros
# print(*carros)
# print(carro1)
# print(carro2)



# tuplaCarros =("Uno","Ranger","Golf","Tucson","Elantra","Fiesta")
# carro1 ,*carros , carro2= tuplaCarros
# print(carro1)
# print(*carros)
# print(carro2)

# Converter Lista em Tupla :

lista = ["Uno","Ranger","Golf","Tucson","Elantra","Fiesta"]

tupla = tuple(lista)
print(type(tupla))


# Converter tupla em lista

tupla =("Uno","Ranger","Golf","Tucson","Elantra","Fiesta")
lista = list(tupla)
print(lista)
lista.append("Focus")
print(lista)

tupla = tuple(lista)
print(tupla)


