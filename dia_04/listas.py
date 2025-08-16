# %%

# uma maneria de definir listas
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

# %%

gabriel = ["Gabriel", "Bueno", 24, False,"Solteiro", 2348.25 ]
print(gabriel)

# %%
type(gabriel)

# %%

# indice em listas de python, se inicia no zero

#idade
print(gabriel[2])

#renda
print(gabriel[5])

# nome 
print(gabriel[0])

# %%

idades = [28, 42, 43, 35, 39, 28, 38]

print("soma idades:", sum(idades))

print("qtde idades:", len(idades)) # len, conta a qtde de elementos dentro do "conteiner"

print("media idades:", sum(idades)/len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

# %%

teo = ["Teo Calvo", 
       32, 
       True, 
       "Casado", 
       ["estagiario","ds jr.", "ds pl", "ds sr", "head"],
       [1500, 4000, 4550, 6500, 10000],
       ["Ana", "Maria","Claudia"]]

print("Tamanho de teo:", len(teo))

print(teo[4][0])

exs = teo[4]
primeira_ex = exs[0]
print(primeira_ex)

# %%

tamanho = len(teo)
pos = tamanho - 1
teo[pos][0] # em uma lista, para descobrir qual o ultimo elemento sem 'hardcode'

exs = teo[pos]

teo[pos][len(exs) - 1] # para descobrir o ultimo elemento da lista de ex

# %%

teo[-1][-1] # -1 representa o ultimo elemento da lista

# %%

# primeiros 4 elementos
teo[0:4]

# %%

teo[4][3:5] # é a mesma coisa que = teo[4][-2:]
# %%
# primeiros 4 elementos
teo[:4] # mesma coisa que teo[0:4]

# %%
# teo[ start : stop ]

# %%

salarios = teo[5]
salarios[::-1]

# teo[ start : stop : step]