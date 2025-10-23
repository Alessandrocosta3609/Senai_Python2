numero = int(input("Digite o número para treinar sua tabuada : "))

acertos = 0
erros = 0

for i in range(1, 11):
    resposta = int(input(f"{numero} x {i} = "))
    resultado_correto = numero * i
    if resposta == resultado_correto:
        print("Correto!")
        acertos += 1
    else:
        print(f"Que pena, você errou! O valor correto é {resultado_correto}.")
        erros += 1

print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")
