# Faça um programa que receba o nome e a idade de uma pessoa. 
# 
# Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
# 	“Fulano, você não pode dirigir nem beber”
# 
# Para as pessoas entre 18 e 65 anos, exiba o aviso:
# 	“Fulano, bebida liberada! Só não vale dirigir!”
# 
# Para as pessoas com mais de 65 anos, exiba o aviso:
# 	“Fulano, beba com muita moderação!”

nome_usuario = input("Insira seu o nome: ")
idade_usuario = int(input("Insira sua idade: "))

if idade_usuario < 18:
    print(f"{nome_usuario}, você não pode dirigir nem beber")

elif idade_usuario < 65:
    print(f"{nome_usuario}, bebida liberada! Só não vale dirigir!")

else:
    print(f"{nome_usuario}, beba com muita moderação!")