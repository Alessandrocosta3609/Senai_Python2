# Precedencias ou Prioridades 
# print(2+5*3)
# print((2+5)*3)          # Parenteses tem precedencia Maior
# print( 1 + 5 ** 2)      # Exponenciação tem Precedencia Maior
# print( (1 + 5) ** 2)    # Parenteses tem precedencia Maior
# print( 8 + 5 - 10)
# print( 8 + (5 - 10))    # Parenteses tem precedencia Maior
# print( 2 + 3 ** 2 * 2)  # Exponenciação tem Precedencia Maior

# print( 2 + 3 ** 2 * 2)  # Exponenciação tem Precedencia Maior

# print ( 2 ** 3 ** 4)    # 3^4 = 81 e depois 2^81  >>>>>>>>>>  Leitura da Direita para a Esquerda 

# print ( 6 + 4 * 2)      # Multiplicação tem Precedencia Maior

# print ( 4 * 9 + 5)      #Multiplicação tem Precedencia Maior
# print ( (6 + 7) *9)     # Multiplicação tem Precedencia Maior

# print ( (15 + 20 )- 30) # Parenteses tem precedencia Maior

# print ( 6 + 5 ** 2)     # Exponenciação tem precedencia Maior

# print(-.01 + 0.10)      # .01 == 0.01

# print ( .01 == 0.01 )   # True

# print(abs(-5)-5)        # Retira o Sinal e mostra o valor absoluto


# # Operadores de Comparação

# print ( 6 > 3)           # Maior que
# print (4  < 8)           # Menor que
# print ( 8 <= 8)          # Menor ou igual a
# print ( 18 >= 9 )        # Maior ou igual a
# print ( 8 == 8)          # Igual a ( só um = Utilizamos para criar Variaveis )
# print ( 3 != 9)          # É Diferente de 



# Entrada de Dados  == input

# #input("Digite seu Nome : ") # Solicitou a entrada e não armazenou nada............

# nome = input ( " Digite seu Nome : ")
# sobrenome = input ( " Digite seu Sobreome : ")
# idade = int (input ( " Digite a sua Idade : "))
# peso = float (input ( " Qual seu Peso ? : "))
# altura =  float (input (" Digite sua Altura  : "))

# print(altura)
# imc = round( peso/(altura*altura) , 2)
# fullname = nome + sobrenome 

# print( "Olá , " , fullname )
# print ( " Seu IMC é : ", imc )



# n1 = int(input( " Digite o primeiro numero : "))
# n2 = int(input( " Digite o segundo numero : "))
# soma = n1 + n2
# divisao = round(n1/n2 , 2)
# multiplicacao = n1*n2

# print ( " A Soma dos numeros 1 e 2  é : ",soma)
# print ( " A divisão do Numero 1 pelo Numero 2 é :" , divisao)
# print ( " O numero 1 multiplicado pelo numero 2 é :" , multiplicacao)

# UTILIZANDO O  f de string 


nome = input ( " Digite seu Nome : ")
sobrenome = input ( " Digite seu Sobreome : ")
idade = int (input ( " Digite a sua Idade : "))
peso = float (input ( " Qual seu Peso ? : "))
altura =  float (input (" Digite sua Altura  : "))
#imc = round( peso/(altura*altura) , 2)
imc =  peso/(altura*altura) 


print( "Ola " , nome,sobrenome , " . Voce tem ", idade ,"anos" , "Voce pesa , " , peso , "kg" , "Sua Altura é ", altura ,"metros", "seu IMC é",imc)

print( f" Ola {nome} {sobrenome} . Voce tem {idade} anos . Voce pesa {peso} kg . Sua altura é {altura } metros . Seu IMC é {imc :.2f}" )