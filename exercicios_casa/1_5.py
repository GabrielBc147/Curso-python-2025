# Faça um programa que receba dois valores A e B. 
# Faça a potência desses dois valores e retorne o resultado:
# a ^ b = z


def valor_letra(nome):
    while True:
        try:
            valor = float(input(f"Insira o valor de {nome}: ")) #Esse f vem de f-string, que significa formatted string (ou string formatada). É uma forma moderna e prática de inserir variáveis diretamente dentro de uma string.
            return valor
        except ValueError:
            print(f"Erro, o valor de {nome} deve ser um numero!")

a = valor_letra("A")
b = valor_letra("B")

z = a ** b

z = round(z,2)

print(a,"^",b ,"=", z)