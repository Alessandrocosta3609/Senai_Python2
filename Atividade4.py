# Exercicio 3


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










# Exercicio 4


numero_mais_alto = 0
numero_mais_baixo = 0
altura_mais_alta = -1
altura_mais_baixa = 999

for i in range(3):
    print(f"\nAluno {i+1}:")
    numero = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura (em cm): "))

   
    if altura > altura_mais_alta:
        altura_mais_alta = altura
        print(altura)
        numero_mais_alto = numero

    
    if altura < altura_mais_baixa:
        altura_mais_baixa = altura
        print(altura)
        numero_mais_baixo = numero

print(f"\nAluno mais alto: Nº {numero_mais_alto} com {altura_mais_alta:.1f} cm")
print(f"Aluno mais baixo: Nº {numero_mais_baixo} com {altura_mais_baixa:.1f} cm")