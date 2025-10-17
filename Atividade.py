cateto_oposto = float(input( " Ditige o valor do Cateto Oposto: "))
cateto_adjacente = float(input( " Digite o Valor do Cateto Adjacente: "))


soma = cateto_adjacente**2 + cateto_oposto**2
hipotenusa = soma**(1/2)

print(f" O Valor da Hipotenusa é : {hipotenusa:.2f}")

