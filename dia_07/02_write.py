# %%

txt = "Meu novo arquivo de texto!/n" # "/n" é uma quebra de linha

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="a") as open_file: # mode="w" escreve um texto e sobrepoe o anterior. mode="a" escreve um texto e adiciona ao texto atual.
    open_file.write(txt)


# %%
