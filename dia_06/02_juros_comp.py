# Zen of python - coleção de 19 princípios orientadores
# Type hint - dicas no codigo 
# %% 

def juros_comp(aporte:int, taxa:float, anos:int)->float: # tipo das variaveis mostrados na sequencia, não forçam o tipo do objeto, são apenas dicas
    """Juros_comp serve para calcular o retorno financeiro a partir de um aporte. 
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) 
    para calculo do valor a ser retornado.
    
    aporte: 
        um numero inteiro, que represente o valor em R$
        
    taxa:
        um numero float entre 0 e 1 que represente o valor da taxa de juros
        
    anos:
        um numero interio >= 1 que representa o tempo que o investimento tera liquidez
        """ # documentação desta função 
    return aporte * (1 + taxa) ** anos

# %%

juros_comp(aporte=20000, taxa=0.13, anos= 20) # Ordem importa! Escrever a variavel com um sinal de igual para seu valor é uma boa pratica neste caso 

# %%

