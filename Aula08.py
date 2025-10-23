# for i in [1,2,3,4,5,6]:
#     if i == 3:
#         print(i)
#         continue
#     print(i)




# Print dos Numeros Impares
for i in range(11):
    if i % 2 == 0 :
              continue
    print(f"Numero Impar : {i}")




# Print dos Numeros Pares
for i in range(11):
    if i % 2 != 0 :
              continue
    print(f"Numero Par : {i}")



# Print dos numeros menores e maiores que zero em uma lista
# for i in [8,10,-1,-7,7,-5,6]:
#        if i < 0 :
#               print("Menor que 0 :",i)
#               continue
#        print("Maior que 0 :",i)


# O break interrompe o Loop imediatamente

# for n in [1,2,3,4,5,6]:
#        print(n)
#        if n == 3:
#               print(f"Numero {n} encontrado  , encerrando o Loop")
#               break
# print("Fim do Programa !!")
       



# nomes = ["Natan","Alessandro","Fernanda","Guilherme","Carlos"]
# for nome in nomes:
#  if nome == "Carlos":
#        print(f"{nome} encontrado !!")
#        break
#  print(f"Verificando {nome}")
# else:
#       print(nome)       


# # Loop aninhado

# for x in range(1,4):
#       for y in range(1,4):
#             if y == 2:
#                   break
#             print(f"x={x},y={y}")



# Exercicio 1
for i in range(1,101):
       if i % 2 != 0:
              continue
       print(i)


# Exercicio 2

# soma = 0
# for i in range(5):
#     n = int(input(f"Digite o {i+1}º Numero :"))
#     soma += n
#     media = (soma/5)
# print("A soma é :", soma)
# print("A média é ",media)
   

# Exercicio 3 :

soma = 0
n = int(input("Quantidade de pessoas :"))
for i in range(n):
    idade = int(input(f"Digite a idade da {i+1}º pessoa :"))
    soma += idade
media = (soma//n)

# print("A soma é :", soma)
# print("A média é ",media)
if media <= 25 :
       print(f"A media de idade é {media} : Turma Jovem")
elif media >= 26 and media <=60 :
       print(f" A media de idade é {media} : Turma Adulta")
else :
       print(f"A média de idade é {media} : Turma Idosa")
       