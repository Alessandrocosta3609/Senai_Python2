# if --> Se
# else --> Se não 
# elif --> Se não Se


# idade = int(input( " Digite sua Idade :"))
# if (idade >= 18) :
#     print(" Você é maior de idade ")
# else :
#     print(" Você não tem idade ainda , seu muleke !!")



# n1 = float(input("Digite a Nota 1 : " ))
# n2 = float(input("Digite a Nota 2 : " ))
# n3 = float(input("Digite a Nota 3 : " ))
# n4 = float(input("Digite a Nota 4 : " ))
# media = (n1+n2+n3+n4)/4
# print("Lembrando que a média para passar tem que ser 7!!!")




# #media = float(input("Digite a média : "))

# if media >= 9 :
#     print("Você é Espetacular !!!" , "Foi Aprovado com a nota",media)
# elif media>7:
#     print("Você é bom cara , passou com a nota",media)

# elif media ==7 :
#     print("Você foi mais ou menos , cara !!","Passou raspando com a nota",media)
# elif media >=5:
#     print("Voce foi Razoável !!","Estude um pouco mais , sua nota foi ",media)

# else:
#     print("Você foi Reprovado !!!","Sua média foi",media)

# if aninhado

usuario = input(" Digite o user : ")
if usuario == "admin":
    senha = input("Digite a senha: " )

    if senha == "1234":
        print("Acesso Permitido!")
    else:
        print("Senha Errada!")
else:
    print("Acesso Negado!")