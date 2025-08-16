# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de garrafas de água
# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

texto = """Escolha a sua agua para comprar:
(1) Agua mineral natural - R$1.50
(2) Agua mineral com gas - R$2.50
"""

opcao = input(texto)

valor_item = 0
if opcao == "1":
   valor_item = 1.5

elif opcao == "2":
    valor_item= 2.5  
else:
    print("Entre com a opção correta, por favor!")

qtde = input("Quantas garrafas? ")
qtde = int(qtde)
valor_item = valor_item * qtde

print("Sua conta deu R$", valor_item)