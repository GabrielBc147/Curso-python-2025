# Faça um programa que receba o raio de uma circunferência em centímetros. 
# Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.
# Área:  x.xx
# Perímetro:  y.yy
import math as mh

def get_input():
        while True:
            try:
                raio = float(input("Entre com o raio da circunferência: "))
                if raio <= 0:
                     print("O raio deve ser um número positivo!")
                     continue
                return raio # Return entrega o resultado de uma função para quem a chamou (Pense na função como uma cozinha: você faz um pedido (chama a função), ela prepara o prato (executa o código), e o return é o garçom trazendo o prato até você.Sem return, a função faz tudo lá dentro, mas não te entrega nada.)
            except ValueError as err:
                print("Valor inválido!")
                continue
            
raio = get_input()

area = mh.pi * (raio ** 2)
perimetro = 2 * mh.pi * raio

area = round(area, 2)
perimetro = round(perimetro,2)

print("A area dessa circunferencia é:", area, "e o preimetro é:", perimetro)
       
        

