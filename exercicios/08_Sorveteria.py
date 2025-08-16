# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

texto = """Escolha o seu sorvete:
(1) Casquinha - R$1.00 
(2) Cascão - R$2.50
(3) Cestinha - R$4.00 
"""

tipo_sorvete = input(texto)

valor_item = 0

if tipo_sorvete == "1":
    valor_item = 1.0

elif tipo_sorvete == "2":
    valor_item = 2.50

elif tipo_sorvete == "3": 
    valor_item = 4.00

if valor_item == 0:
    print("Insira o numero do pedido correto!")

textosabor = """Escolha o seu sabor 
(1) morango
(2) creme
(3) chocolate
"""

sabor = input(textosabor)

if sabor == "1":
    saborEscolhido = "morango"
elif sabor == "2":
    saborEscolhido = "creme"
elif sabor == "3":
    saborEscolhido = "chocolate"


textocobertura = """Escolha a sua cobertura
(1) Caramelo - R$1.50 
(2) Morango - R$1.50
(3) chocolate - R$1.50
(4) sem cobertura - R$0.00
"""

cobertura = input(textocobertura)

if cobertura == "1":
    valor_item = valor_item + 1.5

elif cobertura == "2":
    valor_item = valor_item + 1.5

elif cobertura == "3": 
    valor_item = valor_item + 1.5

print("O valor total é : R$", valor_item)

 
