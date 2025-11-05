# # Variáveis Local e Global

# # Variavel Local

# def exibir():
#     nome = "Ana"
#     print("Dentro da Função ",nome)

# exibir()

# # A Variável nome existe dentro da função e não funciona fora dela.


# # Variável Global

# nome = "João"

# def exibir():
#     print("Dentro da Função" , nome)


# exibir()

# print("Fora da Função ", nome)
# # A Global está fora da Função e pode ser chamada em outro trecho do código


# # Alterar variavel global

# # cont = 0
# # def somar():
# #     cont += 1
#     print("Dentro da Função :",cont)
# somar()

# Desta maneira o python entende que foi criada a variavel local cont , mas ela nao existe dentro da função


# Alterar a Variavel Global ( Com global)

# cont = 0
# def somar():
#     global cont
#     cont += 1
#     print("Dentro da Função ,:", cont)
# somar()
# print("Dentro da Função ,:", cont)


# # # Assim podemos alterar o valor da variavel pois ela está declarada como global

# # E se tiver local com o mesmo nome da global ?
# nome = " Alessandro"
# def exibir_nome():
#     nome = "Paulo"
#     print("Dentro da função :", nome)
# exibir_nome()
# print("Fora da Função  :", nome)

# x = 100 # Variavel Global
# def testar():
#     print("Antes :",x)

# testar()

# def somar(x):
#     return x +1
# cont = 0
# cont = somar(cont)
# print("Contador:",cont)

# Input
# nome = input("Diga seu Nome :")
# def saudacao():    
#     print(f"Olá , {nome}.\nSeja Bem Vindo(a!)")
# saudacao()

# #saudacao()

# # Input com Return

# def idades():
#     anos = int(input("Qual sua idade? :"))
#     return anos
# exibir_idade = idades()
# print(f"{nome} , Voce tem {exibir_idade} anos !")





def conta():
    n1 = float(input("Digite o Valor 1:"))
    n2 = float(input("Digite o Valor 2:"))
    soma = n1 + n2
    sub  = n1 - n2
    mult = n1 * n2
    div  = n1 / n2
    return soma,sub,mult,div
soma,sub,mult,div = conta()
print(f"A Soma  é : {soma}")
print(f"A Subtração   é : {sub}")
print(f"A Multiplicação  é : {mult}")
print(f"A Divisão  é : {div}")