# Faça um programa que receba dois valores A e B.
# Faça a soma desses dois valores e retorne o resultado:
# Soma:  x.xx

def valor_letra(nome):
    while True:
        try:
            valor = float(input(f"Insira o valor de {nome}: ")) #Esse f vem de f-string, que significa formatted string (ou string formatada). É uma forma moderna e prática de inserir variáveis diretamente dentro de uma string.
            return valor
        except ValueError:
            print(f"Erro, o valor de {nome} deve ser um numero!")

valor_a = valor_letra("A")
valor_b = valor_letra("B")

soma = valor_a + valor_b

soma = round(soma,2)

print("A soma é:", soma)