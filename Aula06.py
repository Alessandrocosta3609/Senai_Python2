# Operadores Lógicos

# AND ----> Conjunção (E)    ----------> &&
# OR  ----> Disjunção (OU)   ----------> ||
# NOT ----> Negação (NÃO)    ----------> !


# print((5 > 2) and (10 > 3)) # Para ser True tem que satisfazer todas as condições
# print((5 > 2) and (3 > 10)) # Para ser True tem que satisfazer todas as condições


# print((5 < 2)  or ( 10 > 3)) # Para ser True tem que satisfazer 1 ou + condições
# print((5 < 2)  or ( 3 > 10)) # Para ser True tem que satisfazer 1 ou + condições



# print( not (5 == 5)) # O NOT retorna sempre o resultado INVERSO
# print( not (5 > 5)) # O NOT retorna sempre o resultado INVERSO


# idade = int(input( "Idade : "))
# documento = (input("Possui Documento ? : ")).upper()
# if idade >=18 and (documento == "SIM"  or documento == "S"):
#     print("Entrada Liberada")
# elif idade >=18 and (documento == "NÃO"  or documento == "N"):
#     print( "Maior de 18 , porém sem documento > Entrada Negada")
# else:
#     print("Entrada Negada")


feriado = False
fds = False 

if feriado or fds :
    print("Pode descansar")
else :
    print("Dia de Trabalho")