# print("-" *30)
# print("Cadastro de Clientes")
# print("-" *30)
# print("-" *30)
# print("Cadastro de Clientes")
# print("-" *30)
# print("-" *30)


#Se quisermos alterar por exemplo um caractere temos que fazer no codigo todo.



# #Agora o mesmo exemplo usando Função

# def linhas():
#     print("*" * 30)

# def titulos():
#     linhas()
#     print("Cadastro usando Funções")
#     linhas()

# titulos()

# #Função com Parametro 

# def titulos(texto):
#     linhas()
#     print(texto)
#     linhas()

# titulos("Imprime o que eu quiser")
# titulos("Imprime na hora que eu quiser")
# titulos("Imprime no momento que eu quiser")

# #print(type(titulos))

# def cumprimentos(nome):
#     print(f"Ola {nome} seja bem vindo(a)")

# cumprimentos("Ana")
# linhas()
# cumprimentos("Alessandro")
# linhas()
# cumprimentos("Matheus")
# linhas()

# # Função com Retorno
# def somar (n1,n2):
#     return n1 + n2
# res = somar(5,3)
# print(f"A soma é :{res}")



# Função com Condicional


def validar(idade):
    if idade>= 18 :
        return("Maior de Idade")
    else:
        return("Menor de Idade")

print(validar(18))
print(validar(17))


# Função sem Return , apenas executa algo

def somar(a,b):
    print(a+b)
somar(4,7)


# E se fosse guardar o resultado numa variavel?

res = somar(4,7)
print(res)

# Para Corrigir , utilizamos o Return ( Ele agora devolve o valor para o programa!!)

def somar(a,b):
    return a + b
print(somar(4,7))

res = somar(4,7)
print(res+10)



# # Nota de Aluno ( Sem Return )
# def calcular(n1,n2):
#     print(f"A média é {(n1+n2)/2}")
# calcular(8,6)
# if calcular >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")


# Nota de Aluno ( Com Return )
def calcular(n1,n2):
     return (n1+n2)/2
media = calcular(6,6)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# Usando as duas

def somar(a,b):
    return a + b
def resultado (res):
    print(f"O Resultado é {res}")
valor = somar(5,3)
resultado(valor)

def cont(num):
    for i in range(1,num +1):
        print(i)
cont(5)