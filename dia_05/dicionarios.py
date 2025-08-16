# Dicionarios são um conjuntos de pares chave associados a um valor
# São usados para chamadas de API
# %%

lista = [2, 132, "teo", ["ds", "de", "da"], True]

lista = [2]

# %%

# pares de chave / valor (Associa uma chave a um valor)


dados_teo = {"sobrenome":"Calvo",
    "nome":"Teo",
    "filhos": True, 
    "formação":["estatistica","bigdata datascience"],
    "cargos":[
        {"nome":"ds jr.","empresa":"tapps"},
        {"nome":"ds pl.","empresa":"sas"},
        {"nome":"ds sr.","empresa":"boticario"},
        {"nome":"ds espec.","empresa":"via varejo"},
    ]
    } 



# %%

print(dados_teo)
print(dados_teo["formação"][-1])
print(dados_teo["cargos"][-1]["empresa"])

# %%

dados_teo["estado civil"] = "casado"

# %%

print("Chaves:", dados_teo.keys()) # Mostra todas as chaves presentes em dados_teo
print("valores:", dados_teo.values()) # Mostra todos os valores presentes em dados_teo
print("itens:", dados_teo.items()) # Lista de 'Tuplas' com chave e valor associdado

# %%

for i in [10,20,45,28,"Teo"]:
    print(i)

# %%

for i in dados_teo:
    print(i, "->", dados_teo[i]) # primeira parte exibe somente a chave, segunda parte busca o valor associado a chave buscada

# %%

for chave, valor in dados_teo.items(): # Reconhece os dados das 'Tuplas' como duas "colunas distintas" e associa os dois valores declarados a cada um deles
    print(chave, "->", valor)