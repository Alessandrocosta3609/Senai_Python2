# Laço de Repetição ou Loop

# range (fim)   ---------->   range(5) gera de 0 a 4
# range (inicio,fim)   ---------->   range(1,6) gera de 1 a 5
# range (inicio,fim,intervalo)   ---------->   range(0,10,2) gera de 0 a 10 pulando de 2 em 2

# for i in range(110):
#     print("Palmeiras não tem mundial")
# print("Fim do Programa")


# for i in range(2,11,2):
#     print(i)

# for i in "SENAI":
#     print(i, end ="")
    


# for banana in [1,2,3,4,5] :
#     print(banana)


# print("1 elefante incomoda muita gente ")
# for i in range(2,11):
#     print(f"{i} elefantes incomodam muito mais")


# soma = 0
# for i in range(5):
#     n = int(input(f"Digite o {i+1}º numero:" ))
#     soma += n
       
# print("A soma é :", soma)



# Printar numeros pares e impares
# for numero in range(101):
#     if numero %2 == 0 :
#         print(numero, "PAR")
#     else :
#         print(numero,"IMPAR")


inicio = int(input("Digite o primeiro valor : "))
fim = int(input("Digite o ultimo valor : "))

for i in range(inicio,fim):
    print(i)