# # Variaveis de Impressao


# nome = "Alessandro"
# idade = 52
# peso = 70.0

# # Normal seria printar assim

# print ("Nome :",nome,"Idade :",idade,"Peso",round (peso,2))

# # Mas usamos f de String

# print(f"Nome :{nome} Idade : {idade} Peso : {peso:.2f}")

# # No modo Antigo era assim , usando módulos

# print("Nome :%s , Idade : %i, Peso : %.2f" %(nome , idade , peso))

# # Podemos usar o .format tambem

# print("Nome :{} , Idade : {}, Peso : {:.2f}" .format(nome , idade , peso))

# # Os prints são iguais , mas os métodos diferentes

# # Alinhamento faz assim 

# print("{:>10}".format("Python"))  # Alinha a Direita
# print("{:<10}".format("Python"))  # Alinha a Esquerda
# print("{:^10}".format("Python"))  # Centralizado


# # Formatação Numerica

# print("{}".format(3.1454234)) # Assim Imprime com casas decimais infinitas
# print("{:.2f}".format(3.1454234))# Assim imprime com 2 casas decimais por exemplo

# # Operadores de Atribuição

# x = 1
# #x = x + 1 # A linha debaixo é a mesma coisa , de forma correta

# x += 1
# print(x)

# y = 1
# #y = y - 1
# y -= 1
# print(y)

# z = 1
# #z = z * 1

# z *= 1
# print(z)

# w = 1
# w /= 1
# print(w)

# v =  1
# v %= 1

# print(v)

# x = 8
# x /= 2
# print(x)


# idade = 25
# print(f"Idade atual {idade} Daqui 5 anos terá {idade+5}")




# # Raiz Quadrada
# n1 = 49
# print(f" A raiz quadrada de {n1} é {n1**0.5}")

# # Digite um numero para saber ele ao quadrado

n2 = int(input (" Digite um numero  :") )
quad = n2 * n2
print ( f" O quadrado desse numero é : {quad}")

nome = input (" Digite seu Nome :")
sobrenome = input ( "Qual seu Sobrenome  ? :")
idade =int( input ("Qual sua Idade ? :"))
ra = int( input (" Qual seu RA  :"))
b1 = float (input( " Digite a 1ª Nota Bimestral  :"))
b2 = float (input( " Digite a 2ª Nota Bimestral  :"))
b3 = float (input( " Digite a 3ª Nota Bimestral  :"))
b4 = float (input( " Digite a 4ª Nota Bimestral  :"))

media = (b1+b2+b3+b4)/4
print(f" Olá {nome} {sobrenome} !! Você tem {idade} anos e sua média é {media}")


calc = int(input(" Digite um número para ver sua Tabuada : "))
print ( f"{calc} X 1 = {calc*1}")
print ( f"{calc} X 2 = {calc*2}")
print ( f"{calc} X 3 = {calc*3}")
print ( f"{calc} X 4 = {calc*4}")
print ( f"{calc} X 5 = {calc*5}")
print ( f"{calc} X 6 = {calc*6}")
print ( f"{calc} X 7 = {calc*7}")
print ( f"{calc} X 8 = {calc*8}")
print ( f"{calc} X 9 = {calc*9}")
print ( f"{calc} X 10 = {calc*10}")



