# # Podemos utilizar o comando while para criar Loop´s tambem 
# x = 0
# while x <10 :
#     print(x)
#     x = x + 1



# cadastro = (input("cadastre a senha :")) 
# cadastro2 = (input("confirme a senha :"))
# if cadastro == cadastro2:
#     print("Senha Cadastrada !") 
# else:
#     print("Cadastro errado")



# senha = ""
# while senha != cadastro:
#     senha = input("Digite a senha :")   
# print("Acesso Liberado !")

# Cadastro da senha com validação
# while True:
#     cadastro = input("Cadastre a senha: ")
#     cadastro2 = input("Confirme a senha: ")

#     if cadastro == cadastro2:
#         print("Senha cadastrada com sucesso!\n")
#         break  
#     else:
#         print("As senhas não conferem. Tente novamente.\n")


# while True:
#     senha = input("Digite a senha: ")

#     if senha == cadastro:
#         print("Acesso liberado!")
#         break
#     else:
#         print("Senha incorreta. Tente novamente.\n")



# soma = 0
# numero = int(input("Digite um número ( Ou Digite  0 para sair): "))

# while numero != 0:
#     soma += numero
#     numero = int(input("Digite outro número (Ou  Digite 0 para sair): "))

# print(f"A soma dos numeros digitados é: {soma}")





# # Criando Tabuada com while
# n  = int(input("Digite um numero para ver sua tabuada : "))
# i = 0
# while i != 10:
#     i += 1
#     print(f"{n} x {i} = {i * n}")




# Comparando os numeros digitados e imprimindo o maior
# n = 1
# aux = 0
# while n != 0 :
#     n = int(input(" Digite um Numero , ou Zero para Sair :"))
#     if n > aux:
#         aux = n
# print(f" O maior Numero digitado foi {aux}")


# Comando Continue no while

# cont = 0
# while cont < 10 :
#     cont += 1
#     if cont == 5:
#         continue 
#     print(cont)


total = 0
cont = 0
while True:
    nota = float(input("Digite a nota ou -1 para encerrar :"))
    if nota == -1:
        break
    total += nota
    cont += 1
media = total / cont
print(f"Média : {media}")

