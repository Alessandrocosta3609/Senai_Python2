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