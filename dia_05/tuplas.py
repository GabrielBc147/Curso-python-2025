# Tupla são listas que nao podem ser alteradas nos seus elementos
# %%

dados_teo = [32, 1, "Casado", "dev"]
dados_teo

# %%
dados_teo.append("3241.43") # .append adiciona mais um elemento a lista 

# %%
# tupla_teo = 32, 1, "Casado", "dev goLang"
tupla_teo = (32, 1, "Casado", "dev goLang",["Antonia","Maria"])

print(type(tupla_teo))
print(tupla_teo)

# %%

#tupla_teo[0] = 28 # Exemplo do erro que ocorre ao tentar alterar uma tupla
tupla_teo[-1].append("Ana") # Exemplo de uma mudança que é possivel dentro da lista presente em uma tupla


# %%
