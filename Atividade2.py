idade = int(input("Digite sua Idade : "))
if (idade >= 16 and idade <18) or idade >=70:
    print("Você tem ",idade,"anos , e o voto para você é FACULTATIVO")
elif idade <16:
    print("Você tem",idade,"anos e ainda não pode VOTAR !!")
else :
    print("Você tem",idade,"anos , e o voto é OBRIGATÓRIO")

# elif idade >= 18 and idade <70 :
#     print("Você tem",idade,"anos , e o voto é OBRIGATÓRIO")
# else:
#     print("Você tem",idade,"anos , e o voto é FACULTATIVO ")



categoria = int(input("Digite sua idade e veja qual categoria de natação voce se encaixa : "))

if categoria <5:
    print("Você não se enquadra em nenhuma categoria ainda !!!")
elif categoria >= 5 and categoria <=7:
    print("Você tem",categoria,"anos , e está na categoria Infantil A")
elif categoria >=8 and categoria <= 11:
    print("Você tem",categoria,"anos , e está na categoria Infantil B")
elif categoria >= 12 and categoria <= 13 :
    print("Voce tem ",categoria,"anos , e está na categoria Juvenil A")
elif categoria >= 14 and categoria <= 17 :
    print("Voce tem ",categoria,"anos , e está na categoria Juvenil B")
else :
    print("Voce tem ",categoria,"anos , e está na categoria Adultos")

n1 = float(input("Digite o 1º Número : "))
n2 = float(input("Digite o 2º Número : "))

print("\nEscolha a operação : ")
print("1   - Soma")
print("2   - Subtração")
print("3   - Multiplicação")
print("4   - Divisão")

opcao = int(input("Digite o numero da operação : "))
if opcao ==1:
    print(f"Resultado da Soma :{n1 + n2}")
elif opcao ==2:
    print(f"Resultado da Subtração :{n1 - n2}")
elif opcao ==3:
    print(f"Resultado da Multiplicação :{n1 * n2}")
elif opcao ==4:
    print(f"Resultado da Divisão :{n1 / n2}")
else :
    print("Opção Inválida")