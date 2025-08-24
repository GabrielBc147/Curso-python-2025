# Faça um programa que receba um número em segundos, converta esse número para horas, minuto e segundos.
# Exemplos:

# Entrada: 556
# Saída: 0:9:16
# 
# Entrada: 140153
# Saída: 38:55:53

entrada = int(input("Insira o numero de segundos: "))

hh = entrada // 3600 # Divisão inteira
mm = (entrada //60) % 60
ss = entrada % 60

print(f"{hh}:{mm}:{ss}")